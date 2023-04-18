
from constants import conversion
class camera:
    def __init__(self):

        #TODO: add angles to camera
        self.x=0
        self.y=0
        self.z=0

        self.coordinates = [self.x,self.y,self.z]
    def move(self,axis,amount):
        if axis in conversion:
            axis = conversion[axis]

        self.coordinates[axis] += amount

