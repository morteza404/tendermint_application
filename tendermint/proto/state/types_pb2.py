# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/state/types.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tendermint.third_party.proto.gogoproto import gogo_pb2 as third__party_dot_proto_dot_gogoproto_dot_gogo__pb2
from tendermint.abci.types import types_pb2 as abci_dot_types_dot_types__pb2
from tendermint.proto.types import types_pb2 as proto_dot_types_dot_types__pb2
from tendermint.proto.types import validator_pb2 as proto_dot_types_dot_validator__pb2
from tendermint.proto.types import params_pb2 as proto_dot_types_dot_params__pb2
from ptendermint.roto.version import version_pb2 as proto_dot_version_dot_version__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/state/types.proto',
  package='tendermint.proto.state',
  syntax='proto3',
  serialized_options=_b('Z,github.com/tendermint/tendermint/proto/state'),
  serialized_pb=_b('\n\x17proto/state/types.proto\x12\x16tendermint.proto.state\x1a&third_party/proto/gogoproto/gogo.proto\x1a\x16\x61\x62\x63i/types/types.proto\x1a\x17proto/types/types.proto\x1a\x1bproto/types/validator.proto\x1a\x18proto/types/params.proto\x1a\x1bproto/version/version.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xca\x01\n\rABCIResponses\x12=\n\x0b\x64\x65liver_txs\x18\x01 \x03(\x0b\x32(.tendermint.abci.types.ResponseDeliverTx\x12:\n\tend_block\x18\x02 \x01(\x0b\x32\'.tendermint.abci.types.ResponseEndBlock\x12>\n\x0b\x62\x65gin_block\x18\x03 \x01(\x0b\x32).tendermint.abci.types.ResponseBeginBlock\"j\n\x0eValidatorsInfo\x12;\n\rvalidator_set\x18\x01 \x01(\x0b\x32$.tendermint.proto.types.ValidatorSet\x12\x1b\n\x13last_height_changed\x18\x02 \x01(\x03\"{\n\x13\x43onsensusParamsInfo\x12G\n\x10\x63onsensus_params\x18\x01 \x01(\x0b\x32\'.tendermint.proto.types.ConsensusParamsB\x04\xc8\xde\x1f\x00\x12\x1b\n\x13last_height_changed\x18\x02 \x01(\x03\"Y\n\x07Version\x12<\n\tconsensus\x18\x01 \x01(\x0b\x32#.tendermint.proto.version.ConsensusB\x04\xc8\xde\x1f\x00\x12\x10\n\x08software\x18\x02 \x01(\t\"\x89\x05\n\x05State\x12\x36\n\x07version\x18\x01 \x01(\x0b\x32\x1f.tendermint.proto.state.VersionB\x04\xc8\xde\x1f\x00\x12\x1d\n\x08\x63hain_id\x18\x02 \x01(\tB\x0b\xe2\xde\x1f\x07\x43hainID\x12\x19\n\x11last_block_height\x18\x03 \x01(\x03\x12K\n\rlast_block_id\x18\x04 \x01(\x0b\x32\x1f.tendermint.proto.types.BlockIDB\x13\xc8\xde\x1f\x00\xe2\xde\x1f\x0bLastBlockID\x12=\n\x0flast_block_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12=\n\x0fnext_validators\x18\x06 \x01(\x0b\x32$.tendermint.proto.types.ValidatorSet\x12\x38\n\nvalidators\x18\x07 \x01(\x0b\x32$.tendermint.proto.types.ValidatorSet\x12=\n\x0flast_validators\x18\x08 \x01(\x0b\x32$.tendermint.proto.types.ValidatorSet\x12&\n\x1elast_height_validators_changed\x18\t \x01(\x03\x12G\n\x10\x63onsensus_params\x18\n \x01(\x0b\x32\'.tendermint.proto.types.ConsensusParamsB\x04\xc8\xde\x1f\x00\x12,\n$last_height_consensus_params_changed\x18\x0b \x01(\x03\x12\x19\n\x11last_results_hash\x18\x0c \x01(\x0c\x12\x10\n\x08\x61pp_hash\x18\r \x01(\x0c\x42.Z,github.com/tendermint/tendermint/proto/stateb\x06proto3')
  ,
  dependencies=[third__party_dot_proto_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,abci_dot_types_dot_types__pb2.DESCRIPTOR,proto_dot_types_dot_types__pb2.DESCRIPTOR,proto_dot_types_dot_validator__pb2.DESCRIPTOR,proto_dot_types_dot_params__pb2.DESCRIPTOR,proto_dot_version_dot_version__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_ABCIRESPONSES = _descriptor.Descriptor(
  name='ABCIResponses',
  full_name='tendermint.proto.state.ABCIResponses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deliver_txs', full_name='tendermint.proto.state.ABCIResponses.deliver_txs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_block', full_name='tendermint.proto.state.ABCIResponses.end_block', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='begin_block', full_name='tendermint.proto.state.ABCIResponses.begin_block', index=2,
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
  ],
  serialized_start=258,
  serialized_end=460,
)


_VALIDATORSINFO = _descriptor.Descriptor(
  name='ValidatorsInfo',
  full_name='tendermint.proto.state.ValidatorsInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='validator_set', full_name='tendermint.proto.state.ValidatorsInfo.validator_set', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_height_changed', full_name='tendermint.proto.state.ValidatorsInfo.last_height_changed', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=462,
  serialized_end=568,
)


_CONSENSUSPARAMSINFO = _descriptor.Descriptor(
  name='ConsensusParamsInfo',
  full_name='tendermint.proto.state.ConsensusParamsInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='consensus_params', full_name='tendermint.proto.state.ConsensusParamsInfo.consensus_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\310\336\037\000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_height_changed', full_name='tendermint.proto.state.ConsensusParamsInfo.last_height_changed', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=570,
  serialized_end=693,
)


_VERSION = _descriptor.Descriptor(
  name='Version',
  full_name='tendermint.proto.state.Version',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='consensus', full_name='tendermint.proto.state.Version.consensus', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\310\336\037\000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='software', full_name='tendermint.proto.state.Version.software', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=695,
  serialized_end=784,
)


_STATE = _descriptor.Descriptor(
  name='State',
  full_name='tendermint.proto.state.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='tendermint.proto.state.State.version', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\310\336\037\000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chain_id', full_name='tendermint.proto.state.State.chain_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\342\336\037\007ChainID'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_block_height', full_name='tendermint.proto.state.State.last_block_height', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_block_id', full_name='tendermint.proto.state.State.last_block_id', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\310\336\037\000\342\336\037\013LastBlockID'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_block_time', full_name='tendermint.proto.state.State.last_block_time', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\310\336\037\000\220\337\037\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_validators', full_name='tendermint.proto.state.State.next_validators', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validators', full_name='tendermint.proto.state.State.validators', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_validators', full_name='tendermint.proto.state.State.last_validators', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_height_validators_changed', full_name='tendermint.proto.state.State.last_height_validators_changed', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='consensus_params', full_name='tendermint.proto.state.State.consensus_params', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\310\336\037\000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_height_consensus_params_changed', full_name='tendermint.proto.state.State.last_height_consensus_params_changed', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_results_hash', full_name='tendermint.proto.state.State.last_results_hash', index=11,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_hash', full_name='tendermint.proto.state.State.app_hash', index=12,
      number=13, type=12, cpp_type=9, label=1,
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
  serialized_start=787,
  serialized_end=1436,
)

_ABCIRESPONSES.fields_by_name['deliver_txs'].message_type = abci_dot_types_dot_types__pb2._RESPONSEDELIVERTX
_ABCIRESPONSES.fields_by_name['end_block'].message_type = abci_dot_types_dot_types__pb2._RESPONSEENDBLOCK
_ABCIRESPONSES.fields_by_name['begin_block'].message_type = abci_dot_types_dot_types__pb2._RESPONSEBEGINBLOCK
_VALIDATORSINFO.fields_by_name['validator_set'].message_type = proto_dot_types_dot_validator__pb2._VALIDATORSET
_CONSENSUSPARAMSINFO.fields_by_name['consensus_params'].message_type = proto_dot_types_dot_params__pb2._CONSENSUSPARAMS
_VERSION.fields_by_name['consensus'].message_type = proto_dot_version_dot_version__pb2._CONSENSUS
_STATE.fields_by_name['version'].message_type = _VERSION
_STATE.fields_by_name['last_block_id'].message_type = proto_dot_types_dot_types__pb2._BLOCKID
_STATE.fields_by_name['last_block_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STATE.fields_by_name['next_validators'].message_type = proto_dot_types_dot_validator__pb2._VALIDATORSET
_STATE.fields_by_name['validators'].message_type = proto_dot_types_dot_validator__pb2._VALIDATORSET
_STATE.fields_by_name['last_validators'].message_type = proto_dot_types_dot_validator__pb2._VALIDATORSET
_STATE.fields_by_name['consensus_params'].message_type = proto_dot_types_dot_params__pb2._CONSENSUSPARAMS
DESCRIPTOR.message_types_by_name['ABCIResponses'] = _ABCIRESPONSES
DESCRIPTOR.message_types_by_name['ValidatorsInfo'] = _VALIDATORSINFO
DESCRIPTOR.message_types_by_name['ConsensusParamsInfo'] = _CONSENSUSPARAMSINFO
DESCRIPTOR.message_types_by_name['Version'] = _VERSION
DESCRIPTOR.message_types_by_name['State'] = _STATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ABCIResponses = _reflection.GeneratedProtocolMessageType('ABCIResponses', (_message.Message,), dict(
  DESCRIPTOR = _ABCIRESPONSES,
  __module__ = 'proto.state.types_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.state.ABCIResponses)
  ))
_sym_db.RegisterMessage(ABCIResponses)

ValidatorsInfo = _reflection.GeneratedProtocolMessageType('ValidatorsInfo', (_message.Message,), dict(
  DESCRIPTOR = _VALIDATORSINFO,
  __module__ = 'proto.state.types_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.state.ValidatorsInfo)
  ))
_sym_db.RegisterMessage(ValidatorsInfo)

ConsensusParamsInfo = _reflection.GeneratedProtocolMessageType('ConsensusParamsInfo', (_message.Message,), dict(
  DESCRIPTOR = _CONSENSUSPARAMSINFO,
  __module__ = 'proto.state.types_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.state.ConsensusParamsInfo)
  ))
_sym_db.RegisterMessage(ConsensusParamsInfo)

Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), dict(
  DESCRIPTOR = _VERSION,
  __module__ = 'proto.state.types_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.state.Version)
  ))
_sym_db.RegisterMessage(Version)

State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), dict(
  DESCRIPTOR = _STATE,
  __module__ = 'proto.state.types_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.state.State)
  ))
_sym_db.RegisterMessage(State)


DESCRIPTOR._options = None
_CONSENSUSPARAMSINFO.fields_by_name['consensus_params']._options = None
_VERSION.fields_by_name['consensus']._options = None
_STATE.fields_by_name['version']._options = None
_STATE.fields_by_name['chain_id']._options = None
_STATE.fields_by_name['last_block_id']._options = None
_STATE.fields_by_name['last_block_time']._options = None
_STATE.fields_by_name['consensus_params']._options = None
# @@protoc_insertion_point(module_scope)
