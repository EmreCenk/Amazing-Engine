import pygame
from Mathematical_Functions.projecting import project_3d_point_to_2d, project_triangle
class shape_2d:

    def __init__(self,color,fill_bool=False):
        self.color = color
        self.fill = fill_bool
        self.triangles = [] #all shapes are represented as combined triangles. This is the list of triangles

    def draw(self,window):
        for tri in self.triangles:
            height = window.get_height()
            width = window.get_width()
            v1_2d,v2_2d,v3_2d = project_triangle(tri.vertex1,tri.vertex2,tri.vertex3,width,height)

            if self.fill:
                pygame.draw.polygon(window, self.color,(v1_2d,v2_2d,v3_2d))

            else:


                pygame.draw.line(window,start_pos=v1_2d,end_pos=v2_2d,color=self.color)
                pygame.draw.line(window,start_pos=v2_2d,end_pos=v3_2d,color=self.color)
                pygame.draw.line(window,start_pos=v3_2d,end_pos=v1_2d,color=self.color)



class triangle(shape_2d):
    def __init__(self,vertex1,vertex2,vertex3,color = "white",fill_bool=True):
        super().__init__(color,fill_bool)
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex3 = vertex3
        self.vertices = [vertex1,vertex2,vertex3]

        self.triangles.append(self) #there is only one triangle



# class quadrilateral:
#     def __init__(self,vertex1,vertex2,vertex3,vertex4):
#
#
#     def convert_to_triangles(self,top_left,bottom_right):

