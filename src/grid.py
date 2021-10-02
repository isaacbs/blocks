import random
import math
from cell import Cell

class Grid:
    """A grid of cells used to make up the maze"""

    def __init__(self, numRows, numCols, lCorner):
        self.numRows = numRows
        self.numCols = numCols
        self.lCorner = lCorner
        self.cells = list()


        for y in range(lCorner[0],lCorner[0]+numRows):
            self.cells.append(list())
            for x in range(lCorner[1],lCorner[1]+numCols):
                self.cells[y-lCorner[0]].append(Cell(y,x))
                print("(",self.cells[y-lCorner[0]][x-lCorner[1]].y,",", self.cells[y-lCorner[0]][x-lCorner[1]].x,")")
    
    def collision_check(self, other):
        newCells = list()
        set1 = set()
        set2 = set()
        # st = set(tuple(ind.y,ind.x) for c in other.cells)
        for ind in range(len(other.cells)):
            set1.update((tuple([c[ind].y, c[ind].x]) for c in other.cells))
        
        for ele in range(len(self.cells)):
            set2.update((tuple([c[ele].y, c[ele].x]) for c in self.cells))

        newCells = set(set1).intersection(set2)
        # newCells.append(Cell(c1[ele].y, c1[ele].x))
        print("dis", newCells)
        return newCells
        