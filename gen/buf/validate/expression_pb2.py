# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: buf/validate/expression.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x62uf/validate/expression.proto\x12\x0c\x62uf.validate\"V\n\nConstraint\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\x1e\n\nexpression\x18\x03 \x01(\tR\nexpression\"E\n\nViolations\x12\x37\n\nviolations\x18\x01 \x03(\x0b\x32\x17.buf.validate.ViolationR\nviolations\"i\n\tViolation\x12\x1d\n\nfield_path\x18\x01 \x01(\tR\tfieldPath\x12#\n\rconstraint_id\x18\x02 \x01(\tR\x0c\x63onstraintId\x12\x18\n\x07message\x18\x03 \x01(\tR\x07messageB\xb7\x01\n\x10\x63om.buf.validateB\x0f\x45xpressionProtoP\x01ZAgithub.com/bufbuild/protovalidate/tools/internal/gen/buf/validate\xa2\x02\x03\x42VX\xaa\x02\x0c\x42uf.Validate\xca\x02\x0c\x42uf\\Validate\xe2\x02\x18\x42uf\\Validate\\GPBMetadata\xea\x02\rBuf::Validateb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.expression_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020com.buf.validateB\017ExpressionProtoP\001ZAgithub.com/bufbuild/protovalidate/tools/internal/gen/buf/validate\242\002\003BVX\252\002\014Buf.Validate\312\002\014Buf\\Validate\342\002\030Buf\\Validate\\GPBMetadata\352\002\rBuf::Validate'
  _CONSTRAINT._serialized_start=47
  _CONSTRAINT._serialized_end=133
  _VIOLATIONS._serialized_start=135
  _VIOLATIONS._serialized_end=204
  _VIOLATION._serialized_start=206
  _VIOLATION._serialized_end=311
# @@protoc_insertion_point(module_scope)
