import pygame
from pygame.locals import *

from life import GameOfLife
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.speed = speed
        self.cell_size = cell_size
        self.screen = pygame.display.set_mode(
            (self.life.cols * self.cell_size, self.life.rows * self.cell_size)
        )
        self.width = self.life.cols * self.cell_size
        self.height = self.life.rows * self.cell_size
        self.cell_height = self.life.rows
        self.cell_width = self.life.cols
        self.grid = self.life.curr_generation

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        lenght = self.cell_size - 1
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if self.grid[i][j] == 1:
                    color = pygame.Color("green")
                else:
                    color = pygame.Color("white")
                pygame.draw.rect(
                    self.screen,
                    color,
                    (i * self.cell_size + 1, j * self.cell_size + 1, lenght, lenght),
                )

    def run(self) -> None:
        # Copy from previous assignment
        pass
