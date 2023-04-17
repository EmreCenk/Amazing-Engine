
from math import radians, sqrt, cos
from constants import conversion,excluded

def rotate(vertex, angle, axis, radian_input = False):
    if not radian_input:
        angle = radians(angle)

    if axis in conversion:
        axis = conversion[axis]

    #Getting the other 2 axes:
    a1, a2 = excluded[axis]

    vertex[a1] = vertex[a1]*cos(angle) - vertex[a2]
    vertex[a2] = vertex[a2]*cos(angle) - vertex[a1]

    return vertex


def distance(p1,p2):


    # Let p1 = (x,y,z) and p2 = (xx,yy,zz)
    # The distance between these two points is: sqrt ( (x-xx)^2 + (y-yy)^2 + (z-zz)^2 )

    return sqrt(
        (p1[0]-p2[0])**2 +
        (p1[1] - p2[1]) ** 2 +
        (p1[2] - p2[2]) ** 2
    )

