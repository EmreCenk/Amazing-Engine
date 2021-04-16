

def convert_result(x,y,s_width,s_height):
    #the output of all the other functions take the center of the screen as the origin. Here, we convert it back such
# that the top left corner is the origin

    return x+s_width/2,y+s_height/2

def project_3d_to_2d(x,y,z,screen_width,screen_height,d=1):
    """x,y,z are the coordinates for the point on a 3d plane.
    d is the distance between the focal point and the screen"""


    # This is currently a very basic perspective projection. It is derived using similar triangles
    # At some point the engine will implement quaternions. For now, I will be using 3 coordinates to get some basic
    # functionality
    newx = x*d/z
    newy = y*d/z

    return convert_result(newx,newy,screen_width,screen_height)