from graphics.shapes_2d import shape



class obj_mesh(shape):

    def __init__(self, path_to_object, color = (255,255,255)):
        super().__init__(color)
        self.path_to_object = path_to_object

