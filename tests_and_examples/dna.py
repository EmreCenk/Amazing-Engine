
from graphics.managing_graphics import Engine
import models.shapes_3d as sh3
import pygame

def get_color(index, how_many):
    div = 255*3/how_many

    r = 10
    g = 10
    b = 10
    i=0
    while r<255 and i<index:
       r+=div
       i+=1
    if i>index or r>255:
        r = 255

    index -= i
    i = 0

    while g<255 and i<index:
       g+=div
       i+=1

    if i>index or g>255:
        g = 255





    index -= i
    i = 0

    while b<255 and i<index:
       b+=div
       i+=1

    if i>index or b>255:
        b = 255
    return (r,g,b)


engine = Engine(800, 600, __file__, delay_time=25)
engine.light.luminosity = 8000



def zoom(event):
    zpower = 50 * engine.delta_time
    if event.button == 4:
        engine.camera.shift("z", -zpower)

    elif event.button == 5:
        engine.camera.shift("z", +zpower)

engine.bind_event(pygame.MOUSEBUTTONDOWN, zoom)


center_coor = [0,0,-10]
num = 100
pyramids = []
helix_radius = 0.5
for i in range(num):
    newc = list(center_coor)
    newc[1] += helix_radius*i*0.8
    current_pyramid = sh3.Cube(
        center_coordinates=newc,
        color = (255,255,255),
        side_length=helix_radius
    )

    current_pyramid.shift("x",helix_radius*5)
    current_pyramid.rotate_around_point(newc, "y", i*20)
    current_pyramid.change_color(get_color(i,num))
    pyramids.append(current_pyramid)
    engine.add_model(current_pyramid)

p_original = 30
p_z_original = 30
engine.camera.shift("y",20)
def update():
    power_level = p_original * engine.delta_time

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        engine.stop_engine()
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

try:
    engine.start_engine()

    pygame.quit()
except:
    pygame.quit()

