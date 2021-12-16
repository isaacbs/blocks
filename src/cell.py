from dataclasses import dataclass
import dataclasses as dc
import random

class Cell:
    wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}
        self.set = {(self.x,self.y)}
        self.insolution = False
    # links: list = dc.field(default_factory=list)
    # neighbors: list = dc.field(default_factory=list)
    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.x == other.x and self.y == other.y and self.set.isdisjoint(other.set)
    # def is_walls_between(self, neighbour):
    #     if self.y - neighbour.y == 1 and self.top and neighbour.bottom:
    #         return True
    #     elif self.y - neighbour.y == -1 and self.bottom and neighbour.top:
    #         return True
    #     elif self.x - neighbour.x == 1 and self.left and neighbour.right:
    #         return True
    #     elif self.x - neighbour.x == -1 and self.right and neighbour.left:
    #         return True
    #     return False
    

    def walls_exist(self):
        return all(self.walls.values())

    def destroy_wall(self, other, wall):
        self.walls[wall] = False
        other.walls[Cell.wall_pairs[wall]] = False

    # def unlink(self, other, bidi=True):
    #     self.links.remove(other)
    #     other.unlink(other, self, False)
    #     if bidi:
    #         return self
    
    # def isLinked(self, other):
    #     if other in self.links:
    #         return True
    #     else:
    #         return False