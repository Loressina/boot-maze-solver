from window import Window
from cell import Cell
from maze import Maze

def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)


    # c_1 = Cell(50, 50, 100, 100, win)
    # c_1.has_left_wall = False
    # c_1.draw()

    # c_2 = Cell(125, 125, 200, 200, win)
    # c_2.has_right_wall = False
    # c_2.draw()

    # c_3 = Cell(225, 225, 250, 250, win)
    # c_3.has_bottom_wall = False
    # c_3.draw()

    # c_4 = Cell(300, 300, 500, 500, win)
    # c_4.has_top_wall = False
    # c_4.draw()

    # c_1.draw_move(c_2)

    win.wait_for_close()


main()