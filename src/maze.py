import random

from cell import Cell

ROWS = 20
COLS = 20

CELL_SIZE = 30


class Maze:

    def __init__(self):

        # =========================
        # GRID
        # =========================

        self.grid = [
            [Cell() for _ in range(COLS)]
            for _ in range(ROWS)
        ]

        # =========================
        # GENERATION VARIABLES
        # =========================

        self.stack = []

        self.current = (0, 0)

        self.grid[0][0].visited = True

        self.stack.append((0, 0))

        self.finished_generation = False

        # =========================
        # START / END
        # =========================

        self.start = (0, 0)

        self.end = (ROWS - 1, COLS - 1)

        # open maze entrance/exit

        self.grid[0][0].west = False

        self.grid[ROWS - 1][COLS - 1].east = False

        # =========================
        # SOLVER VARIABLES
        # =========================

        self.solver_stack = [self.start]

        self.solver_visited = set()

        self.solver_visited.add(self.start)

        self.solution_path = set()

        self.dead_ends = set()

        self.solved = False

    # =========================
    # UNVISITED NEIGHBORS
    # =========================

    def get_neighbors(self, r, c):

        neighbors = []

        # up
        if r > 0 and not self.grid[r - 1][c].visited:
            neighbors.append((r - 1, c))

        # down
        if r < ROWS - 1 and not self.grid[r + 1][c].visited:
            neighbors.append((r + 1, c))

        # left
        if c > 0 and not self.grid[r][c - 1].visited:
            neighbors.append((r, c - 1))

        # right
        if c < COLS - 1 and not self.grid[r][c + 1].visited:
            neighbors.append((r, c + 1))

        return neighbors

    # =========================
    # REMOVE WALLS
    # =========================

    def remove_walls(self, r1, c1, r2, c2):

        cell1 = self.grid[r1][c1]
        cell2 = self.grid[r2][c2]

        # vertical movement

        if r1 > r2:

            cell1.north = False
            cell2.south = False

        elif r1 < r2:

            cell1.south = False
            cell2.north = False

        # horizontal movement

        elif c1 > c2:

            cell1.west = False
            cell2.east = False

        elif c1 < c2:

            cell1.east = False
            cell2.west = False

    # =========================
    # GENERATE MAZE
    # =========================

    def step(self):

        if self.finished_generation:
            return

        r, c = self.current

        neighbors = self.get_neighbors(r, c)

        if neighbors:

            nr, nc = random.choice(neighbors)

            self.remove_walls(r, c, nr, nc)

            self.grid[nr][nc].visited = True

            self.stack.append((nr, nc))

            self.current = (nr, nc)

            # =========================
            # BONUS RANDOM CYCLES
            # =========================

            if random.randint(1, 20) == 1:

                directions = []

                if r > 0:
                    directions.append((r - 1, c))

                if r < ROWS - 1:
                    directions.append((r + 1, c))

                if c > 0:
                    directions.append((r, c - 1))

                if c < COLS - 1:
                    directions.append((r, c + 1))

                if directions:

                    rr, cc = random.choice(directions)

                    self.remove_walls(r, c, rr, cc)

        else:

            self.stack.pop()

            if self.stack:

                self.current = self.stack[-1]

            else:

                self.finished_generation = True

    # =========================
    # SOLVER STEP
    # =========================

    def solver_step(self):

        if not self.finished_generation:
            return

        if self.solved:
            return

        r, c = self.solver_stack[-1]

        # reached goal

        if (r, c) == self.end:

            self.solution_path = set(self.solver_stack)

            self.solved = True

            return

        cell = self.grid[r][c]

        neighbors = []

        # available movement directions

        if not cell.north and r > 0:
            neighbors.append((r - 1, c))

        if not cell.south and r < ROWS - 1:
            neighbors.append((r + 1, c))

        if not cell.west and c > 0:
            neighbors.append((r, c - 1))

        if not cell.east and c < COLS - 1:
            neighbors.append((r, c + 1))

        random.shuffle(neighbors)

        moved = False

        for nr, nc in neighbors:

            if (nr, nc) not in self.solver_visited:

                self.solver_stack.append((nr, nc))

                self.solver_visited.add((nr, nc))

                moved = True

                break

        # dead end

        if not moved:

            self.dead_ends.add((r, c))

            if len(self.solver_stack) > 1:

                self.solver_stack.pop()