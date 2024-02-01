#!/usr/bin/python3
"""Does Queen Stuff"""
from sys import argv, exit


class Cell:
    """A Cell/Node on the chase board"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rejected = False
        self.accepted = False
        self.next = None
        self.prev = None

    def __str__(self):
        return f"[{self.x}, {self.y}]"


class Board:
    """Board"""
    def __init__(self, size):
        self.size = size
        self.cells = []
        self.accepted_ = []
        self.rejected = []
        self.partial = []

        self.current_row = 0

        self.populate()

    def populate(self):
        for row in range(self.size):
            row_data = []
            for col in range(self.size):
                row_data.append(Cell(row, col))
            self.cells.append(row_data)

    def check(self, cell):
        self.partial.append(cell)
        for ele in self.cells[cell.x]:
            if ele is not cell:
                self.rejected.append(ele)

        cells_on_same_col = zip(*self.cells)
        for ele in cells_on_same_col:
            if ele is not cell:
                self.rejected.append(ele)

        for i in range(self.size):
            for j in range(self.size):
                if i + j == cell.x + cell.y:
                    ele = self.cells[i][j]
                    if ele is not cell:
                        self.rejected.append(ele)

    def __str__(self):
        for i in self.cells:
            [print(j, end="") for j in i]
            print()
        return ""


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        if (N i:= int(argv[1])) < 4:
            print("N must be atleast 4")
            exit(1)
    except ValueError:
        print("N must be a number")
        exit(1)

    b = Board(N)
    print(b)
