# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc/grpc/types.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from third_party.proto.gogoproto import gogo_pb2 as third__party_dot_proto_dot_gogoproto_dot_gogo__pb2
from abci.types import types_pb2 as abci_dot_types_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rpc/grpc/types.proto',
  package='tendermint.rpc.grpc',
  syntax='proto3',
  serialized_options=_b('Z2github.com/tendermint/tendermint/rpc/grpc;coregrpc\310\342\036\001\320\342\036\001\340\342\036\001\300\343\036\001\370\341\036\001\250\342\036\001\270\342\036\001'),
  serialized_pb=_b('\n\x14rpc/grpc/types.proto\x12\x13tendermint.rpc.grpc\x1a&third_party/proto/gogoproto/gogo.proto\x1a\x16\x61\x62\x63i/types/types.proto\"\r\n\x0bRequestPing\" \n\x12RequestBroadcastTx\x12\n\n\x02tx\x18\x01 \x01(\x0c\"\x0e\n\x0cResponsePing\"\x8d\x01\n\x13ResponseBroadcastTx\x12\x38\n\x08\x63heck_tx\x18\x01 \x01(\x0b\x32&.tendermint.abci.types.ResponseCheckTx\x12<\n\ndeliver_tx\x18\x02 \x01(\x0b\x32(.tendermint.abci.types.ResponseDeliverTx2\xbd\x01\n\x0c\x42roadcastAPI\x12K\n\x04Ping\x12 .tendermint.rpc.grpc.RequestPing\x1a!.tendermint.rpc.grpc.ResponsePing\x12`\n\x0b\x42roadcastTx\x12\'.tendermint.rpc.grpc.RequestBroadcastTx\x1a(.tendermint.rpc.grpc.ResponseBroadcastTxBPZ2github.com/tendermint/tendermint/rpc/grpc;coregrpc\xc8\xe2\x1e\x01\xd0\xe2\x1e\x01\xe0\xe2\x1e\x01\xc0\xe3\x1e\x01\xf8\xe1\x1e\x01\xa8\xe2\x1e\x01\xb8\xe2\x1e\x01\x62\x06proto3')
  ,
  dependencies=[third__party_dot_proto_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,abci_dot_types_dot_types__pb2.DESCRIPTOR,])




_REQUESTPING = _descriptor.Descriptor(
  name='RequestPing',
  full_name='tendermint.rpc.grpc.RequestPing',
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
  serialized_start=109,
  serialized_end=122,
)


_REQUESTBROADCASTTX = _descriptor.Descriptor(
  name='RequestBroadcastTx',
  full_name='tendermint.rpc.grpc.RequestBroadcastTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx', full_name='tendermint.rpc.grpc.RequestBroadcastTx.tx', index=0,
      number=1, type=12, cpp_type=9, label=1,
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
  serialized_start=124,
  serialized_end=156,
)


_RESPONSEPING = _descriptor.Descriptor(
  name='ResponsePing',
  full_name='tendermint.rpc.grpc.ResponsePing',
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
  serialized_start=158,
  serialized_end=172,
)


_RESPONSEBROADCASTTX = _descriptor.Descriptor(
  name='ResponseBroadcastTx',
  full_name='tendermint.rpc.grpc.ResponseBroadcastTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='check_tx', full_name='tendermint.rpc.grpc.ResponseBroadcastTx.check_tx', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deliver_tx', full_name='tendermint.rpc.grpc.ResponseBroadcastTx.deliver_tx', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=175,
  serialized_end=316,
)

_RESPONSEBROADCASTTX.fields_by_name['check_tx'].message_type = abci_dot_types_dot_types__pb2._RESPONSECHECKTX
_RESPONSEBROADCASTTX.fields_by_name['deliver_tx'].message_type = abci_dot_types_dot_types__pb2._RESPONSEDELIVERTX
DESCRIPTOR.message_types_by_name['RequestPing'] = _REQUESTPING
DESCRIPTOR.message_types_by_name['RequestBroadcastTx'] = _REQUESTBROADCASTTX
DESCRIPTOR.message_types_by_name['ResponsePing'] = _RESPONSEPING
DESCRIPTOR.message_types_by_name['ResponseBroadcastTx'] = _RESPONSEBROADCASTTX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestPing = _reflection.GeneratedProtocolMessageType('RequestPing', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTPING,
  __module__ = 'rpc.grpc.types_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.rpc.grpc.RequestPing)
  ))
_sym_db.RegisterMessage(RequestPing)

RequestBroadcastTx = _reflection.GeneratedProtocolMessageType('RequestBroadcastTx', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTBROADCASTTX,
  __module__ = 'rpc.grpc.types_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.rpc.grpc.RequestBroadcastTx)
  ))
_sym_db.RegisterMessage(RequestBroadcastTx)

ResponsePing = _reflection.GeneratedProtocolMessageType('ResponsePing', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEPING,
  __module__ = 'rpc.grpc.types_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.rpc.grpc.ResponsePing)
  ))
_sym_db.RegisterMessage(ResponsePing)

ResponseBroadcastTx = _reflection.GeneratedProtocolMessageType('ResponseBroadcastTx', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEBROADCASTTX,
  __module__ = 'rpc.grpc.types_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.rpc.grpc.ResponseBroadcastTx)
  ))
_sym_db.RegisterMessage(ResponseBroadcastTx)


DESCRIPTOR._options = None

_BROADCASTAPI = _descriptor.ServiceDescriptor(
  name='BroadcastAPI',
  full_name='tendermint.rpc.grpc.BroadcastAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=319,
  serialized_end=508,
  methods=[
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='tendermint.rpc.grpc.BroadcastAPI.Ping',
    index=0,
    containing_service=None,
    input_type=_REQUESTPING,
    output_type=_RESPONSEPING,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='BroadcastTx',
    full_name='tendermint.rpc.grpc.BroadcastAPI.BroadcastTx',
    index=1,
    containing_service=None,
    input_type=_REQUESTBROADCASTTX,
    output_type=_RESPONSEBROADCASTTX,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BROADCASTAPI)

DESCRIPTOR.services_by_name['BroadcastAPI'] = _BROADCASTAPI

# @@protoc_insertion_point(module_scope)
