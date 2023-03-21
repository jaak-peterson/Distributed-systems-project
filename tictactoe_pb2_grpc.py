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
        self.handle_opponent_move = channel.unary_unary(
                '/tic_tac_toe.TicTacToe/handle_opponent_move',
                request_serializer=tictactoe__pb2.MoveMessage.SerializeToString,
                response_deserializer=tictactoe__pb2.Empty.FromString,
                )


class TicTacToeServicer(object):
    """Missing associated documentation comment in .proto file."""

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

    def handle_opponent_move(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TicTacToeServicer_to_server(servicer, server):
    rpc_method_handlers = {
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
            'handle_opponent_move': grpc.unary_unary_rpc_method_handler(
                    servicer.handle_opponent_move,
                    request_deserializer=tictactoe__pb2.MoveMessage.FromString,
                    response_serializer=tictactoe__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tic_tac_toe.TicTacToe', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TicTacToe(object):
    """Missing associated documentation comment in .proto file."""

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
    def handle_opponent_move(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tic_tac_toe.TicTacToe/handle_opponent_move',
            tictactoe__pb2.MoveMessage.SerializeToString,
            tictactoe__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
