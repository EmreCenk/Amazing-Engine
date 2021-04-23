
from Mathematical_Functions.coordinate_system_3d import distance

def get_color(triangle, light_source, rgb_colour = (255, 255, 255)):


    # For now, we will compute the distance between the centroid of the triangle and the light source to find the color

    #TODO: add shadows
    #TODO: blend the shades, don't make it a homogeneous color

    centroid = triangle.get_centroid()
    dist = distance(centroid, light_source)
    some_coefficient = 200 # Might use this to calibrate the sytem



    return (
        some_coefficient * (rgb_colour[0] / dist),
        some_coefficient * (rgb_colour[1] / dist),
        some_coefficient * (rgb_colour[2] / dist),

    )

#
# if __name__ == '__main__':
#     print(get_color(
#         [[100,100,100], [100,100,100], [100,100,100]],
#         [0,0,0],
#     ))




