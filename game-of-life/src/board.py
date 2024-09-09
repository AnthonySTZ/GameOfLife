import os
import random


class Board:
    def __init__(self, cell_size, size) -> None:
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.cell_size = cell_size

    def load_file(self, filepath: str) -> None:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File {filepath} does not exist")

        self.board = []

        with open(filepath, "r") as file:

            lines = file.read().splitlines()
            row_length = len(lines[0].strip().split(","))

            for i, line in enumerate(lines):
                row = list(map(int, line.strip().split(",")))
                if len(row) != row_length:
                    raise ValueError(
                        f"Invalid row length at line {i+1}. Expected {row_length} values, got {len(row)}"
                    )

                self.board.append(row)

    def __repr__(self) -> str:
        return f"Board size : {len(self.board[0]) if len(self.board) > 0 else 0} x {len(self.board)}"

    def count_live_neighbors(self, x, y) -> int:
        count = 0
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(self.board[0]) and 0 <= ny < len(self.board):
                count += self.board[ny][nx]
        return count

    def simulate_next_frame(self) -> None:
        new_board = [
            [0 for _ in range(len(self.board))] for _ in range(len(self.board))
        ]
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                neighbors = self.count_live_neighbors(x, y)
                if neighbors <= 1 or neighbors >= 4:
                    new_board[y][x] = 0
                    continue
                if neighbors == 3:
                    new_board[y][x] = 1
                    continue
                new_board[y][x] = self.board[y][x]  # No change
        self.board = new_board

    def size(self) -> int:
        return (
            len(self.board) * self.cell_size,
            len(self.board[0]) * self.cell_size if len(self.board) > 0 else 0,
        )

    def get_cell(self, x, y) -> int:
        if 0 <= x < len(self.board[0]) and 0 <= y < len(self.board):
            return self.board[y][x]
        return -1

    def randomize_board(self) -> None:
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.board[i][j] = random.randint(0, 1)
