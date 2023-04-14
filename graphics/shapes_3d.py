
from graphics.shapes_2d import quadrilateral,shape_2d
from Mathematical_Functions.coordinate_system_3d import distance

class shape_3d(shape_2d):

    #Surprısınglyö every functıon ın a 2d shape ıs actually really usefull for 3d shapes. Perhaps I should rename the
    # shape_2d class to just shape in the future? (shape_3d should start branching off of shape_2d soon enough)

    def __init__(self,color,fill_bool):
        super().__init__(color,fill_bool)




class rectangular_prism(shape_3d):

    def __init__(self,top_1, top_2, bottom_1, bottom_2,color="white",fill_bool=False):
        super().__init__(color,fill_bool)
        self.generate_coordinates(top_1, top_2, bottom_1, bottom_2)
        #We only need 4 coordinates to represent the rectangular prism

    def generate_coordinates(self,v1,v2,v3,v4):
        pass
