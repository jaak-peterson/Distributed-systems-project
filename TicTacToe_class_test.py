from TicTacToe import TicTacToe


def run_game(moves_str):
    print("New game")
    game = TicTacToe()
    game.print_board()
    for move_str in moves_str:
        game.move(move_str)
        state = game.get_state()
        if state is False:
            print("Game continues")
        elif state is True:
            print(move_str.split(",")[1].strip().upper(), "won!")
            game.print_board()
            print("Board as a list:", game.get_board_list(), "\n")
            break
        elif state is None:
            print("Tie!")
            game.print_board()
            print("Board as a list:", game.get_board_list())
            break
        game.print_board()
        print()


# Test X wins
moves = ["0, x", "1, o", "4, x", "8, o", "3, x", "6, o", "5, x"]
run_game(moves)

# Test O wins
moves = ["0, x", "2, o", "3, x", "6, o", "5, x", "4, o"]
run_game(moves)

# Test tie
moves = ["0, x", "1, o", "3, x", "6, o", "5, x", "4, o", "7, x", "8, o", "2, x"]
run_game(moves)
