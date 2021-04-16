
import pygame
from Mathematical_Functions.projecting import project_3d_point_to_2d
conversion = {"x":0,
              "y":1,
              "z":2}

class shape:

    def __init__(self,color):
        self.color = color
        self.triangles = [] #all shapes are represented as combined triangles. This is the list of triangles
        self.vertices = set()
        self.edges = set()

    def wireframe_draw(self,window):
        for edge in self.edges:
            height = window.get_height()
            width = window.get_width()

            #getting the 2d points:
            p1=[0,0]
            p2=[0,0]


            pygame.draw.line(window,start_pos=p1,end_pos=p2,color=self.color)


class triangle(shape):

    def __init__(self,v1,v2,v3,color,):
        super().__init__(color = color )
        self.v1 = list(v1)
        self.v2 = list(v2)
        self.v3 = list(v3)

        self.vertices = [self.v1,self.v2,self.v3]

    def move_yourself(self,axis, how_much):
        if axis in conversion:
            axis = conversion[axis]

        self.v1[axis] += how_much
        self.v2[axis] += how_much
        self.v3[axis] += how_much

    def get_projected_coordinates(self):

        w,h = pygame.display.get_window_size()
        return project_3d_point_to_2d(self.v1[0],self.v1[1],self.v1[2],w,h),\
               project_3d_point_to_2d(self.v2[0],self.v2[1],self.v2[2],w,h),\
               project_3d_point_to_2d(self.v3[0],self.v3[1],self.v3[2],w,h)

if __name__ == '__main__':
    self = triangle([1,2,3],[3,4,5],[4,5,6],"white")
    print(self.vertices)
    self.v1[0]+=1000
    print(self.vertices)