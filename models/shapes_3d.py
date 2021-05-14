from models.shapes_2d import quadrilateral, shape, triangle
from utils.coordinate_system_3d import rotate_around_point, normalized, is_visible
import pygame
from constants import conversion
from utils.shading import get_color
from math import sqrt


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
        self.max_x = max(self.vertices, key = lambda tri: tri[0])[0]
        self.min_x = min(self.vertices, key = lambda tri: tri[0])[0]

        self.max_y = max(self.vertices, key = lambda tri: tri[1])[1]
        self.min_y = min(self.vertices, key = lambda tri: tri[1])[1]

        self.max_z = max(self.vertices, key = lambda tri: tri[2])[2]
        self.min_z = min(self.vertices, key = lambda tri: tri[2])[2]

        #Taking the average of the upper and lower bounds to find the midpoint for all
        #dimensions:

        self.center = [
            (self.max_x + self.min_x) / 2,
            (self.max_y + self.min_y) / 2,
            (self.max_z + self.min_z) / 2,

        ]



    def move(self,axis,amount):
        #Overriding the move function to also move the center along with everything else:
        if axis in conversion:
            axis = conversion[axis]

        #This method updates both the self.v values and the self.vertices values
        for vert in self.vertices:
            vert[axis]+=amount

        self.center[axis] += amount

    def rotate(self, axis, angle, radian_input = False):
        #Overriding the rotate function to also rotate the center along with everything else:

        for vert in self.vertices:
            rotate_around_point((0,0,0), vert, axis, angle, radian_input)

        # rotate_around_point(self.center,self.center, axis, angle)


#We have to import obj_mesh here since obj_mesh imports the shape_3d class. We need to initialize shape_3d before
# trying to import it from obj_mesh
from models.using_obj_files.using_obj_files import obj_mesh

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
        normalized_camera = normalized(camera_position)
        for face in self.faces:
            new_color = get_color(face.triangles[0],normalized_camera, rgb_colour=self.color)
            for triangle in face.triangles:
                translated_vert = triangle.get_translated(camera_position)

                if is_visible(translated_vert, normalized_camera):
                    a = triangle.get_projected_coordinates(camera_position)
                    pygame.draw.polygon(window,
                                        new_color,
                                        a)


class Cube(rectangular_prism):

    def __init__(self, center_coordinates, side_length, color):
        self.center = center_coordinates
        shift = 0
        v1, v2, v3, v4, v5, v6, v7, v8 = [shift, shift, side_length],\
                                         [side_length, shift, side_length],\
                                         [side_length, shift, shift],\
                                         [shift, shift,shift], \
                                         [shift, side_length, side_length],\
                                         [side_length, side_length, side_length],\
                                         [side_length, side_length, shift],\
                                         [shift, side_length, shift]


        super().__init__(v1, v2,v3 ,v4 ,v5 ,v6 ,v7 ,v8, color)

        self.move("x", center_coordinates[0])
        self.move("y", center_coordinates[1])
        self.move("z", center_coordinates[2])

class Pyramid(shape_3d):

    def __init__(self, center_coordinates, side_length, color):
        super().__init__(color)

        self.height = side_length * sqrt(3)/2

        # top vertex
        self.v1 = list(center_coordinates)
        self.v1[1] += self.height/2

        #base vertices:
        self.v2 = list(center_coordinates)
        self.v3 = list(center_coordinates)
        self.v4 = list(center_coordinates)


        self.v2[1] -= self.height / 2
        self.v3[1] -= self.height / 2
        self.v4[1] -= self.height / 2

        self.v2[2] -= self.height / 2
        self.v3[2] += self.height / 2
        self.v4[2] += self.height / 2


        self.v3[0] -= side_length / 2
        self.v4[0] += side_length / 2

        self.triangles.append(triangle(self.v1, self.v3, self.v4, color = self.color))

        self.triangles.append(triangle(self.v1, self.v4, self.v2, color = self.color))

        self.triangles.append(triangle(self.v1, self.v2, self.v3, color = self.color))
        self.triangles.append(triangle(self.v2, self.v3, self.v4, color = self.color))

        self.center = center_coordinates

        self.vertices = [self.v1, self.v2, self.v3, self.v4 ]


class Sphere(obj_mesh):

    def __init__(self, center, radius, color):
        """This class takes a preset sphere .obj file and scales it according to radius size.
        The initial model sphere has a radius of 5."""
        super().__init__("models/using_obj_files/sample_object_files/sphere_5_scaled.obj", color)

        ratio = radius / 5
        for i in range(len(self.vertices)):
            self.vertices[i][0] *= ratio
            self.vertices[i][1] *= ratio
            self.vertices[i][2] *= ratio

        #moving to the desired position
        self.move("x", center[0])
        self.move("y", center[1])
        self.move("z", center[2])

        self.center = center

