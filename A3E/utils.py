def convert_result(x, y, width, height):
    """
    The output of all the other functions take the center of the screen as the origin.
    This function converts it back such that the top left corner is the origin.
    """

    return x + width / 2, y + height / 2


def project_3d_point_to_2d(x, y, z, width, height, d=1):

    """x,y,z are the coordinates for the point on a 3d plane.
    d is the distance between the focal point and the screen.
    TODO: This is currently a very basic perspective projection. It is derived using similar triangles
    TODO: Division by zero error is raised after the triangle is no longer in view
    """
    new_x = d*x/z
    new_y = d*y/z

    return convert_result(new_x, new_y, width, height)


def project_triangle(v1, v2, v3, width, height, d=1):
    """TODO: Write a docstring here."""

    return (project_3d_point_to_2d(v1[0], v1[1], v1[2], width, height, d),
            project_3d_point_to_2d(v2[0], v2[1], v2[2], width, height, d),
            project_3d_point_to_2d(v3[0], v3[1], v3[2], width, height, d))


def generate_cube_vertices(x_center, y_center, z_center, side_length):
    """TODO"""
    pass
