
import os
from graphics.managing_graphics import Engine
from models.shapes_3d import Cube
import pygame

engine = Engine(800, 600, os.getcwd(), "cube_of_cubes", delay_time=25)
engine.light.luminosity = 80

l = h = f = 5
cubes = []

def get_color(offset, OFF_MAX = 15):
    return ((offset + OFF_MAX) / (2.0 * OFF_MAX) * 255)
for i in range(l):
    for j in range(h):
        for b in range(f):
            current_cube = Cube(center_coordinates=[0,0,0],
                                side_length=2,
                                color=(255,255,255))

            current_cube.shift("x", -4 * j)
            current_cube.shift("y", 4 * i)
            current_cube.shift("z", 4 * b)

            current_cube.shift("x", 5)
            current_cube.shift("y", -8)
            current_cube.shift("z", -15)

            x,y,z = current_cube.center
            current_cube.change_color(
                [get_color(x),
                 get_color(y),
                 get_color(z)]
            )
            cubes.append(current_cube)
            engine.add_model(current_cube)


p_original = 30
p_z_original = 30
def update():

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        engine.stop_engine()

    a, b, c = cubes[len(cubes)//2].center
    for i in range(len(cubes)):
        cubes[i].rotate_around_point([a, b, c],"y",60*engine.delta_time)
        cubes[i].rotate_around_point([a, b, c],"x",59*engine.delta_time)
        cubes[i].rotate_around_point([a, b, c],"z",58*engine.delta_time)

def start():
    pass #to avoid the warning
engine.start_engine()
pygame.quit()
quit()
