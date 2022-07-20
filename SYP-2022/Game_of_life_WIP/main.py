import turtle as turt
import Grid
global board, grid_size

grid_size = 20
board_height= 30
board_width = 30
grid = Grid(grid_size, board_height, board_width)

def main():
    grid.make_grid()
    board = [[False] * board_width]*board_height
    screen = turt.Screen()
    screen.tracer(0)
    screen.title("Game of Life")
    screen.bgcolor("black")
    screen.setup(width=grid_size*board_width, height=grid_size*board_height)
    while True:
        make_gird()
        screen.update()
        screen.mainloop()

if __name__ == "__main__":
    main()