from enum import Enum, auto
from point import Point
from line import Line
from window import Window

class Wall(Enum):
    LEFT = auto()
    RIGHT = auto()
    TOP = auto()
    BOTTOM = auto()


class Cell():
    def __init__(self, x1, y1, x2, y2, window = None):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__win = window

        self.has_left_wall   = True
        self.has_right_wall  = True
        self.has_top_wall    = True
        self.has_bottom_wall = True

        self.visited = False
        

    def draw(self):
        if self.__win != None:
            self.__win.draw_line(self.get_wall(Wall.LEFT),   "black" if self.has_left_wall else "white")
            self.__win.draw_line(self.get_wall(Wall.RIGHT),  "black" if self.has_right_wall else "white")
            self.__win.draw_line(self.get_wall(Wall.TOP),    "black" if self.has_top_wall else "white")
            self.__win.draw_line(self.get_wall(Wall.BOTTOM), "black" if self.has_bottom_wall else "white")


    def draw_move(self, to_cell, undo = False):
        color = "gray" if undo else "red"
        line = Line(self.get_center(), to_cell.get_center())
        if self.__win != None:
            self.__win.draw_line(line, color)


    def get_wall(self, wall):
        a = b = None
        match wall:
            case Wall.LEFT:
                a = Point(self.__x1, self.__y1)
                b = Point(self.__x1, self.__y2)
            case Wall.RIGHT:
                a = Point(self.__x2, self.__y1)
                b = Point(self.__x2, self.__y2)
            case Wall.TOP:
                a = Point(self.__x1, self.__y1)
                b = Point(self.__x2, self.__y1)
            case Wall.BOTTOM:
                a = Point(self.__x1, self.__y2)
                b = Point(self.__x2, self.__y2)
        return Line(a, b)


    def get_center(self):
        center_x = (self.__x1 + self.__x2) / 2
        center_y = (self.__y1 + self.__y2) / 2
        return Point(center_x, center_y)


    def get_coordinates(self):
        return (self.__x1, self.__y1, self.__x2, self.__y2)


    def __eq__(self, other):
        if isinstance(other, Cell):
            return self.get_coordinates() == other.get_coordinates()
        return False

    def __str__(self):
        return f"Cell(x1={round(self.__x1)} y1={round(self.__y1)}, x2={round(self.__x2)}, y2={round(self.__y2)})"

    def __repr__(self):
        return f"Cell(x1={round(self.__x1)} y1={round(self.__y1)}, x2={round(self.__x2)}, y2={round(self.__y2)})"