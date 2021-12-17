from graphics.managing_graphics import Engine
import models.shapes_3d as sh3
import pygame

class Rubiks_Cube:
    """
    A wrapper class that basically holds 9 cubes.
    """
    def __init__(self, center_coordinates, cube_side_length, color):
        self.cubes = []
        for i in range(3):
            for j in range(3):
                for b in range(3):
                    current_cube = sh3.Cube(center_coordinates=center_coordinates,
                                        side_length=cube_side_length,
                                        color=color)

                    current_cube.shift("x", -cube_side_length * j)
                    current_cube.shift("y", cube_side_length * i)
                    current_cube.shift("z", cube_side_length * b)
                    self.cubes.append(current_cube)


engine = Engine(800, 600, __file__, delay_time=10)

ex_cube = Rubiks_Cube(center_coordinates=[0, 0, 0], color=(255, 255, 255), cube_side_length=4)
for k in ex_cube.cubes:
    engine.add_model(k)


p_original = 30
p_z_original = 30


def zoom(event):
    zpower = 50 * engine.delta_time
    if event.button == 4:
        engine.camera.shift("z", -zpower)

    elif event.button == 5:
        engine.camera.shift("z", +zpower)

engine.bind_event(pygame.MOUSEBUTTONDOWN, zoom)


def update():
    power_level = p_original * engine.delta_time

    keys = pygame.key.get_pressed()


    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        engine.camera.shift("y", -power_level)

    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        engine.camera.shift("y", power_level)

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        engine.camera.shift("x", power_level)

    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        engine.camera.shift("x", -power_level)

    power_level += engine.delta_time * 10


    if keys[pygame.K_k]:
        engine.camera.rotate("x", power_level)

    elif keys[pygame.K_i]:
        engine.camera.rotate("x", -power_level)

    if keys[pygame.K_j]:
        engine.camera.rotate("y", -power_level-0.1)

    if keys[pygame.K_l]:
        engine.camera.rotate("y", +power_level-0.1)

engine.start_engine()