import curses

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """ Отобразить рамку. """
        screen.clear()
        height, width = screen.getmaxyx()
        line = ""
        for i in range(height):
            for j in range(width):
                if (
                    (i == 0 and j == 0)
                    or (i == height - 1 and j == width - 1)
                    or (i == 0 and j == width - 1)
                    or (i == height - 1 and j == 0)
                ):
                    line += "+"
                elif (i == 0 and j != 0 and j != width - 1) or (
                    i == height - 1 and j != 0 and j != width - 1
                ):
                    line += "-"
                elif (i != 0 and i != height - 1 and j == 0) or (
                    i != 0 and i != height - 1 and j == width - 1
                ):
                    line += "|"
                elif j != 0 and j != width - 1 and i != 0 and i != height - 1:
                    line += " "
        screen.addstr(line)

    def draw_grid(self, screen) -> None:
        """ Отобразить состояние клеток. """
        pass

    def run(self) -> None:
        screen = curses.initscr()
        # PUT YOUR CODE HERE
        curses.endwin()
