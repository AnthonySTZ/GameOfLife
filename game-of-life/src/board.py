import os


class Board:
    def __init__(self, size) -> None:
        self.board = [[0 for _ in range(size)] for _ in range(size)]

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
        return f"Board size : {len(self.board)} x {len(self.board[0]) if len(self.board) > 0 else 0}"

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
                count += self.board[nx][ny]
        return count

    def simulate_next_frame(self) -> None:
        new_board = [
            [0 for _ in range(len(self.board))] for _ in range(len(self.board))
        ]
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                cell = self.board[i][j]
                neighbors = self.count_live_neighbors(i, j)
                if neighbors <= 1 or neighbors >= 4:
                    new_board[i][j] = 0
                    continue
                if neighbors == 3:
                    new_board[i][j] = 1
                    continue
        self.board = new_board
