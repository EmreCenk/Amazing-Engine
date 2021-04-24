from graphics.shapes_2d import shape
from graphics.using_obj_files.parse_obj_files import parse_triangle_list


class obj_mesh(shape):

    def __init__(self, path_to_object, color = (255,255,255)):
        super().__init__(color)
        self.path_to_object = path_to_object
        self.create_triangles()

    def create_triangles(self):
        self.triangles = parse_triangle_list(self.path_to_object)

