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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ftictactoe.proto\x12\x0btic_tac_toe\"\x07\n\x05\x45mpty\":\n\rStartGameInfo\x12\x14\n\x0cstaring_node\x18\x01 \x01(\x05\x12\x13\n\x0bsecond_node\x18\x02 \x01(\x05\"E\n\x11GameStateResponse\x12\r\n\x05\x62oard\x18\x01 \x03(\t\x12\x0f\n\x07to_play\x18\x02 \x01(\x05\x12\x10\n\x08\x64\x61tetime\x18\x03 \x01(\t\"(\n\x0f\x45lectionMessage\x12\x15\n\rcandidate_ids\x18\x01 \x03(\x05\"4\n\x0e\x45lectionResult\x12\x11\n\tleader_id\x18\x01 \x01(\x05\x12\x0f\n\x07success\x18\x02 \x01(\x08\"\x1d\n\nPingResult\x12\x0f\n\x07success\x18\x01 \x01(\x08\">\n\x0bMoveMessage\x12\x0f\n\x07node_id\x18\x01 \x01(\x05\x12\x10\n\x08location\x18\x02 \x01(\x05\x12\x0c\n\x04\x63har\x18\x03 \x01(\t\"5\n\x0cMoveResponse\x12\r\n\x05state\x18\x01 \x01(\x08\x12\x16\n\x0ewas_legal_move\x18\x02 \x01(\x08\x32\xee\x02\n\tTicTacToe\x12:\n\tping_node\x12\x12.tic_tac_toe.Empty\x1a\x17.tic_tac_toe.PingResult\"\x00\x12N\n\x0fhandle_election\x12\x1c.tic_tac_toe.ElectionMessage\x1a\x1b.tic_tac_toe.ElectionResult\"\x00\x12\x44\n\x0bhandle_move\x12\x18.tic_tac_toe.MoveMessage\x1a\x19.tic_tac_toe.MoveResponse\"\x00\x12\x46\n\x14handle_opponent_move\x12\x18.tic_tac_toe.MoveMessage\x1a\x12.tic_tac_toe.Empty\"\x00\x12G\n\x0f\x61sk_board_state\x12\x12.tic_tac_toe.Empty\x1a\x1e.tic_tac_toe.GameStateResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tictactoe_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=32
  _EMPTY._serialized_end=39
  _STARTGAMEINFO._serialized_start=41
  _STARTGAMEINFO._serialized_end=99
  _GAMESTATERESPONSE._serialized_start=101
  _GAMESTATERESPONSE._serialized_end=170
  _ELECTIONMESSAGE._serialized_start=172
  _ELECTIONMESSAGE._serialized_end=212
  _ELECTIONRESULT._serialized_start=214
  _ELECTIONRESULT._serialized_end=266
  _PINGRESULT._serialized_start=268
  _PINGRESULT._serialized_end=297
  _MOVEMESSAGE._serialized_start=299
  _MOVEMESSAGE._serialized_end=361
  _MOVERESPONSE._serialized_start=363
  _MOVERESPONSE._serialized_end=416
  _TICTACTOE._serialized_start=419
  _TICTACTOE._serialized_end=785
# @@protoc_insertion_point(module_scope)
