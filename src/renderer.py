import pygame

from maze import ROWS, COLS, CELL_SIZE

WHITE = (245, 245, 245)
BLACK = (20, 20, 20)

YELLOW = (255, 215, 0)
ORANGE = (255, 165, 0)
BLUE = (100, 149, 237)
RED = (220, 70, 70)
GREEN = (60, 180, 75)

DARK = (40, 44, 52)

BUTTON = (60, 70, 90)

SLIDER = (120, 120, 120)


def draw(screen, maze, top_offset, speed):

    screen.fill(WHITE)

    # =========================
    # TOP PANEL
    # =========================

    pygame.draw.rect(
        screen,
        DARK,
        (0, 0, 1000, top_offset)
    )

    title_font = pygame.font.SysFont(
        "Arial",
        28,
        bold=True
    )

    title = title_font.render(
        "DFS Maze Generator and Solver",
        True,
        WHITE
    )

    screen.blit(title, (30, 20))

    # =========================
    # BUTTONS
    # =========================

    pygame.draw.rect(
        screen,
        BUTTON,
        (40, 65, 190, 50),
        border_radius=12
    )

    pygame.draw.rect(
        screen,
        BUTTON,
        (260, 65, 220, 50),
        border_radius=12
    )

    button_font = pygame.font.SysFont(
        "Arial",
        22
    )

    txt1 = button_font.render(
        "R  NEW MAZE",
        True,
        WHITE
    )

    txt2 = button_font.render(
        "SPACE  PAUSE",
        True,
        WHITE
    )

    screen.blit(txt1, (65, 78))
    screen.blit(txt2, (285, 78))

    # =========================
    # SPEED UI
    # =========================

    speed_text = button_font.render(
        f"SPEED: {speed}",
        True,
        WHITE
    )

    screen.blit(speed_text, (560, 75))

    pygame.draw.rect(
        screen,
        SLIDER,
        (720, 85, 180, 5),
        border_radius=10
    )

    slider_x = 720 + (speed * 1.5)

    pygame.draw.circle(
        screen,
        WHITE,
        (int(slider_x), 87),
        10
    )

    # =========================
    # LEGEND
    # =========================

    legend_items = [
        ("Current Mouse", YELLOW),
        ("Explored Path", ORANGE),
        ("Dead End", BLUE),
        ("Solution Path", RED),
        ("Start / Goal", GREEN),
    ]

    lx = 50
    ly = 145

    small_font = pygame.font.SysFont(
        "Arial",
        17
    )

    for text, color in legend_items:

        pygame.draw.circle(
            screen,
            color,
            (lx, ly),
            8
        )

        label = small_font.render(
            text,
            True,
            WHITE
        )

        screen.blit(label, (lx + 15, ly - 8))

        lx += 180

    # =========================
    # DRAW CELLS
    # =========================

    for r in range(ROWS):
        for c in range(COLS):

            x = c * CELL_SIZE + 60
            y = r * CELL_SIZE + top_offset + 40

            rect = pygame.Rect(
                x,
                y,
                CELL_SIZE,
                CELL_SIZE
            )

            pygame.draw.rect(screen, WHITE, rect)

            # explored path

            if (r, c) in maze.solver_visited:
                pygame.draw.rect(screen, ORANGE, rect)

            # dead ends

            if (r, c) in maze.dead_ends:
                pygame.draw.rect(screen, BLUE, rect)

            # final solution

            if (r, c) in maze.solution_path:
                pygame.draw.rect(screen, RED, rect)

            # start / goal

            if (r, c) == maze.start:
                pygame.draw.rect(screen, GREEN, rect)

            if (r, c) == maze.end:
                pygame.draw.rect(screen, GREEN, rect)

            # current solver mouse

            if maze.solver_stack and not maze.solved:

                if (r, c) == maze.solver_stack[-1]:

                    pygame.draw.circle(
                        screen,
                        YELLOW,
                        (
                            x + CELL_SIZE // 2,
                            y + CELL_SIZE // 2
                        ),
                        CELL_SIZE // 4
                    )

    # =========================
    # DRAW WALLS
    # =========================

    for r in range(ROWS):
        for c in range(COLS):

            cell = maze.grid[r][c]

            x = c * CELL_SIZE + 60
            y = r * CELL_SIZE + top_offset + 40

            if cell.north:

                pygame.draw.line(
                    screen,
                    BLACK,
                    (x, y),
                    (x + CELL_SIZE, y),
                    2
                )

            if cell.south:

                pygame.draw.line(
                    screen,
                    BLACK,
                    (x, y + CELL_SIZE),
                    (x + CELL_SIZE, y + CELL_SIZE),
                    2
                )

            if cell.west:

                pygame.draw.line(
                    screen,
                    BLACK,
                    (x, y),
                    (x, y + CELL_SIZE),
                    2
                )

            if cell.east:

                pygame.draw.line(
                    screen,
                    BLACK,
                    (x + CELL_SIZE, y),
                    (x + CELL_SIZE, y + CELL_SIZE),
                    2
                )