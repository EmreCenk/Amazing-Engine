

from math import radians, sqrt, cos, sin

cdef dict conversion = {"x":0,
              "y":1,
              "z":2,
              }

cdef dict excluded = {
    "x":[1, 2],
    "y":[0, 2],
    "z":[0, 1],
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
}


cpdef translate(point, camera_position):

    
    cdef double x = point[0]
    cdef double y = point[1]
    cdef double z = point[2]

    cdef double cx = camera_position[0]
    cdef double cy = camera_position[1]
    cdef double d = camera_position[2]

    x+=cx
    y-=cy
    z-=d

    return x,y,z

def translate_triangle_vertices(triangle_vertices, camera_position):
    #has 9 operations
    return [
        translate(triangle_vertices[0],camera_position),
        translate(triangle_vertices[1],camera_position),
        translate(triangle_vertices[2],camera_position)
    ]


def rotate(vertex, axis, angle, radian_input = False):
    if not radian_input:
        angle *= 0.0174533 #I might have to define a new variable here since the input angle is int 
        # but angle is reassigned to a float

    if axis in conversion:
        axis = conversion[axis]


    cdef int[2] ex = excluded[axis]
    cdef int a1 = ex[0]
    cdef int a2 = ex[1]

    cdef double newa1 = vertex[a1]*cos(angle) + vertex[a2]*sin(angle)
    cdef double newa2 = vertex[a2]*cos(angle) - vertex[a1]*sin(angle)

    
    vertex[a1] = newa1
    vertex[a2] = newa2

    return vertex


def distance(p1,p2):
    return sqrt(
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2 +
        (p1[2] - p2[2]) ** 2
    )

cpdef dot_product(v1,v2):
    # 5 operations
    return (
        v1[0]*v2[0] +
        v1[1]*v2[1] +
        v1[2]*v2[2]
    )


cpdef magnitude(v):
    # 5 operations
    return sqrt(
        v[0]**2 + v[1]**2 + v[2]**2
    )


cpdef normalized(v):
    cdef double mag = magnitude(v)
    
    if mag == 0:
        return [0,0,0]
    
    
    return [
        v[0]/mag,v[1]/mag,v[2]/mag
    ]
    

cpdef normalize_triangle_vertices(triangle_vertices):
    return [
        normalized(triangle_vertices[0]),
        normalized(triangle_vertices[1]),
        normalized(triangle_vertices[2])
    ]

cpdef subtract_vectors(v1,v2):
    return [
        v1[0] - v2[0],
        v1[1] - v2[1],
        v1[2] - v2[2],
    ]


cpdef get_lines(triangle_vertices):
    return [
        subtract_vectors(triangle_vertices[2], triangle_vertices[0]),
        subtract_vectors(triangle_vertices[1], triangle_vertices[0])
    ]


cpdef get_normal(triangle_vertices):

    cdef double[2][3] lines = get_lines(triangle_vertices)
    cdef double[3] a = lines[0]
    cdef double[3] b = lines[1]

    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    ] 



def is_visible(translated_triangle_vertices, normalized_camera_position):

    cdef double[3][3] new_triangle_vertices = normalize_triangle_vertices(translated_triangle_vertices) 
    cdef double[3] normal = get_normal(new_triangle_vertices)
    cdef double r = dot_product(normal,normalized_camera_position)

    if r>0:
        return False

    return True
