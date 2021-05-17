
from graphics.managing_graphics import Engine
import os
import models.shapes_3d as sh3
screen_width = 800
screen_height = 600
script_name = "rotating_cube"
engine = Engine(screen_width, screen_height, os.getcwd(), script_name, delay_time=25)
ex_pyramid = sh3.Pyramid(center_coordinates=[0,0,-10],
            color = (255,255,255),
            side_length=10)

engine.add_model(ex_pyramid)

def update():
    ex_pyramid.rotate("x", engine.delta_time*40)
    ex_pyramid.rotate("y", engine.delta_time*40)
    engine.render_frame()
engine.start_engine()
