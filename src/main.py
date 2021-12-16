from grid import Grid
from cell import Cell
import random


# c1 = Cell(10, 10)
# c2 = Cell(5,5)
# c3 = Cell(1,1)

# print(c1.set)
# print(c2.set)
# c1.set.update(c2.set)
# print(c1.set.isdisjoint(c2.set))
# print(c2.set.isdisjoint(c1.set))
# print(c1.set.isdisjoint(c3.set))
# c2.set.update(c1.set)
# c3.set.update(c2.set)
# print(c3.set)
# print(c1.set)
# print(c2.set)
# print(c1.set.isdisjoint(c2.set))

# for i in range(3):
#     # a = random.randint(5,100)
#     # b = random.randint(5,100)
#     g1 = Grid(125, 125)
#     g1.create_grid()
#     a = random.randint(0,3)
#     if a == 0:
#         g1.depth_first()
#     elif a == 1:
#         g1.binary()
#     elif a == 2:
#         g1.sidewinder()
#     else:
#         g1.kruskals()
#     # mat = g1.create_adj_matrix()
#     # aList = g1.convert(mat)
#     g1.print_maze(i+26)
#     g1.plot(i+26)

# print(g1.uniform_cost_search(aList, 0, [24]))
# print(g1.a_star(mat, 0, 24))

# g2 = Grid(25, 25)
# g3 = Grid(25, 25)
# g4 = Grid(25, 25)
# g1.create_grid()
# g2.create_grid()
# g3.create_grid()
# g4.create_grid()
# # print(g1.map)
# g1.kruskals()
# g2.depth_first()
# g3.binary()
# g4.sidewinder()
# print(g1)
# print(g2)
# print(g3)
# print(g4)
# mat = g4.create_adj_matrix()
# aList = g4.convert(mat)
# print(g4.bfs_shortest_path(aList, 0, 124))
# g1.write_svg('g1.svg')
# g2.write_svg('g2.svg')
# g3.write_svg('g3.svg')
# g4.write_svg('g4.svg')

g5 = Grid(12,12)
g5.create_grid()
g5.kruskals()
mat = g5.create_adj_matrix()
aList = g5.convert(mat)
# print(aList)

path = g5.dfs_shortest_path(aList, 0, 143)
g5.write_path(path)
print(g5.print_maze(253))
g5.plot(253)
