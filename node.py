from TicTacToe import TicTacToe
import grpc
from concurrent import futures
import time
import os

import tictactoe_pb2
import tictactoe_pb2_grpc

network="localhost"

port_map = {
    1: 50051,
    2: 50052,
    3: 50053,
}


class Node(tictactoe_pb2_grpc.TicTacToeServicer):
    def __init__(self, node_id, server_address):
        self.node_id = node_id
        self.is_leader = False
        self.leader_id = None
        self.server_address = server_address
        self.nodes_ids = list(port_map.keys()).remove(node_id)
        self.nodes_ports = list(port_map.values()).remove(server_address)
        self.game = None

    def run_server(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        tictactoe_pb2_grpc.add_TicTacToeServicer_to_server(self, self.server)
        self.server.add_insecure_port(f'[::]:{self.server_address}')
        self.server.start()
        print(f"Server started listening on port {self.server_address}")

    def stop_server(self):
        self.server.stop(0)

    def ping_node(self, request, context):
        return tictactoe_pb2.PingResult(success=True)

    def handle_election(self, request, context):

        print(f"Received election message from process {request.candidate_ids[-1]}")
        if self.node_id == request.candidate_ids[0]:
            result = tictactoe_pb2.ElectionResult(leader_id = max(request.candidate_ids))
            result.success = True
            return result
        else:
            target_id = self.node_id + 1
            if target_id > 3:
                target_id -= 3
            print(f"Forwarding election message from process {request.candidate_ids[-1]} to process {target_id}")
            with grpc.insecure_channel(f'{network}:{port_map[target_id]}') as channel:
                stub = tictactoe_pb2_grpc.TicTacToeStub(channel)
                new_c_ids = list(request.candidate_ids) + [self.node_id]
                response = stub.handle_election(tictactoe_pb2.ElectionMessage(candidate_ids=new_c_ids))
                if response.success:
                    print(f'Leader selected: {response.leader_id}')
                    self.leader_id = response.leader_id
                return response

    def start_election(self):
        print(f"I am process {self.node_id} and I am initiating the election")

        target_id = self.node_id + 1
        if target_id>3:
            target_id -= 3
        with grpc.insecure_channel(f'{network}:{port_map[target_id]}') as channel:
            stub = tictactoe_pb2_grpc.TicTacToeStub(channel)
            response = stub.handle_election(tictactoe_pb2.ElectionMessage(candidate_ids=[self.node_id]))
            if response.success:
                print(f"Node {self.node_id}: Election completed successfully. Coordinator ID is {response.leader_id}")
                self.leader_id=response.leader_id
            else:
                print("Election failed")
            return response

    def init_game(self):
        print("Init game")
        self.game = TicTacToe()

    def handle_move(self, request, context):
        node_id = request.node_id
        move_str = request.move
        self.game.move(move_str)
        state = self.game.get_state()
        if node_id == 1:
            with grpc.insecure_channel(f'localhost:50052') as channel:
                stub = tictactoe_pb2_grpc.TicTacToeStub(channel)
                response = stub.handle_opponent_move(tictactoe_pb2.MoveMessage(node_id=2, move=move_str, state=state))

        elif node_id == 2:
            with grpc.insecure_channel(f'localhost:50051') as channel:
                stub = tictactoe_pb2_grpc.TicTacToeStub(channel)
                response = stub.handle_opponent_move(tictactoe_pb2.MoveMessage(node_id=1, move=move_str, state=state))

        return tictactoe_pb2.MoveResponse(state=state)

    def is_connected_with_other_nodes(self):
        connected_to_all_nodes = True
        print("Checking connection with other nodes.")
        for target in port_map.keys():
            if id != target:
                if not check_ping(target):
                    connected_to_all_nodes = False
                    print(f'Connection to node{target} failed trying again in 10 seconds')
                    # Necessary for case when elected leader disconnects.
                    if (target == self.leader_id):
                        self.leader_id = None

        return connected_to_all_nodes


    def handle_opponent_move(self, request, context):
        state = request.state
        opponent_move = request.move
        if state is False:
            print(f"Node {self.node_id}: Your opponent's move was {opponent_move}, now is your turn")
        elif state is True:
            print(f"Node {self.node_id}: Sorry, you lost the game")
        elif state is None:
            print(f"Node {self.node_id}: Tie!")
        return tictactoe_pb2.Empty()

    def move(self, move):
        with grpc.insecure_channel(f'localhost:50053') as channel:
            stub = tictactoe_pb2_grpc.TicTacToeStub(channel)
            response = stub.handle_move(tictactoe_pb2.MoveMessage(node_id=self.node_id, move=move, state=None))
            state = response.state
            if state is False:
                print(f"Node {self.node_id}: Game continues, now is opponent's turn")
            elif state is True:
                print(f"Node {self.node_id}: You won!")
            elif state is None:
                print(f"Node {self.node_id}: Tie!")




def check_ping(target_id):
    port = port_map[target_id]
    with grpc.insecure_channel(f'{network}:{port}') as channel:
        stub = tictactoe_pb2_grpc.TicTacToeStub(channel)
        try:
            response = stub.ping_node(tictactoe_pb2.Empty())
        except grpc.RpcError as rpc_error:
            return False
        return True

def serve(id):
    node = Node(id, port_map[id])
    node.run_server()

    while True:
        if not node.is_connected_with_other_nodes():
            time.sleep(10)
            continue

        if not node.leader_id:
            success = node.start_election()
            if not success:
                time.sleep(10)
                continue

        if node.leader_id == id:
            if not node.game:
                node.init_game()
            time.sleep(5)
            continue
        else:




    """
    time.sleep(3)
    # Play game
    node1.move("0, x")

    time.sleep(1)
    node2.move("1, o")

    time.sleep(1)
    node1.move("4, x")

    time.sleep(1)
    node2.move("8, o")

    time.sleep(1)
    node1.move("3, x")

    time.sleep(1)
    node2.move("6, o")

    time.sleep(1)
    node1.move("5, x")

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        node1.stop_server()

    """
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--node_id", type=int, default=1)
    args = parser.parse_args()
    serve(args.node_id)
