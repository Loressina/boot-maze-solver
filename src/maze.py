from cell import Cell
from window import Window
from time import sleep
import random
from enum import Enum, auto


class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()
    TOP = auto()
    BOTTOM = auto()

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__rng = random.Random(seed)

        self._create_cells()

        # print(self.__cells)

        self._break_entrance_and_exit()
        self._draw_cells()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()


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


    def _break_entrance_and_exit(self):
        entrance = self.__cells[0][0]
        entrance.has_top_wall = False

        exit = self.__cells[-1][-1]
        exit.has_bottom_wall = False


    def _break_walls_r(self, col, row):
        self.__cells[col][row].visited = True

        while True:
            possible_directions = self._get_unvisited_neighbors(col, row)

            if len(possible_directions) == 0:
                self.__cells[col][row].draw()
                self._animate()
                return
            else:
                direction = self.__rng.randint(0, len(possible_directions) - 1)
                neighbor, coordinates = list(possible_directions.items())[direction]
                self._destroy_walls(neighbor, (col, row), coordinates)
                self._break_walls_r(coordinates[0], coordinates[1])


    def _get_unvisited_neighbors(self, col, row):
        neighbors = {}

        if 0 <= row - 1 < len(self.__cells[col]):
            if not self.__cells[col][row - 1].visited:
                neighbors[Direction.TOP] = (col, row - 1)

        if 0 <= row + 1 < len(self.__cells[col]):
            if not self.__cells[col][row + 1].visited:
                neighbors[Direction.BOTTOM] = (col, row + 1)

        if 0 <= col - 1 < len(self.__cells):
            if not self.__cells[col - 1][row].visited:
                neighbors[Direction.LEFT] = (col - 1, row)

        if 0 <= col + 1 < len(self.__cells):
            if not self.__cells[col + 1][row].visited:
                neighbors[Direction.RIGHT] = (col + 1, row)

        return neighbors


    def _destroy_walls(self, direction, current, neighbor):
        match direction:
            case Direction.TOP:
                self.__cells[current[0]][current[1]].has_top_wall = False
                self.__cells[neighbor[0]][neighbor[1]].has_bottom_wall = False
            case Direction.BOTTOM:
                self.__cells[current[0]][current[1]].has_bottom_wall = False
                self.__cells[neighbor[0]][neighbor[1]].has_top_wall = False
            case Direction.LEFT:
                self.__cells[current[0]][current[1]].has_left_wall = False
                self.__cells[neighbor[0]][neighbor[1]].has_right_wall = False
            case Direction.RIGHT:
                self.__cells[current[0]][current[1]].has_right_wall = False
                self.__cells[neighbor[0]][neighbor[1]].has_left_wall = False


    def _reset_cells_visited(self):
        for col in self.__cells:
            for cell in col:
                cell.visited = False


    def solve(self):
        return self._solve_r(0, 0)


    def _solve_r(self, col, row):
        self.__cells[col][row].visited = True

        # goal reached
        if col == self.__num_cols - 1 and row == self.__num_rows - 1:
            return True

        possible_directions = self._get_unvisited_reachable_neighbors(col, row)
        for direction, coordinates in possible_directions.items():
            self.__cells[col][row].draw_move(self.__cells[coordinates[0]][coordinates[1]])
            self._animate()
            if self._solve_r(coordinates[0], coordinates[1]):
                return True
            else:
                self.__cells[col][row].draw_move(self.__cells[coordinates[0]][coordinates[1]], True)
                self._animate()

        return False


    def _get_unvisited_reachable_neighbors(self, col, row):
        unvisited_neighbors = self._get_unvisited_neighbors(col, row)
        return dict(filter(lambda item: self._is_reachable(item[0], (col, row), item[1]), unvisited_neighbors.items()))


    def _is_reachable(self, direction, current, neighbor):
        match direction:
            case Direction.TOP:
                return (not self.__cells[current[0]][current[1]].has_top_wall
                    and not self.__cells[neighbor[0]][neighbor[1]].has_bottom_wall)
            case Direction.BOTTOM:
                return (not self.__cells[current[0]][current[1]].has_bottom_wall
                    and not self.__cells[neighbor[0]][neighbor[1]].has_top_wall)
            case Direction.LEFT:
                return (not self.__cells[current[0]][current[1]].has_left_wall
                    and not self.__cells[neighbor[0]][neighbor[1]].has_right_wall)
            case Direction.RIGHT:
                return (not self.__cells[current[0]][current[1]].has_right_wall
                and not self.__cells[neighbor[0]][neighbor[1]].has_left_wall)
        return False


    def _draw_cells(self):
        for col in self.__cells:
            for cell in col:
                cell.draw()
                self._animate()


    def _animate(self):
        if self.__win != None:
            self.__win.redraw()
            sleep(0.03)


    def get_cells(self):
        return self.__cells