# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grid.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='grid.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ngrid.proto\"c\n\x08Shop_Raw\x12\x0e\n\x06\x43olour\x18\x01 \x02(\t\x12\x10\n\x08\x44iscount\x18\x02 \x02(\x05\x12\x15\n\rRatings_count\x18\x03 \x02(\x05\x12\r\n\x05Price\x18\x04 \x02(\x05\x12\x0f\n\x07Ratings\x18\x05 \x02(\x02\"x\n\x0eShop_Processed\x12\x0e\n\x06\x43olour\x18\x01 \x02(\t\x12\x10\n\x08\x44iscount\x18\x02 \x02(\x05\x12\x15\n\rRatings_count\x18\x03 \x02(\x05\x12\r\n\x05Price\x18\x04 \x02(\x05\x12\x0f\n\x07Ratings\x18\x05 \x02(\x02\x12\r\n\x05Score\x18\x06 \x02(\x02\x32\x34\n\tPredictor\x12\'\n\x07Process\x12\t.Shop_Raw\x1a\x0f.Shop_Processed\"\x00'
)




_SHOP_RAW = _descriptor.Descriptor(
  name='Shop_Raw',
  full_name='Shop_Raw',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Colour', full_name='Shop_Raw.Colour', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Discount', full_name='Shop_Raw.Discount', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Ratings_count', full_name='Shop_Raw.Ratings_count', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Price', full_name='Shop_Raw.Price', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Ratings', full_name='Shop_Raw.Ratings', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=113,
)


_SHOP_PROCESSED = _descriptor.Descriptor(
  name='Shop_Processed',
  full_name='Shop_Processed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Colour', full_name='Shop_Processed.Colour', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Discount', full_name='Shop_Processed.Discount', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Ratings_count', full_name='Shop_Processed.Ratings_count', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Price', full_name='Shop_Processed.Price', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Ratings', full_name='Shop_Processed.Ratings', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Score', full_name='Shop_Processed.Score', index=5,
      number=6, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=235,
)

DESCRIPTOR.message_types_by_name['Shop_Raw'] = _SHOP_RAW
DESCRIPTOR.message_types_by_name['Shop_Processed'] = _SHOP_PROCESSED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Shop_Raw = _reflection.GeneratedProtocolMessageType('Shop_Raw', (_message.Message,), {
  'DESCRIPTOR' : _SHOP_RAW,
  '__module__' : 'grid_pb2'
  # @@protoc_insertion_point(class_scope:Shop_Raw)
  })
_sym_db.RegisterMessage(Shop_Raw)

Shop_Processed = _reflection.GeneratedProtocolMessageType('Shop_Processed', (_message.Message,), {
  'DESCRIPTOR' : _SHOP_PROCESSED,
  '__module__' : 'grid_pb2'
  # @@protoc_insertion_point(class_scope:Shop_Processed)
  })
_sym_db.RegisterMessage(Shop_Processed)



_PREDICTOR = _descriptor.ServiceDescriptor(
  name='Predictor',
  full_name='Predictor',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=237,
  serialized_end=289,
  methods=[
  _descriptor.MethodDescriptor(
    name='Process',
    full_name='Predictor.Process',
    index=0,
    containing_service=None,
    input_type=_SHOP_RAW,
    output_type=_SHOP_PROCESSED,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PREDICTOR)

DESCRIPTOR.services_by_name['Predictor'] = _PREDICTOR

# @@protoc_insertion_point(module_scope)
