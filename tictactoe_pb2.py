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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ftictactoe.proto\x12\x0btic_tac_toe\"\x07\n\x05\x45mpty\"(\n\x15GameMasterKickRequest\x12\x0f\n\x07node_id\x18\x01 \x01(\x05\")\n\x16GameMasterKickResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"(\n\x15TimeoutRequestMessage\x12\x0f\n\x07node_id\x18\x01 \x01(\x05\"\'\n\x14\x41skBoardStateMessage\x12\x0f\n\x07node_id\x18\x01 \x01(\x05\"3\n\x0eSetTimeMessage\x12\x0f\n\x07node_id\x18\x01 \x01(\x05\x12\x10\n\x08new_time\x18\x02 \x01(\t\"!\n\x0eGeneralMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\"U\n\x11GameStateResponse\x12\r\n\x05\x62oard\x18\x01 \x03(\t\x12\x0f\n\x07to_play\x18\x02 \x01(\x05\x12\x10\n\x08\x64\x61tetime\x18\x03 \x01(\t\x12\x0e\n\x06winner\x18\x04 \x01(\x05\"(\n\x0f\x45lectionMessage\x12\x15\n\rcandidate_ids\x18\x01 \x03(\x05\"4\n\x0e\x45lectionResult\x12\x11\n\tleader_id\x18\x01 \x01(\x05\x12\x0f\n\x07success\x18\x02 \x01(\x08\"\x1d\n\nPingResult\x12\x0f\n\x07success\x18\x01 \x01(\x08\">\n\x0bMoveMessage\x12\x0f\n\x07node_id\x18\x01 \x01(\x05\x12\x10\n\x08location\x18\x02 \x01(\x05\x12\x0c\n\x04\x63har\x18\x03 \x01(\t\"0\n\x0cMoveResponse\x12\r\n\x05state\x18\x01 \x01(\x08\x12\x11\n\terror_msg\x18\x02 \x01(\t2\xa2\x05\n\tTicTacToe\x12:\n\tping_node\x12\x12.tic_tac_toe.Empty\x1a\x17.tic_tac_toe.PingResult\"\x00\x12N\n\x0fhandle_election\x12\x1c.tic_tac_toe.ElectionMessage\x1a\x1b.tic_tac_toe.ElectionResult\"\x00\x12\x44\n\x0bhandle_move\x12\x18.tic_tac_toe.MoveMessage\x1a\x19.tic_tac_toe.MoveResponse\"\x00\x12V\n\x0f\x61sk_board_state\x12!.tic_tac_toe.AskBoardStateMessage\x1a\x1e.tic_tac_toe.GameStateResponse\"\x00\x12\x34\n\x08\x65nd_game\x12\x12.tic_tac_toe.Empty\x1a\x12.tic_tac_toe.Empty\"\x00\x12\x41\n\x0csend_message\x12\x1b.tic_tac_toe.GeneralMessage\x1a\x12.tic_tac_toe.Empty\"\x00\x12=\n\x08set_time\x12\x1b.tic_tac_toe.SetTimeMessage\x1a\x12.tic_tac_toe.Empty\"\x00\x12U\n\x19request_timeout_enforcing\x12\".tic_tac_toe.TimeoutRequestMessage\x1a\x12.tic_tac_toe.Empty\"\x00\x12\\\n\x0fkick_gamemaster\x12\".tic_tac_toe.GameMasterKickRequest\x1a#.tic_tac_toe.GameMasterKickResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tictactoe_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=32
  _EMPTY._serialized_end=39
  _GAMEMASTERKICKREQUEST._serialized_start=41
  _GAMEMASTERKICKREQUEST._serialized_end=81
  _GAMEMASTERKICKRESPONSE._serialized_start=83
  _GAMEMASTERKICKRESPONSE._serialized_end=124
  _TIMEOUTREQUESTMESSAGE._serialized_start=126
  _TIMEOUTREQUESTMESSAGE._serialized_end=166
  _ASKBOARDSTATEMESSAGE._serialized_start=168
  _ASKBOARDSTATEMESSAGE._serialized_end=207
  _SETTIMEMESSAGE._serialized_start=209
  _SETTIMEMESSAGE._serialized_end=260
  _GENERALMESSAGE._serialized_start=262
  _GENERALMESSAGE._serialized_end=295
  _GAMESTATERESPONSE._serialized_start=297
  _GAMESTATERESPONSE._serialized_end=382
  _ELECTIONMESSAGE._serialized_start=384
  _ELECTIONMESSAGE._serialized_end=424
  _ELECTIONRESULT._serialized_start=426
  _ELECTIONRESULT._serialized_end=478
  _PINGRESULT._serialized_start=480
  _PINGRESULT._serialized_end=509
  _MOVEMESSAGE._serialized_start=511
  _MOVEMESSAGE._serialized_end=573
  _MOVERESPONSE._serialized_start=575
  _MOVERESPONSE._serialized_end=623
  _TICTACTOE._serialized_start=626
  _TICTACTOE._serialized_end=1300
# @@protoc_insertion_point(module_scope)
