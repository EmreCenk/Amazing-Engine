
from constants import conversion
class camera:
    def __init__(self,x=0,y=0,z=0):

        #TODO: add angles to camera
        self.x=x
        self.y=y
        self.z=z

        self.position = [self.x,self.y,self.z]
    def move(self,axis,amount):
        if axis in conversion:
            axis = conversion[axis]

        self.position[axis] += amount

