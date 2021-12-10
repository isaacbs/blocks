from df_maze import Maze



# Maze dimensions (ncols, nrows)
nx, ny = 25, 25
# Maze entry position
ix, iy = 0, 0

maze = Maze(nx, ny, ix, iy)
maze.make_maze()

print(maze)
maze.write_svg('maze.svg')


