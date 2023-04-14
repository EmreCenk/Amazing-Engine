
from graphics.shapes_2d import quadrilateral,shape_2d

class shape_3d(shape_2d):
    def __init__(self,color,fill_bool):
        super().__init__(color,fill_bool)


class rectangular_prism(shape_3d):

    def __init__(self,top_1, top_2, bottom_1, bottom_2,color="white",fill_bool=False):
        super().__init__(color,fill_bool)
        #We only need 4 coordinates to represent the rectangular prism

    def generate_cube_coordinates(self,xc,yc,zc,s):
        pass