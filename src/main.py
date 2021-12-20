from grid import Grid
from cell import Cell
from generation import *
from pathfinding import *

# g = Grid(50,50)
# g.create_grid()
# depth_first(g)

# mat = create_adj_matrix(g)
# aList = convert(mat)

# path = dfs_shortest_path(aList, 0, 2499)

# write_path(g, path)

# cmap = g.random_colors()
# g.print_maze(303)
# g.plot(303, cmap)

g = Grid(5,30)
g.create_grid()
depth_first(g)
g.create_gif()

