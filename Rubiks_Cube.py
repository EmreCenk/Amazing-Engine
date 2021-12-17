from graphics.managing_graphics import Engine
import models.shapes_3d as sh3

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


def update():
    # ex_cube.rotate("x", engine.delta_time * 40)
    # ex_cube.rotate("y", engine.delta_time * 40)
    engine.render_frame()

engine.start_engine()