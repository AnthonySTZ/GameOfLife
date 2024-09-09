from board import Board
import pygame as pg


class GameOfLife:
    def __init__(self, size=10) -> None:

        self.board = Board(size)

    def init_window(self) -> None:
        pg.init()
        pg.display.set_caption("Conway's Game of Life")
        self.screen = pg.display.set_mode(self.board.size)

    def play_game(self) -> None:
        for event in pg.get_events():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
