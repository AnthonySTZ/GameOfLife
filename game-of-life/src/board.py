import os


class Board:
    def __init__(self, size=0) -> None:
        self.size = size
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
