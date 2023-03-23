# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import tictactoe_pb2 as tictactoe__pb2


class TicTacToeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ping_node = channel.unary_unary(
                '/tic_tac_toe.TicTacToe/ping_node',
                request_serializer=tictactoe__pb2.Empty.SerializeToString,
                response_deserializer=tictactoe__pb2.PingResult.FromString,
                )
        self.handle_election = channel.unary_unary(
                '/tic_tac_toe.TicTacToe/handle_election',
                request_serializer=tictactoe__pb2.ElectionMessage.SerializeToString,
                response_deserializer=tictactoe__pb2.ElectionResult.FromString,
                )
        self.handle_move = channel.unary_unary(
                '/tic_tac_toe.TicTacToe/handle_move',
                request_serializer=tictactoe__pb2.MoveMessage.SerializeToString,
                response_deserializer=tictactoe__pb2.MoveResponse.FromString,
                )
        self.ask_board_state = channel.unary_unary(
                '/tic_tac_toe.TicTacToe/ask_board_state',
                request_serializer=tictactoe__pb2.AskBoardStateMessage.SerializeToString,
                response_deserializer=tictactoe__pb2.GameStateResponse.FromString,
                )
        self.end_game = channel.unary_unary(
                '/tic_tac_toe.TicTacToe/end_game',
                request_serializer=tictactoe__pb2.Empty.SerializeToString,
                response_deserializer=tictactoe__pb2.Empty.FromString,
                )
        self.send_message = channel.unary_unary(
                '/tic_tac_toe.TicTacToe/send_message',
                request_serializer=tictactoe__pb2.GeneralMessage.SerializeToString,
                response_deserializer=tictactoe__pb2.Empty.FromString,
                )
        self.set_time = channel.unary_unary(
                '/tic_tac_toe.TicTacToe/set_time',
                request_serializer=tictactoe__pb2.SetTimeMessage.SerializeToString,
                response_deserializer=tictactoe__pb2.Empty.FromString,
                )
        self.request_timeout_enforcing = channel.unary_unary(
                '/tic_tac_toe.TicTacToe/request_timeout_enforcing',
                request_serializer=tictactoe__pb2.TimeoutRequestMessage.SerializeToString,
                response_deserializer=tictactoe__pb2.Empty.FromString,
                )
        self.kick_gamemaster = channel.unary_unary(
                '/tic_tac_toe.TicTacToe/kick_gamemaster',
                request_serializer=tictactoe__pb2.GameMasterKickRequest.SerializeToString,
                response_deserializer=tictactoe__pb2.GameMasterKickResponse.FromString,
                )


class TicTacToeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ping_node(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def handle_election(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def handle_move(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ask_board_state(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def end_game(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def send_message(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def set_time(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def request_timeout_enforcing(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def kick_gamemaster(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TicTacToeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ping_node': grpc.unary_unary_rpc_method_handler(
                    servicer.ping_node,
                    request_deserializer=tictactoe__pb2.Empty.FromString,
                    response_serializer=tictactoe__pb2.PingResult.SerializeToString,
            ),
            'handle_election': grpc.unary_unary_rpc_method_handler(
                    servicer.handle_election,
                    request_deserializer=tictactoe__pb2.ElectionMessage.FromString,
                    response_serializer=tictactoe__pb2.ElectionResult.SerializeToString,
            ),
            'handle_move': grpc.unary_unary_rpc_method_handler(
                    servicer.handle_move,
                    request_deserializer=tictactoe__pb2.MoveMessage.FromString,
                    response_serializer=tictactoe__pb2.MoveResponse.SerializeToString,
            ),
            'ask_board_state': grpc.unary_unary_rpc_method_handler(
                    servicer.ask_board_state,
                    request_deserializer=tictactoe__pb2.AskBoardStateMessage.FromString,
                    response_serializer=tictactoe__pb2.GameStateResponse.SerializeToString,
            ),
            'end_game': grpc.unary_unary_rpc_method_handler(
                    servicer.end_game,
                    request_deserializer=tictactoe__pb2.Empty.FromString,
                    response_serializer=tictactoe__pb2.Empty.SerializeToString,
            ),
            'send_message': grpc.unary_unary_rpc_method_handler(
                    servicer.send_message,
                    request_deserializer=tictactoe__pb2.GeneralMessage.FromString,
                    response_serializer=tictactoe__pb2.Empty.SerializeToString,
            ),
            'set_time': grpc.unary_unary_rpc_method_handler(
                    servicer.set_time,
                    request_deserializer=tictactoe__pb2.SetTimeMessage.FromString,
                    response_serializer=tictactoe__pb2.Empty.SerializeToString,
            ),
            'request_timeout_enforcing': grpc.unary_unary_rpc_method_handler(
                    servicer.request_timeout_enforcing,
                    request_deserializer=tictactoe__pb2.TimeoutRequestMessage.FromString,
                    response_serializer=tictactoe__pb2.Empty.SerializeToString,
            ),
            'kick_gamemaster': grpc.unary_unary_rpc_method_handler(
                    servicer.kick_gamemaster,
                    request_deserializer=tictactoe__pb2.GameMasterKickRequest.FromString,
                    response_serializer=tictactoe__pb2.GameMasterKickResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tic_tac_toe.TicTacToe', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TicTacToe(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ping_node(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tic_tac_toe.TicTacToe/ping_node',
            tictactoe__pb2.Empty.SerializeToString,
            tictactoe__pb2.PingResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def handle_election(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tic_tac_toe.TicTacToe/handle_election',
            tictactoe__pb2.ElectionMessage.SerializeToString,
            tictactoe__pb2.ElectionResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def handle_move(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tic_tac_toe.TicTacToe/handle_move',
            tictactoe__pb2.MoveMessage.SerializeToString,
            tictactoe__pb2.MoveResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ask_board_state(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tic_tac_toe.TicTacToe/ask_board_state',
            tictactoe__pb2.AskBoardStateMessage.SerializeToString,
            tictactoe__pb2.GameStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def end_game(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tic_tac_toe.TicTacToe/end_game',
            tictactoe__pb2.Empty.SerializeToString,
            tictactoe__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def send_message(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tic_tac_toe.TicTacToe/send_message',
            tictactoe__pb2.GeneralMessage.SerializeToString,
            tictactoe__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def set_time(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tic_tac_toe.TicTacToe/set_time',
            tictactoe__pb2.SetTimeMessage.SerializeToString,
            tictactoe__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def request_timeout_enforcing(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tic_tac_toe.TicTacToe/request_timeout_enforcing',
            tictactoe__pb2.TimeoutRequestMessage.SerializeToString,
            tictactoe__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def kick_gamemaster(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tic_tac_toe.TicTacToe/kick_gamemaster',
            tictactoe__pb2.GameMasterKickRequest.SerializeToString,
            tictactoe__pb2.GameMasterKickResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
