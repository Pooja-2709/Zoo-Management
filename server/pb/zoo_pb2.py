# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: zoo.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tzoo.proto\x12\x03zoo\"u\n\x03Zoo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04Name\x18\x02 \x01(\t\x12\x10\n\x08Location\x18\x03 \x01(\t\x12\x0f\n\x07\x41\x64\x64ress\x18\x04 \x01(\t\x12\x0f\n\x07Opening\x18\x05 \x01(\t\x12\x0f\n\x07\x43losing\x18\x06 \x01(\t\x12\x0f\n\x07\x43ontact\x18\x07 \x01(\t\"v\n\x10\x43reateZooRequest\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x10\n\x08Location\x18\x02 \x01(\t\x12\x0f\n\x07\x41\x64\x64ress\x18\x03 \x01(\t\x12\x0f\n\x07Opening\x18\x04 \x01(\t\x12\x0f\n\x07\x43losing\x18\x05 \x01(\t\x12\x0f\n\x07\x43ontact\x18\x06 \x01(\t\"*\n\x11\x43reateZooResponse\x12\x15\n\x03zoo\x18\x01 \x01(\x0b\x32\x08.zoo.Zoo\"\x82\x01\n\x10UpdateZooRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04Name\x18\x02 \x01(\t\x12\x10\n\x08Location\x18\x03 \x01(\t\x12\x0f\n\x07\x41\x64\x64ress\x18\x04 \x01(\t\x12\x0f\n\x07Opening\x18\x05 \x01(\t\x12\x0f\n\x07\x43losing\x18\x06 \x01(\t\x12\x0f\n\x07\x43ontact\x18\x07 \x01(\t\"*\n\x11UpdateZooResponse\x12\x15\n\x03zoo\x18\x01 \x01(\x0b\x32\x08.zoo.Zoo\"2\n\x11ReadAllZooRequest\x12\x0e\n\x06offset\x18\x01 \x01(\r\x12\r\n\x05limit\x18\x02 \x01(\r\"/\n\x12ReadAllZooResponse\x12\x19\n\x07records\x18\x01 \x03(\x0b\x32\x08.zoo.Zoo\"\x1e\n\x10\x44\x65leteZooRequest\x12\n\n\x02id\x18\x01 \x01(\t\"$\n\x11\x44\x65leteZooResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1b\n\rGetZooRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\'\n\x0eGetZooResponse\x12\x15\n\x03zoo\x18\x01 \x01(\x0b\x32\x08.zoo.Zoo2\xac\x02\n\nZooService\x12\x39\n\x06\x63reate\x12\x15.zoo.CreateZooRequest\x1a\x16.zoo.CreateZooResponse\"\x00\x12\x39\n\x06update\x12\x15.zoo.UpdateZooRequest\x1a\x16.zoo.UpdateZooResponse\"\x00\x12\x39\n\x06\x64\x65lete\x12\x15.zoo.DeleteZooRequest\x1a\x16.zoo.DeleteZooResponse\"\x00\x12\x30\n\x03get\x12\x12.zoo.GetZooRequest\x1a\x13.zoo.GetZooResponse\"\x00\x12;\n\x06search\x12\x16.zoo.ReadAllZooRequest\x1a\x17.zoo.ReadAllZooResponse\"\x00\x42\r\xaa\x02\nGrpcClientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'zoo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\nGrpcClient'
  _globals['_ZOO']._serialized_start=18
  _globals['_ZOO']._serialized_end=135
  _globals['_CREATEZOOREQUEST']._serialized_start=137
  _globals['_CREATEZOOREQUEST']._serialized_end=255
  _globals['_CREATEZOORESPONSE']._serialized_start=257
  _globals['_CREATEZOORESPONSE']._serialized_end=299
  _globals['_UPDATEZOOREQUEST']._serialized_start=302
  _globals['_UPDATEZOOREQUEST']._serialized_end=432
  _globals['_UPDATEZOORESPONSE']._serialized_start=434
  _globals['_UPDATEZOORESPONSE']._serialized_end=476
  _globals['_READALLZOOREQUEST']._serialized_start=478
  _globals['_READALLZOOREQUEST']._serialized_end=528
  _globals['_READALLZOORESPONSE']._serialized_start=530
  _globals['_READALLZOORESPONSE']._serialized_end=577
  _globals['_DELETEZOOREQUEST']._serialized_start=579
  _globals['_DELETEZOOREQUEST']._serialized_end=609
  _globals['_DELETEZOORESPONSE']._serialized_start=611
  _globals['_DELETEZOORESPONSE']._serialized_end=647
  _globals['_GETZOOREQUEST']._serialized_start=649
  _globals['_GETZOOREQUEST']._serialized_end=676
  _globals['_GETZOORESPONSE']._serialized_start=678
  _globals['_GETZOORESPONSE']._serialized_end=717
  _globals['_ZOOSERVICE']._serialized_start=720
  _globals['_ZOOSERVICE']._serialized_end=1020
# @@protoc_insertion_point(module_scope)