
from math import radians, sqrt, cos, sin
from constants import conversion,excluded


def rotate(vertex, axis, angle, radian_input = False):
    if not radian_input:
        angle = radians(angle)


    if axis in conversion:
        axis = conversion[axis]


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

def dot_product(v1,v2):
    return (
        v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
    )

def magnitude(v):
    return sqrt(
        v[0]**2 + v[1]**2 + v[2]**2
    )

def normalize(v):
    mag = magnitude(v)

    return [
        v[1]/mag,v[2]/mag,v[3]/mag
                          ]
def get_normal(triangle_vertices):
    #We get the cross product of two vertices of the triangle to find the normal

    a = triangle_vertices[0]
    b = triangle_vertices[1]

    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    ]

def is_it_visible(light_source, triangle_vertices):
    normal = get_normal(triangle_vertices)
