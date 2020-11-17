# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/privval/msgs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tendermint.third_party.proto.gogoproto import gogo_pb2 as third__party_dot_proto_dot_gogoproto_dot_gogo__pb2
from tendermint.proto.crypto.keys import types_pb2 as proto_dot_crypto_dot_keys_dot_types__pb2
from tendermint.proto.types import types_pb2 as proto_dot_types_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/privval/msgs.proto',
  package='tendermint.proto.privval',
  syntax='proto3',
  serialized_options=_b('Z.github.com/tendermint/tendermint/proto/privval'),
  serialized_pb=_b('\n\x18proto/privval/msgs.proto\x12\x18tendermint.proto.privval\x1a&third_party/proto/gogoproto/gogo.proto\x1a\x1dproto/crypto/keys/types.proto\x1a\x17proto/types/types.proto\"6\n\x11RemoteSignerError\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"\x0f\n\rPubKeyRequest\"\x8c\x01\n\x0ePubKeyResponse\x12>\n\x07pub_key\x18\x01 \x01(\x0b\x32\'.tendermint.proto.crypto.keys.PublicKeyB\x04\xc8\xde\x1f\x00\x12:\n\x05\x65rror\x18\x02 \x01(\x0b\x32+.tendermint.proto.privval.RemoteSignerError\"C\n\x0fSignVoteRequest\x12\x30\n\x04vote\x18\x01 \x01(\x0b\x32\x1c.tendermint.proto.types.VoteB\x04\xc8\xde\x1f\x00\"\x80\x01\n\x10SignVoteResponse\x12\x30\n\x04vote\x18\x01 \x01(\x0b\x32\x1c.tendermint.proto.types.VoteB\x04\xc8\xde\x1f\x00\x12:\n\x05\x65rror\x18\x02 \x01(\x0b\x32+.tendermint.proto.privval.RemoteSignerError\"O\n\x13SignProposalRequest\x12\x38\n\x08proposal\x18\x01 \x01(\x0b\x32 .tendermint.proto.types.ProposalB\x04\xc8\xde\x1f\x00\"\x8e\x01\n\x16SignedProposalResponse\x12\x38\n\x08proposal\x18\x01 \x01(\x0b\x32 .tendermint.proto.types.ProposalB\x04\xc8\xde\x1f\x00\x12:\n\x05\x65rror\x18\x02 \x01(\x0b\x32+.tendermint.proto.privval.RemoteSignerError\"\r\n\x0bPingRequest\"\x0e\n\x0cPingResponseB0Z.github.com/tendermint/tendermint/proto/privvalb\x06proto3')
  ,
  dependencies=[third__party_dot_proto_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,proto_dot_crypto_dot_keys_dot_types__pb2.DESCRIPTOR,proto_dot_types_dot_types__pb2.DESCRIPTOR,])




_REMOTESIGNERERROR = _descriptor.Descriptor(
  name='RemoteSignerError',
  full_name='tendermint.proto.privval.RemoteSignerError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='tendermint.proto.privval.RemoteSignerError.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='tendermint.proto.privval.RemoteSignerError.description', index=1,
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
  serialized_start=150,
  serialized_end=204,
)


_PUBKEYREQUEST = _descriptor.Descriptor(
  name='PubKeyRequest',
  full_name='tendermint.proto.privval.PubKeyRequest',
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
  serialized_start=206,
  serialized_end=221,
)


_PUBKEYRESPONSE = _descriptor.Descriptor(
  name='PubKeyResponse',
  full_name='tendermint.proto.privval.PubKeyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pub_key', full_name='tendermint.proto.privval.PubKeyResponse.pub_key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\310\336\037\000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='tendermint.proto.privval.PubKeyResponse.error', index=1,
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
  serialized_start=224,
  serialized_end=364,
)


_SIGNVOTEREQUEST = _descriptor.Descriptor(
  name='SignVoteRequest',
  full_name='tendermint.proto.privval.SignVoteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vote', full_name='tendermint.proto.privval.SignVoteRequest.vote', index=0,
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
  serialized_start=366,
  serialized_end=433,
)


_SIGNVOTERESPONSE = _descriptor.Descriptor(
  name='SignVoteResponse',
  full_name='tendermint.proto.privval.SignVoteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vote', full_name='tendermint.proto.privval.SignVoteResponse.vote', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\310\336\037\000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='tendermint.proto.privval.SignVoteResponse.error', index=1,
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
  serialized_start=436,
  serialized_end=564,
)


_SIGNPROPOSALREQUEST = _descriptor.Descriptor(
  name='SignProposalRequest',
  full_name='tendermint.proto.privval.SignProposalRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal', full_name='tendermint.proto.privval.SignProposalRequest.proposal', index=0,
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
  serialized_start=566,
  serialized_end=645,
)


_SIGNEDPROPOSALRESPONSE = _descriptor.Descriptor(
  name='SignedProposalResponse',
  full_name='tendermint.proto.privval.SignedProposalResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal', full_name='tendermint.proto.privval.SignedProposalResponse.proposal', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\310\336\037\000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='tendermint.proto.privval.SignedProposalResponse.error', index=1,
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
  serialized_start=648,
  serialized_end=790,
)


_PINGREQUEST = _descriptor.Descriptor(
  name='PingRequest',
  full_name='tendermint.proto.privval.PingRequest',
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
  serialized_start=792,
  serialized_end=805,
)


_PINGRESPONSE = _descriptor.Descriptor(
  name='PingResponse',
  full_name='tendermint.proto.privval.PingResponse',
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
  serialized_start=807,
  serialized_end=821,
)

_PUBKEYRESPONSE.fields_by_name['pub_key'].message_type = proto_dot_crypto_dot_keys_dot_types__pb2._PUBLICKEY
_PUBKEYRESPONSE.fields_by_name['error'].message_type = _REMOTESIGNERERROR
_SIGNVOTEREQUEST.fields_by_name['vote'].message_type = proto_dot_types_dot_types__pb2._VOTE
_SIGNVOTERESPONSE.fields_by_name['vote'].message_type = proto_dot_types_dot_types__pb2._VOTE
_SIGNVOTERESPONSE.fields_by_name['error'].message_type = _REMOTESIGNERERROR
_SIGNPROPOSALREQUEST.fields_by_name['proposal'].message_type = proto_dot_types_dot_types__pb2._PROPOSAL
_SIGNEDPROPOSALRESPONSE.fields_by_name['proposal'].message_type = proto_dot_types_dot_types__pb2._PROPOSAL
_SIGNEDPROPOSALRESPONSE.fields_by_name['error'].message_type = _REMOTESIGNERERROR
DESCRIPTOR.message_types_by_name['RemoteSignerError'] = _REMOTESIGNERERROR
DESCRIPTOR.message_types_by_name['PubKeyRequest'] = _PUBKEYREQUEST
DESCRIPTOR.message_types_by_name['PubKeyResponse'] = _PUBKEYRESPONSE
DESCRIPTOR.message_types_by_name['SignVoteRequest'] = _SIGNVOTEREQUEST
DESCRIPTOR.message_types_by_name['SignVoteResponse'] = _SIGNVOTERESPONSE
DESCRIPTOR.message_types_by_name['SignProposalRequest'] = _SIGNPROPOSALREQUEST
DESCRIPTOR.message_types_by_name['SignedProposalResponse'] = _SIGNEDPROPOSALRESPONSE
DESCRIPTOR.message_types_by_name['PingRequest'] = _PINGREQUEST
DESCRIPTOR.message_types_by_name['PingResponse'] = _PINGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RemoteSignerError = _reflection.GeneratedProtocolMessageType('RemoteSignerError', (_message.Message,), dict(
  DESCRIPTOR = _REMOTESIGNERERROR,
  __module__ = 'proto.privval.msgs_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.privval.RemoteSignerError)
  ))
_sym_db.RegisterMessage(RemoteSignerError)

PubKeyRequest = _reflection.GeneratedProtocolMessageType('PubKeyRequest', (_message.Message,), dict(
  DESCRIPTOR = _PUBKEYREQUEST,
  __module__ = 'proto.privval.msgs_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.privval.PubKeyRequest)
  ))
_sym_db.RegisterMessage(PubKeyRequest)

PubKeyResponse = _reflection.GeneratedProtocolMessageType('PubKeyResponse', (_message.Message,), dict(
  DESCRIPTOR = _PUBKEYRESPONSE,
  __module__ = 'proto.privval.msgs_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.privval.PubKeyResponse)
  ))
_sym_db.RegisterMessage(PubKeyResponse)

SignVoteRequest = _reflection.GeneratedProtocolMessageType('SignVoteRequest', (_message.Message,), dict(
  DESCRIPTOR = _SIGNVOTEREQUEST,
  __module__ = 'proto.privval.msgs_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.privval.SignVoteRequest)
  ))
_sym_db.RegisterMessage(SignVoteRequest)

SignVoteResponse = _reflection.GeneratedProtocolMessageType('SignVoteResponse', (_message.Message,), dict(
  DESCRIPTOR = _SIGNVOTERESPONSE,
  __module__ = 'proto.privval.msgs_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.privval.SignVoteResponse)
  ))
_sym_db.RegisterMessage(SignVoteResponse)

SignProposalRequest = _reflection.GeneratedProtocolMessageType('SignProposalRequest', (_message.Message,), dict(
  DESCRIPTOR = _SIGNPROPOSALREQUEST,
  __module__ = 'proto.privval.msgs_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.privval.SignProposalRequest)
  ))
_sym_db.RegisterMessage(SignProposalRequest)

SignedProposalResponse = _reflection.GeneratedProtocolMessageType('SignedProposalResponse', (_message.Message,), dict(
  DESCRIPTOR = _SIGNEDPROPOSALRESPONSE,
  __module__ = 'proto.privval.msgs_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.privval.SignedProposalResponse)
  ))
_sym_db.RegisterMessage(SignedProposalResponse)

PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), dict(
  DESCRIPTOR = _PINGREQUEST,
  __module__ = 'proto.privval.msgs_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.privval.PingRequest)
  ))
_sym_db.RegisterMessage(PingRequest)

PingResponse = _reflection.GeneratedProtocolMessageType('PingResponse', (_message.Message,), dict(
  DESCRIPTOR = _PINGRESPONSE,
  __module__ = 'proto.privval.msgs_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.proto.privval.PingResponse)
  ))
_sym_db.RegisterMessage(PingResponse)


DESCRIPTOR._options = None
_PUBKEYRESPONSE.fields_by_name['pub_key']._options = None
_SIGNVOTEREQUEST.fields_by_name['vote']._options = None
_SIGNVOTERESPONSE.fields_by_name['vote']._options = None
_SIGNPROPOSALREQUEST.fields_by_name['proposal']._options = None
_SIGNEDPROPOSALRESPONSE.fields_by_name['proposal']._options = None
# @@protoc_insertion_point(module_scope)
