
def convert_result(x,y,s_width,s_height):
    #the output of all the other functions take the center of the screen as the origin. Here, we convert it back such
# that the top left corner is the origin

    return x+s_width/2,y+s_height/2

def project_3d_point_to_2d(point,screen_width,screen_height,d=1):

    """x,y,z are the coordinates for the point on a 3d plane.
    d is the distance between the focal point and the screen"""


    # This is currently a very basic perspective projection. It is derived using similar triangles
    # At some point the engine will implement quaternions. For now, I will be using 3 coordinates to get some basic
    # functionality
    x=point[0]
    y=point[1]
    z=point[2]
    newx = d*x/z
    newy = d*y/z

    return convert_result(newx,newy,screen_width,screen_height)

def project_triangle(v1,v2,v3,screen_width,screen_height,d=10):

    return (project_3d_point_to_2d(v1[0],v1[1],v1[2],screen_width,screen_height,d),
            project_3d_point_to_2d(v2[0],v2[1],v2[2],screen_width,screen_height,d),
            project_3d_point_to_2d(v3[0],v3[1],v3[2],screen_width,screen_height,d))


def matrix_multiplication(matrix1,matrix2):

    #checking to see if it is possible to multiply the matrices:
    if len(matrix1[0])!=len(matrix2):
        raise ValueError("It is not possible to multiply these matrices. ")

    result = []

    rows1 = len(matrix1)
    # columns1 = len(matrix1[0])


    rows2 = len(matrix2)
    columns2 = len(matrix2[0])


    for i in range(rows1):
        current = []
        for j in range(columns2):
            current.append(0)

        result.append(current)



    for i in range(rows1):

        for j in range(columns2):

            for w in range(rows2):

                result[i][j] += matrix1[i][w] * matrix2[w][j]



    return result





if __name__ == '__main__':
    print(project_3d_point_to_2d(70, -189, 70,500,500))
    # m,mm=[[1,2,3]],[[4,3],[2,5],[6,8]]
    # print(matrix_multiplication(m,mm))