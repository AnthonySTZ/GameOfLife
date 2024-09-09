import os


class Board:
    def __init__(self, size=0) -> None:
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]

    def load_file(self, filepath: str) -> None:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File {filepath} does not exist")

        with open(filepath, "r") as file:

            row_length = len(list(file[0].strip().split(",")))

            for i, line in enumerate(file):
                row = list(map(int, line.strip().split(",")))
                if len(row) != row_length:
                    raise ValueError(
                        f"Invalid row length at line {i+1}. Expected {row_length} values, got {len(row)}"
                    )

                self.board[i] = row
