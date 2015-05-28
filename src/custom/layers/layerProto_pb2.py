# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: layerProto.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='layerProto.proto',
  package='LayerCalc',
  serialized_pb='\n\x10layerProto.proto\x12\tLayerCalc\"1\n\x05Param\x12(\n\nlayer_calc\x18\x01 \x03(\x0b\x32\x14.LayerCalc.LayerCalc\"Q\n\tLayerCalc\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x10\n\x08\x66ilename\x18\x02 \x02(\t\x12$\n\nbackground\x18\x03 \x01(\x0b\x32\x10.LayerCalc.Color\"3\n\x05\x43olor\x12\t\n\x01r\x18\x01 \x02(\x05\x12\t\n\x01g\x18\x02 \x02(\x05\x12\t\n\x01\x62\x18\x03 \x02(\x05\x12\t\n\x01\x61\x18\x04 \x02(\x05')




_PARAM = _descriptor.Descriptor(
  name='Param',
  full_name='LayerCalc.Param',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='layer_calc', full_name='LayerCalc.Param.layer_calc', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=31,
  serialized_end=80,
)


_LAYERCALC = _descriptor.Descriptor(
  name='LayerCalc',
  full_name='LayerCalc.LayerCalc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='LayerCalc.LayerCalc.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filename', full_name='LayerCalc.LayerCalc.filename', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='background', full_name='LayerCalc.LayerCalc.background', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=82,
  serialized_end=163,
)


_COLOR = _descriptor.Descriptor(
  name='Color',
  full_name='LayerCalc.Color',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='r', full_name='LayerCalc.Color.r', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='g', full_name='LayerCalc.Color.g', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='b', full_name='LayerCalc.Color.b', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='a', full_name='LayerCalc.Color.a', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=165,
  serialized_end=216,
)

_PARAM.fields_by_name['layer_calc'].message_type = _LAYERCALC
_LAYERCALC.fields_by_name['background'].message_type = _COLOR
DESCRIPTOR.message_types_by_name['Param'] = _PARAM
DESCRIPTOR.message_types_by_name['LayerCalc'] = _LAYERCALC
DESCRIPTOR.message_types_by_name['Color'] = _COLOR

class Param(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PARAM

  # @@protoc_insertion_point(class_scope:LayerCalc.Param)

class LayerCalc(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LAYERCALC

  # @@protoc_insertion_point(class_scope:LayerCalc.LayerCalc)

class Color(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COLOR

  # @@protoc_insertion_point(class_scope:LayerCalc.Color)


# @@protoc_insertion_point(module_scope)
