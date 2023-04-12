import pygame
from Mathematical_Functions.projecting import project_triangle
class shape_2d:

    def __init__(self,color,fill_bool=False):
        self.color = color
        self.fill = fill_bool
        self.triangles = [] #all shapes are represented as combined triangles. This is the list of triangles

    def draw(self,window):
        for tri in self.triangles:
            height = window.get_height()
            width = window.get_width()

            #getting the 2d points:
            v1_2d,v2_2d,v3_2d = project_triangle(tri.vertex1,tri.vertex2,tri.vertex3,width,height)

            if self.fill:
                pygame.draw.polygon(window, self.color,(v1_2d,v2_2d,v3_2d))

            else:


                pygame.draw.line(window,start_pos=v1_2d,end_pos=v2_2d,color=self.color)
                pygame.draw.line(window,start_pos=v2_2d,end_pos=v3_2d,color=self.color)
                pygame.draw.line(window,start_pos=v3_2d,end_pos=v1_2d,color=self.color)



class triangle(shape_2d):
    def __init__(self,vertex1,vertex2,vertex3,color = "white",fill_bool=False):
        super().__init__(color,fill_bool)
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex3 = vertex3
        self.vertices = [vertex1,vertex2,vertex3]

        self.triangles.append(self) #there is only one triangle



class quadrilateral(shape_2d):
    def __init__(self,v1,v2,v3,v4,_color = "white", fill_bool = False):

        super().__init__(color=_color)
        self.convert_to_triangles(v1,v2,v3,v4)

    def convert_to_triangles(self,v1,v2,v3,v4):
        self.triangles.append(
            triangle(
            v1,v2,v3,color = self.color, fill_bool=self.fill
        )
        )

        self.triangles.append(
            triangle(
                v3[0], v4[1], v1[2], color=self.color, fill_bool=self.fill
            )
        )

