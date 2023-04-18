
import pygame
from Mathematical_Functions.projecting import project_3d_point_to_2d,convert_result
from Mathematical_Functions.coordinate_system_3d import rotate
from constants import conversion

class shape:

    def __init__(self,color):
        self.color = color
        self.triangles = [] #all shapes are represented as combined triangles. This is the list of triangle
        self.edges = []
        self.vertices = []

    def wireframe_draw(self,window,d=1,orthogonal=False):
        for edge in self.edges:
            height = window.get_height()
            width = window.get_width()

            if not orthogonal:
                #getting the 2d points:
                p1=project_3d_point_to_2d(edge[0],width,height,d)
                p2=project_3d_point_to_2d(edge[1],width,height,d)
            else:
                p1=convert_result(edge[0][0],edge[0][1],width,height)
                p2=convert_result(edge[1][0],edge[1][1],width,height)



            pygame.draw.line(window,start_pos=p1,end_pos=p2,color=self.color)
    def draw_all_triangles(self,window,d=1):
        for tri in self.triangles:
            tri.wireframe_draw(window,d)


    def move(self,axis,amount):
        if axis in conversion:
            axis = conversion[axis]

        for vert in self.vertices:
            vert[axis]+=amount

    def rotate(self,axis,angle):
        for vert in self.vertices:
            rotate(vert,axis,angle)


class triangle(shape):

    def __init__(self,v1,v2,v3,color = "white"):
        super().__init__(color = color )
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

        self.vertices = [self.v1,self.v2,self.v3]
        self.edges = [
            [self.v1,self.v2],
            [self.v2,self.v3],
            [self.v3,self.v1]
        ]

    # def move_yourself(self,axis, how_much):
    #     if axis in conversion:
    #         axis = conversion[axis]
    #
    #     self.v1[axis] += how_much
    #     self.v2[axis] += how_much
    #     self.v3[axis] += how_much

    def get_projected_coordinates(self):


        w,h = pygame.display.get_window_size()
        return project_3d_point_to_2d(self.v1,w,h),\
               project_3d_point_to_2d(self.v2,w,h),\
               project_3d_point_to_2d(self.v3,w,h)

    def rotate(self,axis,angle):
        rotate(self.v1,axis,angle)
        rotate(self.v2, axis,angle)
        rotate(self.v3,axis,angle)



class quadrilateral(shape):
    def __init__(self,v1,v2,v3,v4,_color = "white", fill_bool = False):
        #This class basically exists for the sole purpose of converting quadrilaterals to triangles

        super().__init__(color=_color)
        self.convert_to_triangles(v1,v2,v3,v4)

    def convert_to_triangles(self,v1,v2,v3,v4):

        t1=triangle(
            v1,v2,v3, color = self.color,
        )


        t2 = triangle(
                v3, v4, v1, color=self.color,
            )

        self.triangles.append(t1)
        self.triangles.append(t2)

if __name__ == '__main__':
    import graphics.shapes_3d as sh3

    shift = 1
    side = 100

    v1, v2, v3, v4, v5, v6, v7, v8 = [shift, shift, side], [side, shift, side], [side, shift, shift], [shift, shift,
                                                                                                       shift], \
                                     [shift, side, side], [side, side, side], [side, side, shift], [shift, side, shift]
    self = sh3.rectangular_prism(v1, v2, v3, v4, v5, v6, v7, v8)
    print(self.triangles[0].edges,self.edges)

    self.rotate("x",60)

    print(self.triangles[0].edges,self.edges)