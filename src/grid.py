import random
import math
from cell import Cell
from dataclasses import dataclass
import dataclasses as dc

@dataclass(init=True, repr=True, eq=True, order=True)
class Grid:
    """A grid of cells used to make up the maze"""
    numRows: int
    numCols: int
    map: list = dc.field(default_factory=list)

    def create_grid(self):
        self.map = [[Cell(i, j) for i in range(numRows)] for x in range(numCols)]

    # def collision_check(self, other):
    #     newCells = list()
    #     set1 = set()
    #     set2 = set()
    #     # st = set(tuple(ind.y,ind.x) for c in other.cells)
    #     for ind in range(len(other.cells)):
    #         set1.update((tuple([c[ind].y, c[ind].x]) for c in other.cells))
        
    #     for ele in range(len(self.cells)):
    #         set2.update((tuple([c[ele].y, c[ele].x]) for c in self.cells))

    #     newCells = set(set1).intersection(set2)
    #     # newCells.append(Cell(c1[ele].y, c1[ele].x))
    #     print("dis", newCells)
    #     return newCells
    
    def 