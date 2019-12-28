
from collections import namedtuple

class Terrain:
    def __init__(self, size):
        self.size = size
        self.terrain_height = array(self.size)
        self.water_height = array(self.size)
        self.suspended_sediment = array(self.size)
        self.flux = array(self.size, value = Flux(0,0,0,0))

Flux = namedtuple('Flux', ['left', 'right', 'top', 'bottom'])

def array(size, value=0):
    """Return a square, 2d array of the given value"""
    return [[value for x in range(size)] for y in range(size)]
