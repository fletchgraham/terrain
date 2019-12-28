
from collections import namedtuple

class Terrain:
    def __init__(self, size):
        self.size = size
        self.terrain_height = array(self.size)
        self.water_height = array(self.size)
        self.suspended_sediment = array(self.size)

Flux = namedtuple('Flux', ['left', 'right', 'top', 'bottom'])

def array(size, value=0):
    """Return a square, 2d array of the given value"""
    return [[0 for x in range(size)] for y in range(size)]
