import random
from cell import Cell

ROWS = 20
COLS = 20
CELL_SIZE = 40


class Maze:
    def __init__(self):
        # grid
        self.grid = [[Cell() for _ in range(COLS)] for _ in range(ROWS)]

        # generator state (DFS maze builder)
        self.stack = []
        self.current = (0, 0)

        self.grid[0][0].visited = True
        self.stack.append((0, 0))
        
        # start & end (REQUIRED BY SPEC)
        self.start = (random.randint(0, ROWS - 1), 0)
        self.end = (random.randint(0, ROWS - 1), COLS - 1)

        # solver state
        self.solver_stack = [self.start]
        self.solver_visited = set()
        self.solver_visited.add(self.start)

        self.solution_path = []
        self.solved = False

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
    def solver_step(self):

        if self.solved:
            return

        r, c = self.solver_stack[-1]

        # reached goal
        if (r, c) == (ROWS - 1, COLS - 1):
            self.solution_path = list(self.solver_stack)
            self.solved = True
            return

        neighbors = []

        cell = self.grid[r][c]

        # UP
        if not cell.north and r > 0:
            neighbors.append((r - 1, c))

        # DOWN
        if not cell.south and r < ROWS - 1:
            neighbors.append((r + 1, c))

        # LEFT
        if not cell.west and c > 0:
            neighbors.append((r, c - 1))

        # RIGHT
        if not cell.east and c < COLS - 1:
            neighbors.append((r, c + 1))

        moved = False

        for nr, nc in neighbors:
            if (nr, nc) not in self.solver_visited:
                self.solver_stack.append((nr, nc))
                self.solver_visited.add((nr, nc))
                moved = True
                break

        if not moved and len(self.solver_stack) > 1:
            # dead end → backtrack
            self.solver_stack.pop()            