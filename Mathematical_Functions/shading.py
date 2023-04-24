
from Mathematical_Functions.coordinate_system_3d import distance, normalized

def get_color(triangle, light_source, rgb_colour = (255, 255, 255)):


    # For now, we will compute the distance between the centroid of the triangle and the light source to find the color

    #TODO: add shadows
    #TODO: blend the shades, don't make it a homogeneous color

    centroid = normalized(triangle.get_centroid())
    dist = distance(centroid, normalized(light_source))
    dist = 1 - (dist / 2)

    some_coefficient = 1 # Might use this to calibrate the sytem




    return (
        some_coefficient * (rgb_colour[0] * dist),
        some_coefficient * (rgb_colour[1] * dist),
        some_coefficient * (rgb_colour[2] * dist),

    )

#
# if __name__ == '__main__':
#     print(get_color(
#         [[100,100,100], [100,100,100], [100,100,100]],
#         [0,0,0],
#     ))




