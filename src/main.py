import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


WIDTH = 800
HEIGHT = 800


def initialize():

    glClearColor(0.0, 0.0, 0.0, 1.0)

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    gluOrtho2D(0, WIDTH, HEIGHT, 0)


def main():

    pygame.init()

    pygame.display.set_mode(
        (WIDTH, HEIGHT),
        DOUBLEBUF | OPENGL
    )

    pygame.display.set_caption(
        "Maze Generator and Solver"
    )

    initialize()

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()