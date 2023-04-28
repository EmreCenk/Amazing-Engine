

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

cpdef translate_triangle_vertices(triangle_vertices, camera_position):
    #has 9 operations
    return [
        translate(triangle_vertices[0],camera_position),
        translate(triangle_vertices[1],camera_position),
        translate(triangle_vertices[2],camera_position)
    ]


cpdef rotate(vertex, axis, angle, radian_input = False):
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