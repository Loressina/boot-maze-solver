from point import Point
from tkinter import Canvas

class Line():
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def draw(self, canvas, fill_color = "black"):
        canvas.create_line(
            self.a.x, self.a.y,
            self.b.x, self.b.y,
            fill=fill_color,
            width=2)