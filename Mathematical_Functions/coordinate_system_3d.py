
from math import radians, sqrt, cos, sin
from constants import conversion, excluded
import pygame

def translate(point,camera_position):

    #Has 3 operations
    x=point[0]
    y=point[1]
    z=point[2]

    cx=camera_position[0]
    cy = camera_position[1]
    d=camera_position[2]

    x+=cx
    y-=cy
    z-=d

    return [x,y,z]

def translate_triangle_vertices(triangle_vertices,camera_position):
    #has 9 operations
    return [
        translate(triangle_vertices[0],camera_position),
        translate(triangle_vertices[1],camera_position),
        translate(triangle_vertices[2],camera_position),
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
    # 8 operations

    # Let p1 = (x,y,z) and p2 = (xx,yy,zz)
    # The distance between these two points is: sqrt ( (x-xx)^2 + (y-yy)^2 + (z-zz)^2 )

    return sqrt(
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2 +
        (p1[2] - p2[2]) ** 2
    )

def dot_product(v1,v2):
    # 5 operations
    return (
        v1[0]*v2[0] +
        v1[1]*v2[1] +
        v1[2]*v2[2]
    )

def magnitude(v):
    # 5 operations
    return sqrt(
        v[0]**2 + v[1]**2 + v[2]**2
    )

def normalized(v):
    # 8 operations

    mag = magnitude(v) # 5 ops
    try:
        return [
            v[0]/mag,v[1]/mag,v[2]/mag
        ]
    except ZeroDivisionError:
        return [0,0,0]

def normalize_triangle_vertices(triangle_vertices):
    #24 operations
    return [
        normalized(triangle_vertices[0]),
        normalized(triangle_vertices[1]),
        normalized(triangle_vertices[2])
    ]
def subtract_vectors(v1,v2):
    # 3 operations
    return [
        v1[0] - v2[0],
        v1[1] - v2[1],
        v1[2] - v2[2],
    ]

def get_lines(triangle_vertices):
    # 6 operations
    return [
        subtract_vectors(triangle_vertices[2], triangle_vertices[0]),
        subtract_vectors(triangle_vertices[1], triangle_vertices[0])
    ]


def get_normal(triangle_vertices):
    # 15 operations
    #We get the cross product of two vertices of the triangle to find the normal

    a, b = get_lines(triangle_vertices) # 6 operations
    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    ] # 9 operations



def is_visible(translated_triangle_vertices, normalized_camera_position):
    #45 operations


    new_triangle_vertices = normalize_triangle_vertices(translated_triangle_vertices) # 24 operations

    normal = get_normal(new_triangle_vertices) # 15 operations



    if dot_product(normal,normalized_camera_position)>0: #6 operations
        return False

    return True



##################cython version of the above code exists#######################################

def classify_point(x,y,width,height):
    # Finds which sector a given point is:
    # 1010 | 1000 | 1001 |
    # ___________________
    # 0010 | 0000 | 0001 |
    # ___________________
    # 0110 | 0100 | 0101 |
    # ___________________
    #first digit: check if inside top boundary
    #Second boolean: check if inside bottom boundary
    #third boolean: check if inside  left boundary
    #Fourth boolean: check if inside right boundary

    top = 1
    bottom = 1
    left = 1
    right = 1

    if y>0:
        top = 0
    if y<height:
        bottom = 0

    if x<width:
        right = 0

    if x>0:
        left = 0

    return top, bottom, left, right


def clip_line(line_coordinates, width, height):
    x1, y1 = line_coordinates[0]
    x2, y2 = line_coordinates[1]

    clas_p1 = classify_point(x1, y1, width, height)
    clas_p2 = classify_point(x2, y2, width, height)


    #Checking for trivial cases:
    if clas_p1 == clas_p2:
        if clas_p1 == (0,0,0,0): #if both are inside, we can leave line as is
            return line_coordinates

        return [] #if both are in the same sector outside of the screen, then no part of the line is inside the screen

    if y1>y2:
        max_y, min_y = y1, y2
    else:
        max_y, min_y = y2, y1
    if x1>x2:
        max_x, min_x = x1, x2
    else:
        max_x, min_x = x2, x1


    new_points = []
    #checking if it intersects with top:
    if max_y>100 and min_y<100:
        # x intercept is found via:x1 + (deltax*y1/deltay)
        new_points.append(
            [ x1 + y1*(x2-x1)/(y2-y1),
              0]
        )

    #checking bottom:
    if max_y>height and min_y<height:
        pass

    #checking left:
    if max_x>0 and min_x<0:
        pass

    #checking right:
    if max_x>width and min_x<height:
        pass

    if len(new_points)==0:
        print("ya")
        return line_coordinates

    print("No wtf")
    
def clip_2d_triangle(triangle_vertices, width, height):

    a = clip_line([triangle_vertices[0], triangle_vertices[1]], width, height)
    b = clip_line([triangle_vertices[1], triangle_vertices[2]], width, height)
    c = clip_line([triangle_vertices[0], triangle_vertices[2]], width, height)

    final = []
    for k in a:
        final.append(k)
    for k in b:
        final.append(k)
    for k in c:
        final.append(k)

    return final


def rotate_around_point(point_to_rotate_around, vertex, axis, angle, radian_input=False):
    # Translate the vertex such that point_to_rotate_around is the origin
    vertex[0] -= point_to_rotate_around[0]
    vertex[1] -= point_to_rotate_around[1]
    vertex[2] -= point_to_rotate_around[2]


    rotate(vertex, axis, angle, radian_input)

    # re-translating it to the original place:
    vertex[0] += point_to_rotate_around[0]
    vertex[1] += point_to_rotate_around[1]
    vertex[2] += point_to_rotate_around[2]

if __name__ == "__main__":
    import pygame
    pygame.init()
    window = pygame.display.set_mode((500,500), pygame.RESIZABLE)
    a,b,c = [100,50], [200,100],[400,20]
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                break

        new = clip_2d_triangle([a,b,c],800,800)
        print(new)
        pygame.draw.polygon(window, (255,0,0), new)
        pygame.time.delay(50)
        pygame.display.update()
        window.fill((0,0,0))

