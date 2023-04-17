
from math import radians, sqrt, cos, sin
from constants import conversion,excluded


def rotateX3D(node,theta):

    sinTheta = sin(theta)
    cosTheta = cos(theta)


    y = node[1]
    z = node[2]
    node[1] = y * cosTheta - z * sinTheta
    node[2] = z * cosTheta + y * sinTheta
    return node
def rotate(vertex, axis, angle, radian_input = False):
    if not radian_input:
        angle = radians(angle)


    if axis in conversion:
        axis = conversion[axis]

    if axis==0:
        print("XXXX")
        return rotateX3D(vertex,angle)
    #Getting the other 2 axes:
    a1, a2 = excluded[axis]

    newa1 = vertex[a1]*cos(angle) + vertex[a2]*sin(angle)
    newa2 = vertex[a2]*cos(angle) - vertex[a1]*sin(angle)

    vertex[a1] = newa1
    vertex[a2] = newa2

    return vertex


def distance(p1,p2):


    # Let p1 = (x,y,z) and p2 = (xx,yy,zz)
    # The distance between these two points is: sqrt ( (x-xx)^2 + (y-yy)^2 + (z-zz)^2 )

    return sqrt(
        (p1[0]-p2[0])**2 +
        (p1[1] - p2[1]) ** 2 +
        (p1[2] - p2[2]) ** 2
    )




