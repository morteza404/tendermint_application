import array
import six.moves.cPickle as pickle
import json
from collections import defaultdict
from gzip import GzipFile
from os.path import getmtime
import struct
from time import time
import os
from hashlib import md5
from itertools import chain, count
from tempfile import NamedTemporaryFile
import sys
import zlib

from six.moves import range

def calc_replica_count(replica2part2dev_id):
    base = len(replica2part2dev_id) - 1
    extra = 1.0 * len(replica2part2dev_id[-1]) / len(replica2part2dev_id[0])
    return base + extra


class RingReader(object):
    chunk_size = 2 ** 16

    def __init__(self, filename):
        self.fp = open(filename, 'rb')
        self._reset()

    def _reset(self):
        self._buffer = b''
        self.size = 0
        self.raw_size = 0
        self._md5 = md5()
        self._decomp = zlib.decompressobj(32 + zlib.MAX_WBITS)

    # @property
    # def close(self):
    #     return self.fp.close

    def seek(self, pos, ref=0):
        if (pos, ref) != (0, 0):
            raise NotImplementedError
        self._reset()
        return self.fp.seek(pos, ref)

    def _buffer_chunk(self):
        chunk = self.fp.read(self.chunk_size)
        if not chunk:
            return False
        self.size += len(chunk)
        self._md5.update(chunk)
        chunk = self._decomp.decompress(chunk)
        self.raw_size += len(chunk)
        self._buffer += chunk
        return True

    def read(self, amount=-1):
        if amount < 0:
            raise IOError("don't be greedy")

        while amount > len(self._buffer):
            if not self._buffer_chunk():
                break

        result, self._buffer = self._buffer[:amount], self._buffer[amount:]
        return result    

    @property
    def md5(self):
        return self._md5.hexdigest()


class RingData(object):
    """Partitioned consistent hashing ring data (used for serialization)."""

    def __init__(self, replica2part2dev_id, devs, part_shift,
                 next_part_power=None, version=None):
        self.devs = devs
        self._replica2part2dev_id = replica2part2dev_id
        self._part_shift = part_shift
        self.next_part_power = next_part_power
        self.version = version
        self.md5 = self.size = self.raw_size = None

        for dev in self.devs:
            if dev is not None:
                dev.setdefault("region", 1)

    # @property
    # def replica_count(self):
    #     """Number of replicas (full or partial) used in the ring."""
    #     return calc_replica_count(self._replica2part2dev_id)

    @classmethod
    def deserialize_v1(cls, gz_file, metadata_only=False):
        """
        Deserialize a v1 ring file into a dictionary with `devs`, `part_shift`,
        and `replica2part2dev_id` keys.

        If the optional kwarg `metadata_only` is True, then the
        `replica2part2dev_id` is not loaded and that key in the returned
        dictionary just has the value `[]`.

        :param file gz_file: An opened file-like object which has already
                             consumed the 6 bytes of magic and version.
        :param bool metadata_only: If True, only load `devs` and `part_shift`
        :returns: A dict containing `devs`, `part_shift`, and
                  `replica2part2dev_id`
        """

        json_len, = struct.unpack('!I', gz_file.read(4))
        ring_dict = json.loads(gz_file.read(json_len))
        ring_dict['replica2part2dev_id'] = []

        if metadata_only:
            return ring_dict

        byteswap = (ring_dict.get('byteorder', sys.byteorder) != sys.byteorder)

        partition_count = 1 << (32 - ring_dict['part_shift'])
        for x in range(ring_dict['replica_count']):
            part2dev = array.array('H', gz_file.read(2 * partition_count))
            if byteswap:
                part2dev.byteswap()
            ring_dict['replica2part2dev_id'].append(part2dev)

        return ring_dict

    @classmethod
    def load(cls, filename, metadata_only=False):
        """
        Load ring data from a file.

        :param filename: Path to a file serialized by the save() method.
        :param bool metadata_only: If True, only load `devs` and `part_shift`.
        :returns: A RingData instance containing the loaded data.
        """
        gz_file = RingReader(filename)

        # See if the file is in the new format
        magic = gz_file.read(4)
        if magic == b'R1NG':
            format_version, = struct.unpack('!H', gz_file.read(2))
            if format_version == 1:
                ring_data = cls.deserialize_v1(
                    gz_file, metadata_only=metadata_only)
            else:
                raise Exception('Unknown ring format version %d' %
                                format_version)
        else:
            # Assume old-style pickled ring
            gz_file.seek(0)
            ring_data = pickle.load(gz_file)

        if not hasattr(ring_data, 'devs'):
            ring_data = RingData(ring_data['replica2part2dev_id'],
                                 ring_data['devs'], ring_data['part_shift'],
                                 ring_data.get('next_part_power'),
                                 ring_data.get('version'))
        for attr in ('md5', 'size', 'raw_size'):
            setattr(ring_data, attr, getattr(gz_file, attr))
        return ring_data 

    

    def to_dict(self):
        return {'devs': self.devs,
                'replica2part2dev_id': self._replica2part2dev_id,
                'part_shift': self._part_shift,
                'next_part_power': self.next_part_power,
                'version': self.version}

ring_dict = RingData.load("/home/shahbazi/Desktop/rings/account.ring.gz").to_dict()

del ring_dict["replica2part2dev_id"]

# print(ring_dict)

print(ring_dict["devs"][0]["replication_ip"])

# with open("/home/shahbazi/Desktop/ring.json","w") as ring_json:
#     json.dump(ring_dict,ring_json)