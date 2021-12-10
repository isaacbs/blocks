from grid import Grid
from cell import Cell





c1 = Cell(5, 2)
print(c1.row)
print(c1.col)

print(c1.west)
print(c1.neighbors)
print(repr(c1))



grid1 = Grid(10, 10)
grid1.create_grid()
grid1.initialize_cells()
print(grid1.cells)
print("grid 2")
grid2 = Grid(4, 10, (3,0))

# grid1.collision_check(grid2)



