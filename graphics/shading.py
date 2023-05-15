
from utils.coordinate_system_3d import distance, normalized
from constants import conversion

def get_color(triangle, light_v, luminosity = 75, rgb_colour = (255, 255, 255), background_color = (0,0,0)):

    # For now, we will compute the distance between the centroid of the triangle and the light source to find the color

    # centroid = triangle.get_centroid() # 8+9 = 17 ops

    a, b = 0, 1
    centroid = [
        (triangle.vertices[a][0] + triangle.vertices[b][0]) / 2,
        (triangle.vertices[a][1] + triangle.vertices[b][1]) / 2,
        (triangle.vertices[a][2] + triangle.vertices[b][2]) / 2,
    ]
    dist = distance(centroid, light_v) # 8 operations
    if dist>luminosity:
        return background_color


    dist = 1 - (dist/luminosity)


    # 3 operations:

    return (
        rgb_colour[0] * dist,
        rgb_colour[1] * dist,
        rgb_colour[2] * dist,

    )





class Light:
    def __init__(self, x, y, z, luminosity):
        self.x = x
        self.y = y
        self.z = z
        self.luminosity = luminosity

        self.position = [self.x,self.y,self.z]

    def move(self,axis,amount):
        if axis in conversion:
            axis = conversion[axis]

        self.position[axis] += amount

    def adjust_luminosity(self, new_luminosity):
        self.luminosity = new_luminosity





