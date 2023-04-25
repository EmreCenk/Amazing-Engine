
from Mathematical_Functions.coordinate_system_3d import distance, normalized

def get_color(triangle, light_source, rgb_colour = (255, 255, 255)):
    # 38 operations

    # For now, we will compute the distance between the centroid of the triangle and the light source to find the color

    #TODO: add shadows
    #TODO: blend the shades, don't make it a homogeneous color

    centroid = normalized(triangle.get_centroid()) # 8+9 = 17 ops
    dist = distance(centroid, normalized(light_source)) # 8+8=16 operations
    dist = 1 - (dist / 2) # 2 operations



    # 3 operations:
    return (
        rgb_colour[0] * dist,
        rgb_colour[1] * dist,
        rgb_colour[2] * dist,

    )





