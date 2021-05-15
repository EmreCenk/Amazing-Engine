
from constants import conversion
class Camera:
    def __init__(self, models_3d, x=0,y=0,z=0, x_theta = 0, y_theta = 0, z_theta = 0):

        #TODO: add angles to Camera
        self.x=x
        self.y=y
        self.z=z

        self.x_theta =  x_theta
        self.y_theta = y_theta
        self.z_theta = z_theta
        self.position = [self.x, self.y, self.z, self.x_theta, self.y_theta, self.z_theta]
        self.models_3d = models_3d
        self.translate_all_models(self.x, self.y, self.z)


    def translate_all_models(self, x, y, z):
        for i in range(len(self.models_3d)):
            self.models_3d[i].shift("x", -x)
            self.models_3d[i].shift("y", -y)
            self.models_3d[i].shift("z", -z)

    def shift(self,axis,amount):
        if axis in conversion:
            axis = conversion[axis]

        # self.position[axis] += amount
        for i in range(len(self.models_3d)):
            self.models_3d[i].shift(axis, -amount)



    def rotate(self, axis, amount):
        #Same principle as the shift function: Find the axis and add to the angle.
        if axis in conversion:
            axis = conversion[axis]

        #Angles are 3 after the index of their respective axis
        # self.position[axis+3] += amount

        for i in range(len(self.models_3d)):
            self.models_3d[i].rotate_around_point((0,0,0), axis, -amount)
            self.models_3d[i].rotations[axis] += -amount
