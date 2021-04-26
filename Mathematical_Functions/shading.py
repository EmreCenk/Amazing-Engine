
from Mathematical_Functions.coordinate_system_3d import distance, normalized

def get_color(triangle, normalized_light_source, rgb_colour = (255, 255, 255)):
    # 30 operations

    # For now, we will compute the distance between the centroid of the triangle and the light source to find the color

    #TODO: add shadows
    #TODO: blend the shades, don't make it a homogeneous color

    centroid = normalized(triangle.get_centroid()) # 8+9 = 17 ops
    dist = distance(centroid, normalized_light_source) # 8 operations
    dist = 1 - (dist / 2) # 2 operations



    # 3 operations:
    return (
        rgb_colour[0] * dist,
        rgb_colour[1] * dist,
        rgb_colour[2] * dist,

    )





