from dataclasses import dataclass
import dataclasses as dc


@dataclass(init=True, repr=True, eq=True, order=True)
class Cell:
    row: int
    col: int
    visited: bool = False
    north: bool = True
    south: bool = True
    west: bool = True
    east: bool = True
    links: list = dc.field(default_factory=list)
    neighbors: list = dc.field(default_factory=list)
    

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
    
    def link(self, other, bidi = True):
        self.links[other] = True
        other.link(other, self, False)
        if bidi:
            return self

    def unlink(self, other, bidi=True):
        self.links.remove(other)
        other.unlink(other, self, False)
        if bidi:
            return self
    
    def isLinked(self, other):
        if other in self.links:
            return True
        else:
            return False