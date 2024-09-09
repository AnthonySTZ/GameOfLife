from board import Board

if __name__ == "__main__":

    board_game = Board()
    board_game.load_file("../assets/board.txt")
    print(board_game)
