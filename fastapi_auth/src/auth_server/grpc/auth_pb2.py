# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\x12\x04\x61uth\"\"\n\x11\x43heckTokenRequest\x12\r\n\x05token\x18\x01 \x01(\t\"t\n\x12\x43heckTokenResponse\x12\x10\n\x08is_valid\x18\x01 \x01(\x08\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\r\n\x05roles\x18\x03 \x03(\t\x12\x15\n\ris_subscribed\x18\x04 \x01(\x08\x12\x15\n\rerror_message\x18\x05 \x01(\t2P\n\x0b\x41uthService\x12\x41\n\nCheckToken\x12\x17.auth.CheckTokenRequest\x1a\x18.auth.CheckTokenResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CHECKTOKENREQUEST']._serialized_start=20
  _globals['_CHECKTOKENREQUEST']._serialized_end=54
  _globals['_CHECKTOKENRESPONSE']._serialized_start=56
  _globals['_CHECKTOKENRESPONSE']._serialized_end=172
  _globals['_AUTHSERVICE']._serialized_start=174
  _globals['_AUTHSERVICE']._serialized_end=254
# @@protoc_insertion_point(module_scope)
