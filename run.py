

import os
from graphics.managing_graphics import Engine
import pygame
import models.shapes_3d as sh3
from models.using_obj_files.using_obj_files import obj_mesh
my_engine = Engine(800, 600, os.getcwd(), "run", delay_time=25)


alpha = sh3.obj_mesh("models/using_obj_files/sample_object_files/utah_teapot.obj")
my_engine.add_model(alpha)




def zoom(event):
    zpower = 50 * my_engine.delta_time
    if event.button == 4:
        my_engine.camera.move("z", -zpower)

    elif event.button == 5:
        my_engine.camera.move("z", +zpower)

my_engine.bind_event(pygame.MOUSEBUTTONDOWN, zoom)




def update():
    p_original = 10
    p_z_original = 10
    power_level = p_original * my_engine.delta_time
    zpower = p_z_original * my_engine.delta_time
    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        my_engine.camera.move("y", -power_level)

    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        my_engine.camera.move("y", power_level)

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        my_engine.camera.move("x", power_level)

    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        my_engine.camera.move("x", -power_level)

    power_level += my_engine.delta_time * 10
    if keys[pygame.K_k]:
        my_engine.camera.rotate("x", power_level)

    elif keys[pygame.K_i]:
        my_engine.camera.rotate("x", -power_level)

    if keys[pygame.K_j]:
        my_engine.camera.rotate("y", -power_level-0.1)

    if keys[pygame.K_l]:
        my_engine.camera.rotate("y", +power_level-0.1)


    # if keys[pygame.K_SPACE]:
    #     tester_rectangle.move("x",0.1)
    #     print(tester_rectangle.triangles[0].vertices)
    #
    # tester_rectangle.rotate("y",10 * my_engine.delta_time)
    #
    #
    # tester_rectangle2.rotate("y", 30 * my_engine.delta_time)
    # tester_rectangle3.rotate("y", 30 * my_engine.delta_time)

my_engine.start_engine()



