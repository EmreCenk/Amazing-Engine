

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
