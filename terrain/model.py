

class Terrain:
    def __init__(self, size):
        self.size = size
        self.terrain_height = empty_array(self.size)


def empty_array(size):
    return [[0 for x in range(size)] for y in range(size)]
