import numpy as np


def check_win(axis):
    if '' in axis:
        return False
    elif len(set(axis)) == 1:
        return True


class TicTacToe:
    def __init__(self, board_size=3):
        self.board_size = board_size
        self.board = np.empty((board_size, board_size), dtype=str)

    def move(self, value):
        value = value.split(",")
        index, char = int(value[0]), value[1].strip().upper()
        board_1d = self.board.flatten()
        board_1d[index] = char
        self.board = board_1d.reshape(self.board_size, self.board_size)

    # Return 'True' if the game was won,
    # 'False' if the game continues,
    # 'None' if the game was tied
    def get_state(self):
        # Check rows
        for i in range(self.board_size):
            if check_win(self.board[i]):
                return True
        # Check columns
        transposed = self.board.T
        for i in range(self.board_size):
            if check_win(transposed[i]):
                return True
        # Check diagonals
        if check_win(np.array([self.board[i][i] for i in range(self.board_size)])):
            return True
        if check_win(np.array([self.board[i][self.board_size-1-i] for i in range(self.board_size)])):
            return True

        # Neither has won, check whether the game continues
        if '' in self.board:
            return False
        else:
            return None

    def get_board_list(self):
        return [None if val is None else val for row in self.board for val in row]

    def print_board(self):
        for row in self.board:
            print(["_" if val == '' else val for val in row])
