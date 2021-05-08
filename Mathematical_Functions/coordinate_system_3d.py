
from math import radians, sqrt, cos, sin
from constants import conversion, excluded


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


IN, LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 4, 8

def classify_point(xa, ya, xmax, ymax, xmin = 0, ymin = 0):
    # Finds which sector a given point is:
    # 1010 | 1000 | 1001 |
    # ___________________
    # 0010 | 0000 | 0001 |
    # ___________________
    # 0110 | 0100 | 0101 |
    # ___________________
    #first digit: check if outside top boundary
    #Second boolean: check if outside bottom boundary
    #third boolean: check if outside  left boundary
    #Fourth boolean: check if outside right boundary


    point = IN  # default is inside

    if xa < xmin:
        point |= LEFT

    elif xa > xmax:
        point |= RIGHT

    if ya < ymin:
        point |= BOTTOM  # bitwise OR

    elif ya > ymax:
        point |= TOP

    return point

def clip_line(
    v1, v2, xmax, ymax, xmin = 0,  ymin = 0, ):
    #An implementation of the cohen-sutherland algorithm
    #Takes two points v1, v2 and clips them so that they will fit in a rectangle with
    #boundaries at xmax, ymax, xmin and ymin

    x1, y1 = v1
    x2, y2 = v2



    clip_class_1 = classify_point(x1, y1, xmax, ymax, xmin, ymin)
    clip_class_2 = classify_point(x2, y2, xmax, ymax, xmin, ymin)


    while (clip_class_1 | clip_class_2) != 0:  # stop if both points are in

        # if line trivially outside , reject
        if (clip_class_1 & clip_class_2) != 0:  # bitwise AND &
            return None, None, None, None

        # non-trivial case, at least one point outside window

        opt = clip_class_1 or clip_class_2  # take first non-zero point
        if opt & TOP:  # & is a bitwise and
            x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
            y = ymax


        elif opt & BOTTOM:
            x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
            y = ymin


        elif opt & RIGHT:
            y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
            x = xmax


        elif opt & LEFT:
            y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
            x = xmin


        else:
            raise ValueError('Wow buddy you really screwed up lol')

        if opt == clip_class_1:
            x1, y1 = x, y
            clip_class_1 = classify_point(x1, y1, xmax, ymax, xmin, ymin)
            # if dbglvl>1: print('checking k1: ' + str(x) + ',' + str(y) + '    ' + str(k1))
        elif opt == clip_class_2:
            # if dbglvl>1: print('checking k2: ' + str(x) + ',' + str(y) + '    ' + str(k2))
            x2, y2 = x, y
            clip_class_2 = classify_point(x2, y2, xmax, ymax, xmin, ymin)

    return x1, y1, x2, y2

def clip_2d_triangle(triangle_vertices, width, height):

    a = clip_line(triangle_vertices[0], triangle_vertices[1], width, height)
    b = clip_line(triangle_vertices[1], triangle_vertices[2], width, height)
    c = clip_line(triangle_vertices[2], triangle_vertices[0], width, height)

    final = []
    if a[0] != None:
        final.append((a[0],a[1]))

        final.append((a[2],a[3]))


    if b[0] != None:
        final.append((b[0],b[1]))

        final.append((b[2],b[3]))

    if c[0] != None:
        final.append((c[0],c[1]))

        final.append((c[2],c[3]))
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


    a,b,c = [560,50], [200,600],[400,320]
    while 1:
        a[1]+=-4
        b[1]+=-4
        c[1]+=-4

        a[0]+=4
        b[0]+=4
        c[0]+=4

        pygame.draw.line(window, "green", (0, 0), (0, 500))
        pygame.draw.line(window, "green", (0, 0), (500, 0))
        pygame.draw.line(window, "green", (500, 500), (0, 500))
        pygame.draw.line(window, "green", (500, 500), (500, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                break



        new = clip_2d_triangle([a,b,c],500,500)

        print(len(new))
        if len(new)>2:
            print("alpha:",new)
            pygame.draw.polygon(window, (255,255,0), new)

        pygame.time.delay(50)
        pygame.display.update()
        window.fill((0,0,0))

