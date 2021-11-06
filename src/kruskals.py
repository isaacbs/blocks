from src.cell import Cell
from src.grid import Grid
import random

def kruskals(grid):
    cells = [{}]
    walls = [{}]
    i = 0
    j = 0
    for cellrow in grid.cells:
        for cell in cellrow:
            for wall in cell.walls:
                walls[i] = {wall}
                i+=1
            cells[j] = {cell}
            j+=1
         
    while walls != []:
        wallNo = random.randint(0, len(walls)-1)    #get a random wall out of the list of walls
        if walls[wallNo].getValue() == True:        #check what the value of the wall currently is
            cellNo = wallNo//4                      #ass 
            curCell = cells[cellNo]
            curWallKey = walls[wallNo].getKey()
            exists = False
            if curWallKey == "top":
                for cell in cells:
                    if cell.y == (curCell.y - 1) and cell.walls[bottom] == True:

