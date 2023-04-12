import pygame
class shape_2d:

    def __init__(self,color,fill_bool=True):
        self.color = color
        self.fill = fill_bool
        self.triangles = [] #all shapes are represented as combined triangles. This is the list of triangles

    def draw(self,window):
        for tri in self.triangles:
            if self.fill:
                pygame.draw.polygon(window, points=tri.vertices, color=self.color)

            else:
                pygame.draw.line(window,start_pos=tri.vertex1,end_pos=tri.vertex2,color=self.color)
                pygame.draw.line(window,start_pos=tri.vertex2,end_pos=tri.vertex3,color=self.color)
                pygame.draw.line(window,start_pos=tri.vertex3,end_pos=tri.vertex1,color=self.color)



class triangle:
    def __init__(self,vertex1,vertex2,vertex3):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex3 = vertex3
        tri.vertices = [vertex1,vertex2,vertex3]


class quadrilateral:
    def __init__(self,vertex1,vertex2,vertex3,vertex4):


    def convert_to_triangles(self,top_left,bottom_right):

