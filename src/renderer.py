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