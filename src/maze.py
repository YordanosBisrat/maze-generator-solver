import random
from cell import Cell

ROWS = 20
COLS = 20
CELL_SIZE = 40


class Maze:
    def __init__(self):
        self.grid = [[Cell() for _ in range(COLS)] for _ in range(ROWS)]

        self.stack = []
        self.current = (0, 0)

        self.grid[0][0].visited = True
        self.stack.append((0, 0))

    def get_neighbors(self, r, c):
        neighbors = []

        if r > 0 and not self.grid[r - 1][c].visited:
            neighbors.append((r - 1, c))

        if r < ROWS - 1 and not self.grid[r + 1][c].visited:
            neighbors.append((r + 1, c))

        if c > 0 and not self.grid[r][c - 1].visited:
            neighbors.append((r, c - 1))

        if c < COLS - 1 and not self.grid[r][c + 1].visited:
            neighbors.append((r, c + 1))

        return neighbors

    def remove_walls(self, r1, c1, r2, c2):

        cell1 = self.grid[r1][c1]
        cell2 = self.grid[r2][c2]

        if r1 > r2:
            cell1.north = False
            cell2.south = False
        elif r1 < r2:
            cell1.south = False
            cell2.north = False
        elif c1 > c2:
            cell1.west = False
            cell2.east = False
        elif c1 < c2:
            cell1.east = False
            cell2.west = False

    def step(self):

        r, c = self.current
        neighbors = self.get_neighbors(r, c)

        if neighbors:

            nr, nc = random.choice(neighbors)

            self.remove_walls(r, c, nr, nc)

            self.grid[nr][nc].visited = True

            self.stack.append((nr, nc))

            self.current = (nr, nc)

        else:

            # 🚨 SAFE BACKTRACK
            if len(self.stack) > 1:
                self.stack.pop()
                self.current = self.stack[-1]