from grid import Grid
from cell import Cell

grid1 = Grid(10, 10, (0, 0))
print("grid 2")
grid2 = Grid(4, 10, (3,0))

grid1.collision_check(grid2)



