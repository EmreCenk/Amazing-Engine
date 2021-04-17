from alternative_graphics.shapes_2d import quadrilateral,shape
from Mathematical_Functions.coordinate_system_3d import distance

class shape_3d(shape):

    # Surprisingly, every function in the 2d shape class is actually really usefull for 3d shapes. Perhaps I should
    # rename the shape_2d class to just shape in the future? (shape_3d should start branching off of shape_2d soon
    # enough)

    def __init__(self,color):
        super().__init__(color)




class rectangular_prism(shape_3d):

    def __init__(self,v1, v2, v3, v4, v5, v6, v7, v8, color="white",fill_bool=False):
        """Label the first 4 points starting with the top left corner of a given side, and moving in a clockwise
        direction. Label the last 4 points by picking the vertex that has not been labeled which is also connected to vertex 1.
        From there, keep labeling in a clockwise direction. """
        super().__init__(color)
        self.generate_triangles(v1, v2, v3, v4, v5, v6, v7, v8)



    def generate_triangles(self,v1, v2, v3, v4, v5, v6, v7, v8):

        s1 = quadrilateral(list(v1),list(v2),list(v3),list(v4),self.color)
        s2 = quadrilateral(list(v8),list(v7),list(v3),list(v4),self.color,)

        s3 = quadrilateral(list(v5),list(v6),list(v7),list(v8),self.color)
        s4 = quadrilateral(list(v5),list(v6),list(v2),list(v1),self.color)

        s5 = quadrilateral(list(v2),list(v3),list(v7),list(v6),self.color)
        s6 = quadrilateral(list(v5),list(v8),list(v1),list(v4),self.color)

        self.faces = [s1,s2,s3,s4,s5,s6]

        for side in self.faces:
            self.triangles.extend(side.triangles)



    def define_center(self):
        #We find the center of this cube by taking the average of all coordinates

        x=0
        y=0
        z=0
        for s in self.vertices:
           x+=s[0]
           y+=s[1]
           z+=s[2]


        return x/8,y/8,z/8
