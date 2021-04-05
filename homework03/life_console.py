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
        height, width = screen.getmaxyx()

        x = (width - self.life.cols) // 2
        y = (height - self.life.rows) // 2

        for n_row, row in enumerate(self.life.curr_generation):
            for n_col, col in enumerate(row):
                if col == 1:
                    try:
                        screen.addstr(n_row + y, n_col + x, "*")
                    except curses.error:
                        pass
        screen.refresh()
        screen.getch()

    def run(self) -> None:
        screen = curses.initscr()
        # PUT YOUR CODE HERE
        curses.endwin()
