from terrain.model import Terrain, Flux

def test_init_terrain():

    SIZE = 256

    my_terrain = Terrain(SIZE)
    assert my_terrain.size == SIZE

    # test that terrain height is a 2d array
    assert len(my_terrain.terrain_height) == SIZE
    assert len(my_terrain.terrain_height[0]) == SIZE

    # test that water height is a 2d array
    assert len(my_terrain.water_height) == SIZE
    assert len(my_terrain.water_height[0]) == SIZE

def test_flux():

    SIZE = 256

    flux = Flux(.1, .2, .3, .4)

    assert flux.left == .1
    assert flux.right == .2
    assert flux.top == .3
    assert flux.bottom == .4
