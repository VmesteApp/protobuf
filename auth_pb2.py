# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: auth.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'auth.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\x12\x04\x61uth\" \n\x0eGetVkIDRequest\x12\x0e\n\x06userID\x18\x01 \x01(\x03\"\x1f\n\x0fGetVkIDResponse\x12\x0c\n\x04vkID\x18\x01 \x01(\x03\x32G\n\x0b\x41uthService\x12\x38\n\x07GetVkID\x12\x14.auth.GetVkIDRequest\x1a\x15.auth.GetVkIDResponse\"\x00\x42\x1aZ\x18VmesteApp.auth.v1;authv1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\030VmesteApp.auth.v1;authv1'
  _globals['_GETVKIDREQUEST']._serialized_start=20
  _globals['_GETVKIDREQUEST']._serialized_end=52
  _globals['_GETVKIDRESPONSE']._serialized_start=54
  _globals['_GETVKIDRESPONSE']._serialized_end=85
  _globals['_AUTHSERVICE']._serialized_start=87
  _globals['_AUTHSERVICE']._serialized_end=158
# @@protoc_insertion_point(module_scope)
