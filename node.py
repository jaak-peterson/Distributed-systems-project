import datetime
import random
from enum import Enum

from TicTacToe import TicTacToe
import grpc
from concurrent import futures
import time
import os
import argparse


import tictactoe_pb2
import tictactoe_pb2_grpc

network = "localhost"

port_map = {
    1: 50051,
    2: 50052,
    3: 50053,
}


class Symbol(Enum):
    X = "x",
    O = "o",


class Node(tictactoe_pb2_grpc.TicTacToeServicer):

    def __init__(self, node_id):
        self.node_id = node_id
        self.leader_id = None
        self.server = None
        self.time_diff = None
        self.game = None

    def run_server(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        tictactoe_pb2_grpc.add_TicTacToeServicer_to_server(self, self.server)
        self.server.add_insecure_port(f'[::]:{port_map[self.node_id]}')
        self.server.start()
        print(f"Server started listening on port {port_map[self.node_id]}")
        while True:
            try:
                user_input = input(f'Node-{self.node_id}>')
                if user_input == "":
                    continue
                ui_parts = user_input.split()
                if ui_parts[0] == "Check-connections":
                    connected_nodes = self.is_connected_with_other_nodes()
                    print(f"Node {self.node_id} is connected to nodes {connected_nodes}")

                elif ui_parts[0] == "Start-game":
                    if self.node_id != self.leader_id:
                        print("Only the game master can start the game")
                        continue
                    else:
                        self.init_game()
                elif ui_parts[0] =="Get-local-time":
                    print(self.get_time())
                elif ui_parts[0] == "Elect-leader":
                    if not all(self.is_connected_with_other_nodes()):
                        print("Connection to all nodes failed, please assure all nodes are in the same network.")
                    else:
                        self.start_election()
                elif ui_parts[0] == "List-board":
                    data = self.ask_for_board_info()
                    b = list(data.board)
                    b = list(map(lambda x: "empty" if x == "" else x, b))
                    os = b.count("O")
                    xs = b.count("X")
                    symbol = "X" if os == xs else "O"
                    is_my_turn = self.node_id == data.to_play
                    if is_my_turn:
                        print("It is your turn.")
                    else:
                        print("It is opponent's turn")
                    print(f'{symbol}: {data.datetime}, {str(b)}')
                elif ui_parts[0] == "Set-node-time":
                    if len(ui_parts) != 3:
                        print("Set-node-time requires two parameters: target node id and time(hh:mm:ss) ")
                    self.set_node_time(int(ui_parts[1]), ui_parts[2])
                elif ui_parts[0] == "Set-symbol":
                    if len(ui_parts) != 3:
                        print("Set-symbol requires two parameters loc(1-9) and symbol(X,O), separated by comma")
                    self.move(int(ui_parts[1].strip(", ")), ui_parts[2])
                else:
                    print("invalid input")
            except Exception as e:
                print(
                    f'You broke something. Go in your room and think about what you have done. Error-type {type(e)}{e}')

    def end_game(self, request, context):
        self.leader_id = None
        print("Game master has stepped down.")
        return tictactoe_pb2.Empty()

    def step_down(self):
        print("Initalizing stepping down")
        players = [self.game.o_player, self.game.x_player]
        for player in players:
            with grpc.insecure_channel(f'{network}:{port_map[player]}') as channel:
                stub = tictactoe_pb2_grpc.TicTacToeStub(channel)
                stub.end_game(tictactoe_pb2.Empty())
        self.game = None

    def ask_board_state(self, request, context):
        dt = datetime.datetime.utcnow()
        dt = dt.strftime("%H:%M:%S.%f")[:-3]
        board = self.game.get_board_list()
        winner = -1
        if self.game.get_state():
            winner = self.game.get_winner()
            winner = self.game.x_player if winner == "X" else self.game.o_player
        return tictactoe_pb2.GameStateResponse(datetime=dt, board=board, to_play=self.game.to_play(), winner=winner)

    def ask_for_board_info(self):
        if not self.leader_id:
            print("No leader selected.")
        with grpc.insecure_channel(f'{network}:{port_map[self.leader_id]}') as channel:
            stub = tictactoe_pb2_grpc.TicTacToeStub(channel)
            return stub.ask_board_state(tictactoe_pb2.Empty())

    def stop_server(self):
        self.server.stop(0)

    def ping_node(self, request, context):
        return tictactoe_pb2.PingResult(success=True)

    def handle_election(self, request, context):

        print(f"Received election message from process {request.candidate_ids[-1]}")
        if self.node_id == request.candidate_ids[0]:
            result = tictactoe_pb2.ElectionResult(leader_id=max(request.candidate_ids), success=True)
            return result
        else:
            target_id = self.node_id + 1
            if target_id > 3:
                target_id -= 3
            print(f"Forwarding election message from process {self.node_id} to process {target_id}")
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
        if target_id > 3:
            target_id -= 3
        with grpc.insecure_channel(f'{network}:{port_map[target_id]}') as channel:
            stub = tictactoe_pb2_grpc.TicTacToeStub(channel)
            response = stub.handle_election(tictactoe_pb2.ElectionMessage(candidate_ids=[self.node_id]))
            if response.success:
                print(f"Node {self.node_id}: Election completed successfully. Coordinator ID is {response.leader_id}")
                self.leader_id = response.leader_id

            else:
                print("Election failed")
            return response

    def init_game(self):
        print("Initializing the game as the leader")
        ids = list(port_map.keys())
        ids.sort()
        starting_player, second_player = (ids[0], ids[1]) if random.random() > 0.5 else (ids[1], ids[0])
        self.game = TicTacToe(board_size=3, x_player=starting_player, o_player=second_player)
        with grpc.insecure_channel(f'{network}:{port_map[starting_player]}') as channel:
            stub = tictactoe_pb2_grpc.TicTacToeStub(channel)
            stub.send_message(tictactoe_pb2.GeneralMessage(message="Gamemaster started the game. Your symbol: 'X'"))

        with grpc.insecure_channel(f'{network}:{port_map[second_player]}') as channel:
            stub = tictactoe_pb2_grpc.TicTacToeStub(channel)
            stub.send_message(tictactoe_pb2.GeneralMessage(message="Gamemaster started the game. Your symbol: 'O'"))

        return

    def send_message(self, request, context):
        print(request.message)
        return tictactoe_pb2.Empty()

    def handle_move(self, request, context):

        if self.game.get_board_list()[request.location - 1] in ["X", "O"]:
            return tictactoe_pb2.MoveResponse(error_msg=f"Location {request.location} already contains a number")
        if self.game.to_play() != request.node_id:
            return tictactoe_pb2.MoveResponse(error_msg="Wrong player is trying to make a turn")
        if request.char.lower() != self.game.get_next_char().lower():
            return tictactoe_pb2.MoveResponse(error_msg=f"Illegal symbol. {self.game.get_next_char()} was expected.")
        if request.location not in range(1, 10):
            return tictactoe_pb2.MoveResponse(error_msg=f"Invalid location.")

        self.game.move(f'{request.location - 1}, {request.char}')

        next_player = self.game.to_play()
        with grpc.insecure_channel(f'{network}:{port_map[next_player]}') as channel:
            stub = tictactoe_pb2_grpc.TicTacToeStub(channel)
            stub.send_message(tictactoe_pb2.GeneralMessage(
                message=f"Your opponent played {request.char} at {request.location}. It is your turn"))

        state = self.game.get_state()
        if state or state is None:
            self.handle_game_end()

        return tictactoe_pb2.MoveResponse(state=state)

    def is_connected_with_other_nodes(self):
        connected_nodes = []
        for target in port_map.keys():
            if self.node_id != target:
                if not self.check_ping(target):
                    print(f'Connection to node {target} failed')
                    # Necessary for case when elected leader disconnects.
                    if target == self.leader_id:
                        self.leader_id = None
                else:
                    connected_nodes.append(target)
        return connected_nodes

    def move(self, location, char):
        with grpc.insecure_channel(f'{network}:{port_map[self.leader_id]}') as channel:
            stub = tictactoe_pb2_grpc.TicTacToeStub(channel)
            response = stub.handle_move(tictactoe_pb2.MoveMessage(node_id=self.node_id, location=location, char=char))
            state = response.state
            if response.error_msg:
                print(response.error_msg)
                return
            if state is False:
                print(f"Node {self.node_id}: Game continues, now is opponent's turn")
            elif state is True:
                print(f"Node {self.node_id}: You won!")
            elif state is None:
                print(f"Node {self.node_id}: Tie!")

    def handle_game_end(self):
        result = self.game.get_state()
        next_player = self.game.to_play()
        with grpc.insecure_channel(f'{network}:{port_map[next_player]}') as channel:
            stub = tictactoe_pb2_grpc.TicTacToeStub(channel)
            stub.send_message(tictactoe_pb2.GeneralMessage(
                message="Game over! You lost" if result else "Game over! It's a tie"))
            self.step_down()
        return tictactoe_pb2.Empty()

    def check_ping(self, target_id):
        port = port_map[target_id]
        with grpc.insecure_channel(f'{network}:{port}') as channel:
            stub = tictactoe_pb2_grpc.TicTacToeStub(channel)
            try:
                response = stub.ping_node(tictactoe_pb2.Empty())
            except grpc.RpcError as rpc_error:
                return False
            return True

    def get_time(self):
        if self.time_diff:
            dt = datetime.datetime.utcnow() + self.time_diff
        else:
            dt = datetime.datetime.utcnow()

        return dt.time()

    def set_time(self, request, context):
        server_time = request.new_time
        dt_local = datetime.datetime.utcnow().time()
        dt_server = datetime.datetime.strptime(server_time, "%H:%M:%S").time()
        diff = datetime.datetime.combine(datetime.date.min, dt_server) - datetime.datetime.combine(datetime.date.min, dt_local)

        self.time_diff = diff
        print(f"New clock: {dt_server}")
        return tictactoe_pb2.Empty()

    def set_node_time(self, target, time):
        if target not in port_map.keys():
            print("Invalid target id")
            return
        if self.node_id not in [self.leader_id, target]:
            print(f"Only the game master ({self.leader_id}) can modify the clock of code {target}")
            return
        with grpc.insecure_channel(f'{network}:{port_map[target]}') as channel:
            stub = tictactoe_pb2_grpc.TicTacToeStub(channel)
            return stub.set_time(tictactoe_pb2.SetTimeMessage(new_time=time))

def serve(id):
    node = Node(id)
    node.run_server()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--node_id", type=int, default=1)
    args = parser.parse_args()
    serve(args.node_id)
