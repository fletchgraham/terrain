from terrain.model import Terrain

def test_init_terrain():
    my_terrain = Terrain(1024)
    assert my_terrain.size == 1024

    # test that terrain height is a 2d array
    assert len(my_terrain.terrain_height) == 1024
    assert len(my_terrain.terrain_height[0]) == 1024
