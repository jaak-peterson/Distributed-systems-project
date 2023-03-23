# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tictactoe.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ftictactoe.proto\x12\x0btic_tac_toe\"\x07\n\x05\x45mpty\"!\n\x0eGeneralMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\":\n\rStartGameInfo\x12\x14\n\x0cstaring_node\x18\x01 \x01(\x05\x12\x13\n\x0bsecond_node\x18\x02 \x01(\x05\"U\n\x11GameStateResponse\x12\r\n\x05\x62oard\x18\x01 \x03(\t\x12\x0f\n\x07to_play\x18\x02 \x01(\x05\x12\x10\n\x08\x64\x61tetime\x18\x03 \x01(\t\x12\x0e\n\x06winner\x18\x04 \x01(\x05\"(\n\x0f\x45lectionMessage\x12\x15\n\rcandidate_ids\x18\x01 \x03(\x05\"4\n\x0e\x45lectionResult\x12\x11\n\tleader_id\x18\x01 \x01(\x05\x12\x0f\n\x07success\x18\x02 \x01(\x08\"\x1d\n\nPingResult\x12\x0f\n\x07success\x18\x01 \x01(\x08\">\n\x0bMoveMessage\x12\x0f\n\x07node_id\x18\x01 \x01(\x05\x12\x10\n\x08location\x18\x02 \x01(\x05\x12\x0c\n\x04\x63har\x18\x03 \x01(\t\"0\n\x0cMoveResponse\x12\r\n\x05state\x18\x01 \x01(\x08\x12\x11\n\terror_msg\x18\x02 \x01(\t2\xe7\x03\n\tTicTacToe\x12:\n\tping_node\x12\x12.tic_tac_toe.Empty\x1a\x17.tic_tac_toe.PingResult\"\x00\x12N\n\x0fhandle_election\x12\x1c.tic_tac_toe.ElectionMessage\x1a\x1b.tic_tac_toe.ElectionResult\"\x00\x12\x44\n\x0bhandle_move\x12\x18.tic_tac_toe.MoveMessage\x1a\x19.tic_tac_toe.MoveResponse\"\x00\x12\x46\n\x14handle_opponent_move\x12\x18.tic_tac_toe.MoveMessage\x1a\x12.tic_tac_toe.Empty\"\x00\x12G\n\x0f\x61sk_board_state\x12\x12.tic_tac_toe.Empty\x1a\x1e.tic_tac_toe.GameStateResponse\"\x00\x12\x34\n\x08\x65nd_game\x12\x12.tic_tac_toe.Empty\x1a\x12.tic_tac_toe.Empty\"\x00\x12\x41\n\x0csend_message\x12\x1b.tic_tac_toe.GeneralMessage\x1a\x12.tic_tac_toe.Empty\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tictactoe_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=32
  _EMPTY._serialized_end=39
  _GENERALMESSAGE._serialized_start=41
  _GENERALMESSAGE._serialized_end=74
  _STARTGAMEINFO._serialized_start=76
  _STARTGAMEINFO._serialized_end=134
  _GAMESTATERESPONSE._serialized_start=136
  _GAMESTATERESPONSE._serialized_end=221
  _ELECTIONMESSAGE._serialized_start=223
  _ELECTIONMESSAGE._serialized_end=263
  _ELECTIONRESULT._serialized_start=265
  _ELECTIONRESULT._serialized_end=317
  _PINGRESULT._serialized_start=319
  _PINGRESULT._serialized_end=348
  _MOVEMESSAGE._serialized_start=350
  _MOVEMESSAGE._serialized_end=412
  _MOVERESPONSE._serialized_start=414
  _MOVERESPONSE._serialized_end=462
  _TICTACTOE._serialized_start=465
  _TICTACTOE._serialized_end=952
# @@protoc_insertion_point(module_scope)
