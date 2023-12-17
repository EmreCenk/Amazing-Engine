from graphics.managing_graphics import Engine
import models.shapes_3d as sh3

class Rubiks_Cube(sh3.Cube):

    def __init__(self, center_coordinates, side_length, color):
        super().__init__(center_coordinates, side_length, color)

engine = Engine(800, 600, __file__, delay_time=10)

ex_cube = Rubiks_Cube(center_coordinates=[-10, 0, -10], color=(255, 255, 255), side_length=10)
engine.add_model(ex_cube)

def update():
    ex_cube.rotate("x", engine.delta_time * 40)
    ex_cube.rotate("y", engine.delta_time * 40)
    engine.render_frame()

engine.start_engine()