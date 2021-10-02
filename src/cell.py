class Cell:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.visited = False
        self.walls = {"top": True, "right": True, "bottom": True, "left": True}
        self.neighbors = list()

    def is_walls_between(self, neighbour):
        
        if self.row - neighbour.row == 1 and self.walls["top"] and neighbour.walls["bottom"]:
            return True
        elif self.row - neighbour.row == -1 and self.walls["bottom"] and neighbour.walls["top"]:
            return True
        elif self.col - neighbour.col == 1 and self.walls["left"] and neighbour.walls["right"]:
            return True
        elif self.col - neighbour.col == -1 and self.walls["right"] and neighbour.walls["left"]:
            return True

        return False
    