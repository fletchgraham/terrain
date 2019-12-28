from terrain.model import Terrain, Flux, UV

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

    # test that suspended_sediment is a 2d array
    assert len(my_terrain.suspended_sediment) == SIZE
    assert len(my_terrain.suspended_sediment[0]) == SIZE

    # flux
    assert my_terrain.flux[0][0].left == 0

    # velocity_vector
    assert my_terrain.velocity[0][0].u == 0

def test_uv():
    velocity_vector = UV(.1, .3)

    assert velocity_vector.u == .1
    assert velocity_vector.v == .3



def test_flux():

    flux = Flux(.1, .2, .3, .4)

    assert flux.left == .1
    assert flux.right == .2
    assert flux.top == .3
    assert flux.bottom == .4
