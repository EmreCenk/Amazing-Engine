
from constants import conversion
class camera:
    def __init__(self,x=0,y=0,z=0, x_theta = 0, y_theta = 0, z_theta = 0):

        #TODO: add angles to camera
        self.x=x
        self.y=y
        self.z=z

        self.x_theta =  x_theta
        self.y_theta = y_theta
        self.z_theta = z_theta
        self.position = [self.x, self.y, self.z, self.x_theta, self.y_theta, self.z_theta]

    def move(self,axis,amount):
        if axis in conversion:
            axis = conversion[axis]

        self.position[axis] += amount

    def rotate(self, axis, amount):
        #Same principle as the move function: Find the axis and add to the angle.
        if axis in conversion:
            axis = conversion[axis]

        #Angles are 3 after the index of their respective axis
        self.position[axis+3] += amount

