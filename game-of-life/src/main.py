from game import GameOfLife

if __name__ == "__main__":

    game = GameOfLife(600, 50, 1)
    # game.board.load_file("../assets/board.txt")
    game.init_window()
    game.play_game()
    print(game.board)
