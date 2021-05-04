

print("I AM HERE")

from math import tan,radians
from cython_coordinate_system_3d import translate

def convert_result(x,y,s_width,s_height):
    return [x+s_width/2,y+s_height/2]


def efficient_perspective_projection(translated_point,screen_width,screen_height):
    
    cdef int d=500
    return convert_result(d*translated_point[0]/translated_point[2],
                          d*translated_point[1]/translated_point[2],
                          screen_width,
                          screen_height)

def efficient_triangle_projection(translated_triangle_vertices, screen_width, screen_height):
    return (efficient_perspective_projection(translated_triangle_vertices[0],screen_width,screen_height,),
            efficient_perspective_projection(translated_triangle_vertices[1],screen_width,screen_height,),
            efficient_perspective_projection(translated_triangle_vertices[2],screen_width,screen_height,),
            )


def project_3d_point_to_2d(point,screen_width,screen_height,camera_position,orthogonal=False):

    if orthogonal: # 1 op
        return convert_result(
            point[0],point[1],screen_width,screen_height
        )

    cdef double[3] new_point = translate(point,camera_position) # 3 operations


    cdef int d=500

    #projected coordinates: ( 6 operations )
    return convert_result(d*new_point[0]/new_point[2],
                          d*new_point[1]/new_point[2],
                          screen_width,
                          screen_height)
                          
def project_triangle(v1,v2,v3,screen_width,screen_height,camera_position):

    return (project_3d_point_to_2d(v1,screen_width,screen_height,camera_position),
            project_3d_point_to_2d(v2,screen_width,screen_height,camera_position),
            project_3d_point_to_2d(v3,screen_width,screen_height,camera_position))
