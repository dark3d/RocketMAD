# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/use_item_move_reroll_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory.item import item_id_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__id__pb2
from pogoprotos.enums import pokemon_move_pb2 as pogoprotos_dot_enums_dot_pokemon__move__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/use_item_move_reroll_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\nJpogoprotos/networking/requests/messages/use_item_move_reroll_message.proto\x12\'pogoprotos.networking.requests.messages\x1a\'pogoprotos/inventory/item/item_id.proto\x1a#pogoprotos/enums/pokemon_move.proto\"\xba\x01\n\x18UseItemMoveRerollMessage\x12\x32\n\x07item_id\x18\x01 \x01(\x0e\x32!.pogoprotos.inventory.item.ItemId\x12\x12\n\npokemon_id\x18\x02 \x01(\x06\x12\x1c\n\x14reroll_unlocked_move\x18\x03 \x01(\x08\x12\x38\n\x11target_elite_move\x18\x04 \x01(\x0e\x32\x1d.pogoprotos.enums.PokemonMoveb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_item_dot_item__id__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__move__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_USEITEMMOVEREROLLMESSAGE = _descriptor.Descriptor(
  name='UseItemMoveRerollMessage',
  full_name='pogoprotos.networking.requests.messages.UseItemMoveRerollMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='pogoprotos.networking.requests.messages.UseItemMoveRerollMessage.item_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.networking.requests.messages.UseItemMoveRerollMessage.pokemon_id', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reroll_unlocked_move', full_name='pogoprotos.networking.requests.messages.UseItemMoveRerollMessage.reroll_unlocked_move', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_elite_move', full_name='pogoprotos.networking.requests.messages.UseItemMoveRerollMessage.target_elite_move', index=3,
      number=4, type=14, cpp_type=8, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=384,
)

_USEITEMMOVEREROLLMESSAGE.fields_by_name['item_id'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
_USEITEMMOVEREROLLMESSAGE.fields_by_name['target_elite_move'].enum_type = pogoprotos_dot_enums_dot_pokemon__move__pb2._POKEMONMOVE
DESCRIPTOR.message_types_by_name['UseItemMoveRerollMessage'] = _USEITEMMOVEREROLLMESSAGE

UseItemMoveRerollMessage = _reflection.GeneratedProtocolMessageType('UseItemMoveRerollMessage', (_message.Message,), dict(
  DESCRIPTOR = _USEITEMMOVEREROLLMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.use_item_move_reroll_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.UseItemMoveRerollMessage)
  ))
_sym_db.RegisterMessage(UseItemMoveRerollMessage)


# @@protoc_insertion_point(module_scope)
