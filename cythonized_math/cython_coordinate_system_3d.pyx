

# # from math import radians, sqrt, cos, sin
# # from constants import conversion, excluded


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