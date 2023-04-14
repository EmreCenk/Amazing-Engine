
from graphics.shapes_2d import quadrilateral,shape_2d
from Mathematical_Functions.coordinate_system_3d import distance

class shape_3d(shape_2d):

    #Surprısınglyö every functıon ın a 2d shape ıs actually really usefull for 3d shapes. Perhaps I should rename the
    # shape_2d class to just shape in the future? (shape_3d should start branching off of shape_2d soon enough)

    def __init__(self,color,fill_bool):
        super().__init__(color,fill_bool)




class rectangular_prism(shape_3d):

    def __init__(self,v1, v2, v3, v4, v5, v6, v7, v8, color="white",fill_bool=False):
        super().__init__(color,fill_bool)
        self.generate_triangles(v1, v2, v3, v4, v5, v6, v7, v8)
        self.vertices= (v1, v2, v3, v4, v5, v6, v7, v8)


    def generate_triangles(self,v1, v2, v3, v4, v5, v6, v7, v8):
        self.quadrilaterals = []

        s1 = quadrilateral(v1,v2,v3,v4,self.color,self.fill)
        s2 = quadrilateral(v3,v4,v8,v7,self.color,self.fill)

        s3 = quadrilateral(v5,v6,v7,v8,self.color,self.fill)
        s4 = quadrilateral(v5,v6,v2,v1,self.color,self.fill)

        s5 = quadrilateral(v2,v3,v7,v6,self.color,self.fill)
        s6 = quadrilateral(v1,v4,v8,v5,self.color,self.fill)

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














