
from Mathematical_Functions.coordinate_system_3d import distance

def get_color(triangle_vertices, light_source, rgb_colour = (255, 255, 255)):


    # For now, we will take the average of how far away the 3 vertices are. In the future, I might make a more complex
    # system where we blend the distances and the shading

    #TODO: add shadows
    #TODO: blend the shades, don't make it a homogeneous color

    v1, v2, v3 = triangle_vertices[0], triangle_vertices[1], triangle_vertices[2]

    t1 = distance(v1, light_source)
    t2 = distance(v2, light_source)
    t3 = distance(v3, light_source)

    some_coefficient = 10 # Might use this to calibrate the sytem
    average = (t1 + t2 + t3) / 3


    return (
        some_coefficient * (rgb_colour[0] / average),
        some_coefficient * (rgb_colour[1] / average),
        some_coefficient * (rgb_colour[2] / average),

    )


if __name__ == '__main__':
    print(get_color(
        [[100,100,100], [100,100,100], [100,100,100]],
        [0,0,0],
    ))




