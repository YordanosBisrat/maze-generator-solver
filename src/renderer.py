from OpenGL.GL import *

from maze import CELL_SIZE, ROWS, COLS


def draw_grid(maze):

    glColor3f(1, 1, 1)

    glBegin(GL_LINES)

    for r in range(ROWS):
        for c in range(COLS):

            cell = maze.grid[r][c]

            x = c * CELL_SIZE
            y = r * CELL_SIZE

            # top
            if cell.north:
                glVertex2f(x, y)
                glVertex2f(x + CELL_SIZE, y)

            # left
            if cell.west:
                glVertex2f(x, y)
                glVertex2f(x, y + CELL_SIZE)

    glEnd()

    # =========================
    # 2. BLUE DEAD ENDS
    # =========================

    glColor3f(0, 0, 1)

    glBegin(GL_QUADS)

    for r in range(ROWS):
        for c in range(COLS):

            if (r, c) in maze.solver_visited and (r, c) not in maze.solver_stack:

                x = c * CELL_SIZE
                y = r * CELL_SIZE

                glVertex2f(x, y)
                glVertex2f(x + CELL_SIZE, y)
                glVertex2f(x + CELL_SIZE, y + CELL_SIZE)
                glVertex2f(x, y + CELL_SIZE)

    glEnd()

    # =========================
    # 3. FINAL PATH (YELLOW)
    # =========================

    if maze.solved:

        glColor3f(1, 1, 0)

        glBegin(GL_QUADS)

        for r, c in maze.solution_path:

            x = c * CELL_SIZE
            y = r * CELL_SIZE

            glVertex2f(x, y)
            glVertex2f(x + CELL_SIZE, y)
            glVertex2f(x + CELL_SIZE, y + CELL_SIZE)
            glVertex2f(x, y + CELL_SIZE)

        glEnd()

    # =========================
    # 4. RED CURRENT POSITION
    # =========================

    r, c = maze.solver_stack[-1]

    x = c * CELL_SIZE
    y = r * CELL_SIZE

    glColor3f(1, 0, 0)

    glBegin(GL_QUADS)

    glVertex2f(x + 10, y + 10)
    glVertex2f(x + 30, y + 10)
    glVertex2f(x + 30, y + 30)
    glVertex2f(x + 10, y + 30)

    glEnd()