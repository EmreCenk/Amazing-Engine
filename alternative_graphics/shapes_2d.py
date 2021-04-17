
import pygame
from Mathematical_Functions.projecting import project_3d_to_2d
from Mathematical_Functions.coordinate_system_3d import rotate
from constants import conversion

class shape:

    def __init__(self,color):
        self.color = color
        self.triangles = [] #all shapes are represented as combined triangles. This is the list of triangle
        self.edges = []
        self.vertices = []

    def wireframe_draw(self,window,d=1):
        for edge in self.edges:
            height = window.get_height()
            width = window.get_width()

            #getting the 2d points:
            p1=project_3d_to_2d(edge[0],width,height,d)
            p2=project_3d_to_2d(edge[1],width,height,d)


            pygame.draw.line(window,start_pos=p1,end_pos=p2,color=self.color)


class triangle(shape):

    def __init__(self,v1,v2,v3,color = "white"):
        super().__init__(color = color )
        self.v1 = list(v1)
        self.v2 = list(v2)
        self.v3 = list(v3)

        self.vertices = [self.v1,self.v2,self.v3]
        self.edges = [
            [self.v1,self.v2],
            [self.v2,self.v3],
            [self.v3,self.v1]
        ]

    def move_yourself(self,axis, how_much):
        if axis in conversion:
            axis = conversion[axis]

        self.v1[axis] += how_much
        self.v2[axis] += how_much
        self.v3[axis] += how_much

    def get_projected_coordinates(self):


        w,h = pygame.display.get_window_size()
        return project_3d_to_2d(self.v1,w,h),\
               project_3d_to_2d(self.v2,w,h),\
               project_3d_to_2d(self.v3,w,h)

    def rotate(self,axis,angle):
        print(self.vertices)
        rotate(self.v1,axis,angle)
        rotate(self.v2, axis,angle)
        rotate(self.v3,axis,angle)
        print(self.vertices)
        print()

if __name__ == '__main__':
    self = triangle([1,2,3],[3,4,5],[4,5,6],"white")
    print(self.vertices)
    self.v1[0]+=1000
    print(self.vertices)