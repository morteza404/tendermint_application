# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/blockchain/msgs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tendermint.third_party.proto.gogoproto import gogo_pb2 as third__party_dot_proto_dot_gogoproto_dot_gogo__pb2
from tendermint.proto.types import block_pb2 as proto_dot_types_dot_block__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/blockchain/msgs.proto',
  package='tendermint.proto.blockchain',
  syntax='proto3',
  serialized_options=_b('Z1github.com/tendermint/tendermint/proto/blockchain'),
  serialized_pb=_b('\n\x1bproto/blockchain/msgs.proto\x12\x1btendermint.proto.blockchain\x1a&third_party/proto/gogoproto/gogo.proto\x1a\x17proto/types/block.proto\"\x1e\n\x0c\x42lockRequest\x12\x0e\n\x06height\x18\x01 \x01(\x03\"!\n\x0fNoBlockResponse\x12\x0e\n\x06height\x18\x01 \x01(\x03\"C\n\rBlockResponse\x12\x32\n\x05\x62lock\x18\x01 \x01(\x0b\x32\x1d.tendermint.proto.types.BlockB\x04\xc8\xde\x1f\x00\"-\n\rStatusRequest\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\x0c\n\x04\x62\x61se\x18\x02 \x01(\x03\".\n\x0eStatusResponse\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\x0c\n\x04\x62\x61se\x18\x02 \x01(\x03\"\xf3\x02\n\x07Message\x12\x42\n\rblock_request\x18\x01 \x01(\x0b\x32).tendermint.proto.blockchain.BlockRequestH\x00\x12I\n\x11no_block_response\x18\x02 \x01(\x0b\x32,.tendermint.proto.blockchain.NoBlockResponseH\x00\x12\x44\n\x0e\x62lock_response\x18\x03 \x01(\x0b\x32*.tendermint.proto.blockchain.BlockResponseH\x00\x12\x44\n\x0estatus_request\x18\x04 \x01(\x0b\x32*.tendermint.proto.blockchain.StatusRequestH\x00\x12\x46\n\x0fstatus_response\x18\x05 \x01(\x0b\x32+.tendermint.proto.blockchain.StatusResponseH\x00\x42\x05\n\x03sumB3Z1github.com/tendermint/tendermint/proto/blockchainb\x06proto3')
  ,
  dependencies=[third__party_dot_proto_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,proto_dot_types_dot_block__pb2.DESCRIPTOR,])




_BLOCKREQUEST = _descriptor.Descriptor(
  name='BlockRequest',
  full_name='tendermint.proto.blockchain.BlockRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='tendermint.proto.blockchain.BlockRequest.height', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=125,
  serialized_end=155,
)


_NOBLOCKRESPONSE = _descriptor.Descriptor(
  name='NoBlockResponse',
  full_name='tendermint.proto.blockchain.NoBlockResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='tendermint.proto.blockchain.NoBlockResponse.height', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=157,
  serialized_end=190,
)


_BLOCKRESPONSE = _descriptor.Descriptor(
  name='BlockResponse',
  full_name='tendermint.proto.blockchain.BlockResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block', full_name='tendermint.proto.blockchain.BlockResponse.block', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\310\336\037\000'), file=DESCRIPTOR),
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
  serialized_start=192,
  serialized_end=259,
)


_STATUSREQUEST = _descriptor.Descriptor(
  name='StatusRequest',
  full_name='tendermint.proto.blockchain.StatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='tendermint.proto.blockchain.StatusRequest.height', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base', full_name='tendermint.proto.blockchain.StatusRequest.base', index=1,
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
  serialized_start=261,
  serialized_end=306,
)


_STATUSRESPONSE = _descriptor.Descriptor(
  name='StatusResponse',
  full_name='tendermint.proto.blockchain.StatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='tendermint.proto.blockchain.StatusResponse.height', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base', full_name='tendermint.proto.blockchain.StatusResponse.base', index=1,
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
  serialized_start=308,
  serialized_end=354,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='tendermint.proto.blockchain.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_request', full_name='tendermint.proto.blockchain.Message.block_request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='no_block_response', full_name='tendermint.proto.blockchain.Message.no_block_response', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_response', full_name='tendermint.proto.blockchain.Message.block_response', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status_request', full_name='tendermint.proto.blockchain.Message.status_request', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status_response', full_name='tendermint.proto.blockchain.Message.status_response', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
      name='sum', full_name='tendermint.proto.blockchain.Message.sum',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=357,
  serialized_end=728,
)

_BLOCKRESPONSE.fields_by_name['block'].message_type = proto_dot_types_dot_block__pb2._BLOCK
_MESSAGE.fields_by_name['block_request'].message_type = _BLOCKREQUEST
_MESSAGE.fields_by_name['no_block_response'].message_type = _NOBLOCKRESPONSE
_MESSAGE.fields_by_name['block_response'].message_type = _BLOCKRESPONSE
_MESSAGE.fields_by_name['status_request'].message_type = _STATUSREQUEST
_MESSAGE.fields_by_name['status_response'].message_type = _STATUSRESPONSE
_MESSAGE.oneofs_by_name['sum'].fields.append(
  _MESSAGE.fields_by_name['block_request'])
_MESSAGE.fields_by_name['block_request'].containing_oneof = _MESSAGE.oneofs_by_name['sum']
_MESSAGE.oneofs_by_name['sum'].fields.append(
  _MESSAGE.fields_by_name['no_block_response'])
_MESSAGE.fields_by_name['no_block_response'].containing_oneof = _MESSAGE.oneofs_by_name['sum']
_MESSAGE.oneofs_by_name['sum'].fields.append(
  _MESSAGE.fields_by_name['block_response'])
_MESSAGE.fields_by_name['block_response'].containing_oneof = _MESSAGE.oneofs_by_name['sum']
_MESSAGE.oneofs_by_name['sum'].fields.append(
  _MESSAGE.fields_by_name['status_request'])
_MESSAGE.fields_by_name['status_request'].containing_oneof = _MESSAGE.oneofs_by_name['sum']
_MESSAGE.oneofs_by_name['sum'].fields.append(
  _MESSAGE.fields_by_name['status_response'])
_MESSAGE.fields_by_name['status_response'].containing_oneof = _MESSAGE.oneofs_by_name['sum']
DESCRIPTOR.message_types_by_name['BlockRequest'] = _BLOCKREQUEST
DESCRIPTOR.message_types_by_name['NoBlockResponse'] = _NOBLOCKRESPONSE
DESCRIPTOR.message_types_by_name['BlockResponse'] = _BLOCKRESPONSE
DESCRIPTOR.message_types_by_name['StatusRequest'] = _STATUSREQUEST
DESCRIPTOR.message_types_by_name['StatusResponse'] = _STATUSRESPONSE
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BlockRequest = _reflection.GeneratedProtocolMessageType('BlockRequest', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKREQUEST,
  __module__ = 'proto.blockchain.msgs_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.blockchain.BlockRequest)
  ))
_sym_db.RegisterMessage(BlockRequest)

NoBlockResponse = _reflection.GeneratedProtocolMessageType('NoBlockResponse', (_message.Message,), dict(
  DESCRIPTOR = _NOBLOCKRESPONSE,
  __module__ = 'proto.blockchain.msgs_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.blockchain.NoBlockResponse)
  ))
_sym_db.RegisterMessage(NoBlockResponse)

BlockResponse = _reflection.GeneratedProtocolMessageType('BlockResponse', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKRESPONSE,
  __module__ = 'proto.blockchain.msgs_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.blockchain.BlockResponse)
  ))
_sym_db.RegisterMessage(BlockResponse)

StatusRequest = _reflection.GeneratedProtocolMessageType('StatusRequest', (_message.Message,), dict(
  DESCRIPTOR = _STATUSREQUEST,
  __module__ = 'proto.blockchain.msgs_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.blockchain.StatusRequest)
  ))
_sym_db.RegisterMessage(StatusRequest)

StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), dict(
  DESCRIPTOR = _STATUSRESPONSE,
  __module__ = 'proto.blockchain.msgs_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.blockchain.StatusResponse)
  ))
_sym_db.RegisterMessage(StatusResponse)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'proto.blockchain.msgs_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.blockchain.Message)
  ))
_sym_db.RegisterMessage(Message)


DESCRIPTOR._options = None
_BLOCKRESPONSE.fields_by_name['block']._options = None
# @@protoc_insertion_point(module_scope)
