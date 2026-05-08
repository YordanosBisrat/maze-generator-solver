import pygame

from maze import Maze
from renderer import draw

WIDTH = 900
HEIGHT = 850

TOP_UI_HEIGHT = 180

maze = Maze()


def main():

    global maze

    pygame.init()

    screen = pygame.display.set_mode(
        (WIDTH, HEIGHT)
    )

    pygame.display.set_caption(
        "DFS Maze Generator and Solver"
    )

    clock = pygame.time.Clock()

    running = True

    paused = False

    speed = 20

    while running:

        clock.tick(speed)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                # pause / resume

                if event.key == pygame.K_SPACE:
                    paused = not paused

                # reset maze

                if event.key == pygame.K_r:
                    maze = Maze()

                # increase speed

                if event.key == pygame.K_UP:
                    speed = min(100, speed + 5)

                # decrease speed

                if event.key == pygame.K_DOWN:
                    speed = max(5, speed - 5)

        # =========================
        # UPDATE
        # =========================

        if not paused:

            # generation phase

            if not maze.finished_generation:

                maze.step()

            # solving phase

            else:

                maze.solver_step()

        # =========================
        # DRAW
        # =========================

        draw(
            screen,
            maze,
            TOP_UI_HEIGHT,
            speed
        )

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()