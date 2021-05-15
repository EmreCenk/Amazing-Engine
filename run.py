

import os
from graphics.managing_graphics import Engine
import pygame
import models.shapes_3d as sh3
from models.using_obj_files.using_obj_files import obj_mesh
my_engine = Engine(800, 600, os.getcwd(), "run", delay_time=25)
my_engine.light.luminosity = 500

to_write = "WELCOME"
letter_objs = []

for i in range(len(to_write)):
    car = obj_mesh(rf"C:\Users\Murat\Downloads\uploads_files_1950256_{to_write[i]}.obj", (255,255,255))
    car.teleport(-8*i+23, 0 ,-10)
    car.rotate("x", -90)
    car.rotate("y", 180)
    car.scale(0.3)
    letter_objs.append(car)
    my_engine.add_model(car)


# tester_rectangle3 = sh3.Cube([10, 0, -10], 5, (255, 0, 255))
# tester_rectangle2 = sh3.Pyramid([25, 0, -10], 5, (255,0,0))
# tester_rectangle = sh3.Sphere([0,0,-10], 8, (255,255,0))
# my_engine.add_model(tester_rectangle)
# my_engine.add_model(tester_rectangle2)
# my_engine.add_model(tester_rectangle3)





def zoom(event):
    zpower = 50 * my_engine.delta_time
    if event.button == 4:
        my_engine.camera.shift("z", -zpower)

    elif event.button == 5:
        my_engine.camera.shift("z", +zpower)

my_engine.bind_event(pygame.MOUSEBUTTONDOWN, zoom)




def update():
    p_original = 30
    p_z_original = 30
    power_level = p_original * my_engine.delta_time
    zpower = p_z_original * my_engine.delta_time
    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        my_engine.camera.shift("y", -power_level)

    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        my_engine.camera.shift("y", power_level)

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        my_engine.camera.shift("x", power_level)

    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        my_engine.camera.shift("x", -power_level)

    power_level += my_engine.delta_time * 10
    if keys[pygame.K_k]:
        my_engine.camera.rotate("x", power_level)

    elif keys[pygame.K_i]:
        my_engine.camera.rotate("x", -power_level)

    if keys[pygame.K_j]:
        my_engine.camera.rotate("y", -power_level-0.1)

    if keys[pygame.K_l]:
        my_engine.camera.rotate("y", +power_level-0.1)


    if keys[pygame.K_SPACE]:
        print(car.center)

    # tester_rectangle.rotate("y",10 * my_engine.delta_time)
    #
    #
    # tester_rectangle2.rotate("y", 30 * my_engine.delta_time)
    # tester_rectangle3.rotate("y", 30 * my_engine.delta_time)

my_engine.start_engine()



