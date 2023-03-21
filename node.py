from TicTacToe import TicTacToe
import grpc
from concurrent import futures
import time

import tictactoe_pb2
import tictactoe_pb2_grpc

LEADER_ID = 3

class Node(tictactoe_pb2_grpc.TicTacToeServicer):
    def __init__(self, node_id, server_address, nodes_ids, nodes_ports):
      self.node_id = node_id
      self.is_leader = False
      self.leader_id = None
      self.server_address = server_address
      self.nodes_ids = nodes_ids
      self.nodes_ports = nodes_ports
      self.game = None
    
    def runServer(self):
      self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
      tictactoe_pb2_grpc.add_TicTacToeServicer_to_server(self, self.server)
      self.server.add_insecure_port(f'[::]:{self.server_address}') 
      self.server.start()
      print(f"Server started listening on port {self.server_address}")
    
    def stopServer(self):
      self.server.stop(0)

    def handle_election(self, request, context):
        print(f"Received election message from process {request.sender_id}")
        if self.node_id == LEADER_ID:
            result = tictactoe_pb2.ElectionResult()
            result.leader_id = LEADER_ID
            result.success = True
            return result
        else:
            print(f"Forwarding election message from process {request.sender_id} to process {request.sender_id+1}")
            with grpc.insecure_channel(f'localhost:50053') as channel:
                stub = tictactoe_pb2_grpc.TicTacToeStub(channel)
                response = stub.handle_election(tictactoe_pb2.ElectionMessage(sender_id=request.sender_id+1))
                return response

    def startElection(self):
      print(f"I am process {self.node_id} and I am initiating the election")
      with grpc.insecure_channel(f'localhost:50052') as channel:
          stub = tictactoe_pb2_grpc.TicTacToeStub(channel)
          response = stub.handle_election(tictactoe_pb2.ElectionMessage(sender_id=1))
          if response.success:
              print(f"Node {self.node_id}: Election completed successfully. Coordinator ID is {response.leader_id}")
          else:
              print("Election failed")
          return response

    def initGame(self):
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
        response =  stub.handle_move(tictactoe_pb2.MoveMessage(node_id = self.node_id, move=move, state=None))
        state = response.state
        if state is False:
            print(f"Node {self.node_id}: Game continues, now is opponent's turn")
        elif state is True:
            print(f"Node {self.node_id}: You won!")
        elif state is None:
            print(f"Node {self.node_id}: Tie!")

 
def serve():
    node1 = Node(1, 50051, [2, 3], [50052,50053])
    node1.runServer()
    
    node2 = Node(2, 50052, [1, 3], [50051, 50053])
    node2.runServer()

    node3 = Node(3, 50053, [1, 2], [50051, 50052])
    node3.runServer()

    # TODO: Add some randomness to the election.
    time.sleep(3)
    node1.startElection()

    time.sleep(3)
    node3.initGame()

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
        node1.stopServer()


if __name__ == '__main__':
    serve()