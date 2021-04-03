import copy
import pathlib
import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        # Copy from previous assignment
        grid = []
        grid_add = []
        if randomize == False:
            for i in range(0, self.cell_height):
                for j in range(0, self.cell_width):
                    grid_add += [0]
                grid += [grid_add]
                grid_add = []
        else:
            for i in range(0, self.cell_height):
                for j in range(0, self.cell_width):
                    grid_add += [random.randint(0, 1)]
                grid += [grid_add]
                grid_add = []
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        # Copy from previous assignment
        neighbours = []
        row, col = cell
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (
                    self.cell_height > row + i >= 0
                    and self.cell_width > col + j >= 0
                    and (i, j) != (0, 0)
                ):
                    neighbours += [self.grid[row + i][col + j]]
        return neighbours

    def get_next_generation(self) -> Grid:
        # Copy from previous assignment
        clone_grid = self.create_grid(False)
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if sum(self.get_neighbours((i, j))) == 3 and (self.grid[i][j] == 0):
                    clone_grid[i][j] = 1
                elif 1 < sum(self.get_neighbours((i, j))) < 4 and self.grid[i][j] == 1:
                    clone_grid[i][j] = 1
        return clone_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = copy.deepcopy(self.curr_generation)
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        if self.generations == self.max_generations:
            return True
        else:
            return False

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        if self.curr_generation == self.prev_generation:
            return False
        else:
            return True

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        curr_file = open(filename, "r")
        curr_file_list = [[int(col) for col in row.strip()] for row in curr_file]
        curr_file.close()

        game = GameOfLife((len(curr_file_list), len(curr_file_list[0])))
        game.curr_generation = curr_file_list
        return game

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        pass
