from cell import Cell
from time import sleep

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._create_cells()
        self._draw_cells()

    def _create_cells(self):
        self.__cells = []

        for col in range(0, self.__num_cols):
            col_cells = []
            for row in range(0, self.__num_rows):
                x1 = self.__x1 + col * self.__cell_size_x
                y1 = self.__y1 + row * self.__cell_size_y
                x2 = x1 + self.__cell_size_x
                y2 = y1 + self.__cell_size_y
                col_cells.append(Cell(x1, y1, x2, y2, self.__win))
            self.__cells.append(col_cells)

    def _draw_cells(self):
        for col in self.__cells:
            for cell in col:
                cell.draw()
                self._animate()

    def _animate(self):
        self.__win.redraw()
        sleep(0.05)