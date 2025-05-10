from window import Window
from cell import Cell

def main():
    win = Window(800, 600)

    c_1 = Cell(50, 50, 100, 100, win)
    c_1.has_left_wall = False
    c_1.draw()

    c_2 = Cell(125, 125, 200, 200, win)
    c_2.has_right_wall = False
    c_2.draw()

    c_3 = Cell(225, 225, 250, 250, win)
    c_3.has_bottom_wall = False
    c_3.draw()

    c_4 = Cell(300, 300, 500, 500, win)
    c_4.has_top_wall = False
    c_4.draw()

    c_1.draw_move(c_2)

    win.wait_for_close()


main()