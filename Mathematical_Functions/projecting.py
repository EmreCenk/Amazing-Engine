
def convert_result(x,y,s_width,s_height):
    #the output of all the other functions take the center of the screen as the origin. Here, we convert it back such
# that the top left corner is the origin

    return x+s_width/2,y+s_height/2

def project_3d_point_to_2d(x,y,z,screen_width,screen_height,d=1):

    """x,y,z are the coordinates for the point on a 3d plane.
    d is the distance between the focal point and the screen"""


    #This is currently a very basic perspective projection. It is derived using similar triangles

    newx = d*x/z
    newy = d*y/z

    return convert_result(newx,newy,screen_width,screen_height)

def project_triangle(v1,v2,v3,screen_width,screen_height,d=1):

    return (project_3d_point_to_2d(v1[0],v1[1],v1[2],screen_width,screen_height,d),
            project_3d_point_to_2d(v2[0],v2[1],v2[2],screen_width,screen_height,d),
            project_3d_point_to_2d(v3[0],v3[1],v3[2],screen_width,screen_height,d))

def generate_cube_vertices(x_center,y_center,z_center,side_length):
    pass
