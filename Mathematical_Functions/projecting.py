


def project_3d_point_to_2d(x,y,z,d=1):

    """x,y,z are the coordinates for the point on a 3d plane.
    d is the distance between the focal point and the screen"""


    #This is currently a very basic perspective projection. It is derived using similar triangles

    newx = d*x/z
    newy = d*y/z

    return (newx,newy)

def project_triangle(v1,v2,v3,d=1):

    return (project_3d_point_to_2d(v1[0],v1[1],v1[2],d),
            project_3d_point_to_2d(v2[0],v2[1],v2[2],d),
            project_3d_point_to_2d(v3[0],v3[1],v3[2],d))
