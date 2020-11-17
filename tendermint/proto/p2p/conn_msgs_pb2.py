# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/p2p/conn_msgs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tendermint.third_party.proto.gogoproto import gogo_pb2 as third__party_dot_proto_dot_gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/p2p/conn_msgs.proto',
  package='tendermint.proto.p2p',
  syntax='proto3',
  serialized_options=_b('Z*github.com/tendermint/tendermint/proto/p2p'),
  serialized_pb=_b('\n\x19proto/p2p/conn_msgs.proto\x12\x14tendermint.proto.p2p\x1a&third_party/proto/gogoproto/gogo.proto\"\x0c\n\nPacketPing\"\x0c\n\nPacketPong\"R\n\tPacketMsg\x12!\n\nchannel_id\x18\x01 \x01(\x05\x42\r\xe2\xde\x1f\tChannelID\x12\x14\n\x03\x65of\x18\x02 \x01(\x05\x42\x07\xe2\xde\x1f\x03\x45OF\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"\xb8\x01\n\x06Packet\x12\x37\n\x0bpacket_ping\x18\x01 \x01(\x0b\x32 .tendermint.proto.p2p.PacketPingH\x00\x12\x37\n\x0bpacket_pong\x18\x02 \x01(\x0b\x32 .tendermint.proto.p2p.PacketPongH\x00\x12\x35\n\npacket_msg\x18\x03 \x01(\x0b\x32\x1f.tendermint.proto.p2p.PacketMsgH\x00\x42\x05\n\x03sumB,Z*github.com/tendermint/tendermint/proto/p2pb\x06proto3')
  ,
  dependencies=[third__party_dot_proto_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_PACKETPING = _descriptor.Descriptor(
  name='PacketPing',
  full_name='tendermint.proto.p2p.PacketPing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=103,
)


_PACKETPONG = _descriptor.Descriptor(
  name='PacketPong',
  full_name='tendermint.proto.p2p.PacketPong',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=117,
)


_PACKETMSG = _descriptor.Descriptor(
  name='PacketMsg',
  full_name='tendermint.proto.p2p.PacketMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='tendermint.proto.p2p.PacketMsg.channel_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\342\336\037\tChannelID'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eof', full_name='tendermint.proto.p2p.PacketMsg.eof', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\342\336\037\003EOF'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='tendermint.proto.p2p.PacketMsg.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=201,
)


_PACKET = _descriptor.Descriptor(
  name='Packet',
  full_name='tendermint.proto.p2p.Packet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packet_ping', full_name='tendermint.proto.p2p.Packet.packet_ping', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packet_pong', full_name='tendermint.proto.p2p.Packet.packet_pong', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packet_msg', full_name='tendermint.proto.p2p.Packet.packet_msg', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='sum', full_name='tendermint.proto.p2p.Packet.sum',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=204,
  serialized_end=388,
)

_PACKET.fields_by_name['packet_ping'].message_type = _PACKETPING
_PACKET.fields_by_name['packet_pong'].message_type = _PACKETPONG
_PACKET.fields_by_name['packet_msg'].message_type = _PACKETMSG
_PACKET.oneofs_by_name['sum'].fields.append(
  _PACKET.fields_by_name['packet_ping'])
_PACKET.fields_by_name['packet_ping'].containing_oneof = _PACKET.oneofs_by_name['sum']
_PACKET.oneofs_by_name['sum'].fields.append(
  _PACKET.fields_by_name['packet_pong'])
_PACKET.fields_by_name['packet_pong'].containing_oneof = _PACKET.oneofs_by_name['sum']
_PACKET.oneofs_by_name['sum'].fields.append(
  _PACKET.fields_by_name['packet_msg'])
_PACKET.fields_by_name['packet_msg'].containing_oneof = _PACKET.oneofs_by_name['sum']
DESCRIPTOR.message_types_by_name['PacketPing'] = _PACKETPING
DESCRIPTOR.message_types_by_name['PacketPong'] = _PACKETPONG
DESCRIPTOR.message_types_by_name['PacketMsg'] = _PACKETMSG
DESCRIPTOR.message_types_by_name['Packet'] = _PACKET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PacketPing = _reflection.GeneratedProtocolMessageType('PacketPing', (_message.Message,), dict(
  DESCRIPTOR = _PACKETPING,
  __module__ = 'proto.p2p.conn_msgs_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.p2p.PacketPing)
  ))
_sym_db.RegisterMessage(PacketPing)

PacketPong = _reflection.GeneratedProtocolMessageType('PacketPong', (_message.Message,), dict(
  DESCRIPTOR = _PACKETPONG,
  __module__ = 'proto.p2p.conn_msgs_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.p2p.PacketPong)
  ))
_sym_db.RegisterMessage(PacketPong)

PacketMsg = _reflection.GeneratedProtocolMessageType('PacketMsg', (_message.Message,), dict(
  DESCRIPTOR = _PACKETMSG,
  __module__ = 'proto.p2p.conn_msgs_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.p2p.PacketMsg)
  ))
_sym_db.RegisterMessage(PacketMsg)

Packet = _reflection.GeneratedProtocolMessageType('Packet', (_message.Message,), dict(
  DESCRIPTOR = _PACKET,
  __module__ = 'proto.p2p.conn_msgs_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.p2p.Packet)
  ))
_sym_db.RegisterMessage(Packet)


DESCRIPTOR._options = None
_PACKETMSG.fields_by_name['channel_id']._options = None
_PACKETMSG.fields_by_name['eof']._options = None
# @@protoc_insertion_point(module_scope)
