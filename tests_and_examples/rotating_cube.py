from graphics.managing_graphics import Engine
import models.shapes_3d as sh3
from constants import WIREFRAME
screen_width = 800
screen_height = 600

engine = Engine(screen_width, screen_height, __file__, delay_time=25)
ex_cube = sh3.Cube(center_coordinates=[-10, 0, -10],
                   color=(255, 255, 255),
                   side_length=10)

# ex_cube.change_draw_style(WIREFRAME)
engine.add_model(ex_cube)



def update():

    ex_cube.rotate("x", engine.delta_time * 40)
    ex_cube.rotate("y", engine.delta_time * 40)
    engine.render_frame()

engine.start_engine()


