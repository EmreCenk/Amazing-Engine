
from utils.coordinate_system_3d import distance, normalized

def get_color(triangle, light_v, luminosity = 75, rgb_colour = (255, 255, 255), background_color = (0,0,0)):

    # For now, we will compute the distance between the centroid of the triangle and the light source to find the color

    centroid = triangle.get_centroid() # 8+9 = 17 ops

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







