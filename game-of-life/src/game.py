from board import Board
import pygame as pg


class GameOfLife:
    def __init__(self, window_width=600, size=10, borderwidth=2) -> None:

        cell_size = int(window_width / size)
        self.board = Board(cell_size, size)
        self.borderwidth = borderwidth

    def init_window(self) -> None:
        pg.init()
        pg.display.set_caption("Conway's Game of Life")
        self.screen = pg.display.set_mode(self.board.size())

    def play_game(self) -> None:
        run = True
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.board.simulate_next_frame()
                        self.draw_board()
                    if event.key == pg.K_r:
                        self.board.randomize_board()
                        self.draw_board()

        pg.quit()

    def draw_board(self) -> None:
        self.screen.fill(pg.Color("grey"))
        for x in range(self.board.size()[0]):
            for y in range(self.board.size()[1]):
                self.draw_cell(x, y)
        pg.display.flip()

    def draw_cell(self, x, y) -> None:
        cell = self.board.get_cell(x, y)
        if cell == 1:
            pg.draw.rect(
                self.screen,
                pg.Color("yellow"),
                (
                    x * self.board.cell_size,
                    y * self.board.cell_size,
                    self.board.cell_size - self.borderwidth,
                    self.board.cell_size - self.borderwidth,
                ),
            )
