from window import Window
from point import Point
from line import Line

def main():
    win = Window(800, 600)

    a = Point(100, 50)
    b = Point(600, 400)
    line = Line(a, b)
    win.draw_line(line, "black")

    win.wait_for_close()


main()