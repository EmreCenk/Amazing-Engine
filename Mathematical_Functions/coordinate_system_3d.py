
from math import radians, sqrt, cos, sin
from constants import conversion, excluded

def translate(point,camera_position):
    x=point[0]
    y=point[1]
    z=point[2]

    cx=camera_position[0]
    cy = camera_position[1]
    d=camera_position[2]

    x+=cx
    y-=cy
    z-=d

    return x,y,z

def translate_triangle_vertices(triangle_vertices,camera_position):
    return [
        translate(triangle_vertices[0],camera_position),
        translate(triangle_vertices[1],camera_position),
        translate(triangle_vertices[2],camera_position)
    ]

def rotate(vertex, axis, angle, radian_input = False):
    if not radian_input:
        angle = radians(angle)


    if axis in conversion:
        axis = conversion[axis]


    #Getting the other 2 axes:
    a1, a2 = excluded[axis]

    newa1 = vertex[a1]*cos(angle) + vertex[a2]*sin(angle)
    newa2 = vertex[a2]*cos(angle) - vertex[a1]*sin(angle)


    #we update the given values directly:
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
        v1[0]*v2[0] +
        v1[1]*v2[1] +
        v1[2]*v2[2]
    )

def magnitude(v):
    return sqrt(
        v[0]**2 + v[1]**2 + v[2]**2
    )

def normalized(v):
    mag = magnitude(v)
    if mag==0:
        mag=0.001
    return [
        v[0]/mag,v[1]/mag,v[2]/mag
    ]

def normalize_triangle_vertices(triangle_vertices):
    return [
        normalized(triangle_vertices[0]),
        normalized(triangle_vertices[1]),
        normalized(triangle_vertices[2])
    ]
def subtract_vectors(v1,v2):
    return [
        v1[0] - v2[0],
        v1[1] - v2[1],
        v1[2] - v2[2],
    ]

def get_lines(triangle_vertices):
    return [
        subtract_vectors(triangle_vertices[1],triangle_vertices[0]),
        subtract_vectors(triangle_vertices[2], triangle_vertices[0])
    ]


def get_normal(triangle_vertices):
    #We get the cross product of two vertices of the triangle to find the normal

    a, b = get_lines(triangle_vertices)

    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    ]


def is_visible(triangle_vertices, camera_position):
    triangle_vertices = translate_triangle_vertices(triangle_vertices,camera_position)
    triangle_vertices = normalize_triangle_vertices(triangle_vertices)

    normal = get_normal(triangle_vertices)

    if normal[2]<0:
        return True

    return False




