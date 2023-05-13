

import os
from graphics.managing_graphics import graphics_manager
import pygame
import models.shapes_3d as sh3

Engine = graphics_manager(800, 600, os.getcwd(), "run", delay_time=25)
shift = 0
side = 5
v1, v2, v3, v4, v5, v6, v7, v8 = [shift, shift, side], [side, shift, side], [side, shift, shift], [shift, shift, shift], \
                                 [shift, side, side], [side, side, side], [side, side, shift], [shift, side, shift]

tester_rectangle = sh3.rectangular_prism(v1, v2, v3, v4, v5, v6, v7, v8, color=(255, 255, 255))
Engine.add_model(tester_rectangle)


def zoom(event):
    zpower = 10*Engine.delta_time
    if event.button == 4:
        Engine.camera.move("z", -zpower)

    elif event.button == 5:
        Engine.camera.move("z", +zpower)

Engine.bind_event(pygame.MOUSEBUTTONDOWN, zoom)




def update():
    p_original = 10
    p_z_original = 10
    power_level = p_original * Engine.delta_time
    zpower = p_z_original * Engine.delta_time
    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        Engine.camera.move("y", -power_level)

    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        Engine.camera.move("y", power_level)

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        Engine.camera.move("x", power_level)

    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        Engine.camera.move("x", -power_level)

    power_level += Engine.delta_time * 10
    if keys[pygame.K_k]:
        Engine.camera.rotate("x", power_level)

    elif keys[pygame.K_i]:
        Engine.camera.rotate("x", -power_level)

    if keys[pygame.K_j]:
        Engine.camera.rotate("y", -power_level)

    if keys[pygame.K_l]:
        Engine.camera.rotate("y", +power_level)


Engine.init_loop()



