from graphics.shapes_2d import quadrilateral,shape
from Mathematical_Functions.coordinate_system_3d import rotate_around_point
import pygame
from constants import conversion
from Mathematical_Functions.shading import get_color

class shape_3d(shape):

    # Surprisingly, every function in the 2d shape class is actually really usefull for 3d shapes. Perhaps I should
    # rename the shape_2d class to just shape in the future? (shape_3d should start branching off of shape_2d soon
    # enough)

    def __init__(self,color):
        super().__init__(color)

    def define_center(self):
        """
        Finds the center of the object by taking
        the upper bounds of the object and treating it as a rectangle.
        The efficiency of this function does not really matter since it is called
        only once.
        """

        #The lambda part takes the index of the axis as the key when finding max
        max_x = max(self.vertices, key = lambda tri: tri[0])[0]
        min_x = min(self.vertices, key = lambda tri: tri[0])[0]

        max_y = max(self.vertices, key = lambda tri: tri[1])[1]
        min_y = min(self.vertices, key = lambda tri: tri[1])[1]

        max_z = max(self.vertices, key = lambda tri: tri[2])[2]
        min_z = min(self.vertices, key = lambda tri: tri[2])[2]

        #Taking the average of the upper and lower bounds to find the midpoint for all
        #dimensions:

        self.center = [
            (max_x + min_x) / 2,
            (max_y + min_y) / 2,
            (max_z + min_z) / 2,

        ]



    def move(self,axis,amount):
        #Overriding the move function to also move the center along with everything else:
        if axis in conversion:
            axis = conversion[axis]

        #This method updates both the self.v values and the self.vertices values
        for vert in self.vertices:
            vert[axis]+=amount

        self.center[axis] += amount

    def rotate(self,axis,angle):
        #Overriding the rotate function to also rotate the center along with everything else:

        for vert in self.vertices:
            rotate_around_point(self.center, vert, axis, angle)

        # rotate_around_point(self.center,self.center, axis, angle)



class rectangular_prism(shape_3d):

    def __init__(self,v1, v2, v3, v4, v5, v6, v7, v8, color=(255,255,255),):
        """Label the first 4 points starting with the top left corner of a given side, and moving in a clockwise
        direction. Label the last 4 points by picking the vertex that has not been labeled which is also connected to vertex 1.
        From there, keep labeling in a clockwise direction. """
        super().__init__(color)

        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4
        self.v5 = v5
        self.v6 = v6
        self.v7 = v7
        self.v8 = v8

        self.generate_triangles()
        self.define_center()



    def generate_triangles(self):

        s1 = quadrilateral(self.v2,self.v1,self.v4,self.v3,self.color) # FIXED
        s2 = quadrilateral(self.v8,self.v7,self.v3,self.v4,self.color) # FIXED

        s3 = quadrilateral(self.v7,self.v8,self.v5,self.v6,self.color) # FIXED
        s4 = quadrilateral(self.v6,self.v5,self.v1,self.v2,self.color) # FIXED

        s5 = quadrilateral(self.v7,self.v6,self.v2,self.v3,self.color) # FIXED
        s6 = quadrilateral(self.v5,self.v8,self.v4,self.v1,self.color) # FIXED

        self.vertices = [self.v1,
                         self.v2,
                         self.v3,
                         self.v4,
                         self.v5,
                         self.v6,
                         self.v7,
                         self.v8,
                         ]

        self.edges = [
            [self.v1,self.v2],
            [self.v2,self.v3],
            [self.v3,self.v4],
            [self.v4,self.v1],
            [self.v4,self.v8],
            [self.v3,self.v7],
            [self.v7,self.v8],
            [self.v2,self.v6],
            [self.v1,self.v5],
            [self.v5,self.v6],
            [self.v7,self.v6],
            [self.v5,self.v8]
        ]
        self.faces = [s1,s2,s3,s4,s5,s6]

        for side in self.faces:
            self.triangles.extend(side.triangles)




    def draw_faces(self,window,camera_position,orthogonal=False):
        #This overrides the inherited draw_faces function
        for face in self.faces:
            new_color = get_color(face.triangles[0],camera_position)
            for triangle in face.triangles:
                if triangle.is_visible(camera_position):
                    a = triangle.get_projected_coordinates(camera_position)
                    pygame.draw.polygon(window,
                                        new_color,
                                        a)
