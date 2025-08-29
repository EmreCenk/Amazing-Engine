import os
from graphics.managing_graphics import Engine
import pygame

def zoom(event):
    zpower = 50 * my_engine.delta_time
    if event.button == 4:
        my_engine.camera.shift("z", -zpower)

    elif event.button == 5:
        my_engine.camera.shift("z", +zpower)


def update():

    power_level = p_original * my_engine.delta_time

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





my_engine = Engine(800, 600, __file__, delay_time=25)
my_engine.light.luminosity = 50
letters = my_engine.create_text("Amazing Engine\nby Emre Cenk", [20, 0, -10], 3, 0.1)

my_engine.bind_event(pygame.MOUSEBUTTONDOWN, zoom)

p_original = 30
p_z_original = 30



my_engine.start_engine()



