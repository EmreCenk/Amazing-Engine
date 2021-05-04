import pygame
from pygame import Surface
from numpy import full, array, double, ndarray, ubyte

from libc.math cimport round
from pixels import clear_z_buffer, efficient_clear_z_buffer, fill_screen

cdef class WindowManager:
    #This class implements a z buffer

    cdef int width
    cdef int height
    cdef double[:, :] pixel_depths
    cdef unsigned char[:, :, :] pixels

    
    def __init__(self, unsigned char[:, :, :] _pixels, int _width, int _height, unsigned char[:] background_color) :


        self.width = _width
        self.height = _height
        self.pixel_depths = full((self.width, self.height),float("inf"))

        self.pixels = _pixels
        
    cdef void draw_pixel(self, int x, int y, unsigned char[:] color, int depth):
        try:
            if self.pixel_depths[x][y]<=depth:
                return 
            self.pixel_depths[x][y] = depth
            self.pixels[x][y][0] = color[0]
            self.pixels[x][y][1] = color[1]
            self.pixels[x][y][2] = color[2]
        except Exception as E:
            print(x,y,color,depth,self.pixels.shape)
            print("oh no:",E)
            pygame.quit()
            quit()

    cpdef clear_z_buffer(self,):
        clear_z_buffer(self.pixel_depths,float("inf"))
    

    cdef void sort_v_by_ascending(self, double arr[3][3]):
        # basically a very efficient insertion sort
        # This method uses as little operations as possible (3 operations)
        # This function also changes the array in place, so be very carefull when using this function
        if (arr[1][1] < arr[0][1]):
            arr[0], arr[1] = arr[1], arr[0]

        if (arr[2][1] < arr[1][1]):
            arr[1], arr[2] = arr[2], arr[1]
            if (arr[1][1] < arr[0][1]):
                arr[1], arr[0] = arr[0], arr[1]



    cpdef void draw_horizontal_line(self, window, unsigned char[:] color, int distance, double[:] start_position, double[:] end_position ):


        cdef double y
        cdef double new_e_x
        cdef double new_s_x
        y = round(start_position[1])
        if y<0 or y>=self.height:
            return 

        
        #Check to see which one is on the left:
        #The while loop loops from left to right (new_s_x is starting position, new_e_x is ending position)

        if start_position[0]<end_position[0]:
            new_s_x = round(start_position[0])
            new_e_x = round(end_position[0])
        else:
            new_e_x = round(start_position[0])
            new_s_x = round(end_position[0])
        
        if new_s_x<0:
            new_s_x = 0
        while new_s_x<new_e_x and new_s_x<self.width:
            
            self.draw_pixel(int(new_s_x), int(y), color, distance)

            new_s_x += 1

    cpdef void flat_fill_top(self, surface, int distance, double[:] v1, double[:] v2, double[:] v3, unsigned char[:] color):
    
        
        """
        v1, v2: bottom left and bottom right corners of the triangle (in any order)
        v3: top vertex of triangle
        
        This is a helper method for the "draw_triangle" method. It is not meant to be used standalone

        Assumes that the y values of v1 and v2 are the same. 
        This function uses the fact that increasing y by one increases x by the inverse slope of the line:
        y=mx+b
        (y-b)/m = x
        (y+1-b)/m = x + (1/m)
        Using this fact, we loop through all the y values given, and find the respective x values"""
        
        cdef double inverse_m1, inverse_m2, current_x_1, current_x_2, current_y
        
        cdef double initial[2]
        cdef double final[2]

        if v1[1] == v3[1] or v2[1] == v3[1]:
            return 
        

        inverse_m1 = (v1[0]-v3[0]) / (v1[1] - v3[1])
        inverse_m2 = (v2[0]-v3[0]) / (v2[1] - v3[1])

        current_x_1 = v1[0]
        current_x_2 = v2[0]
        current_y = v1[1]

        
        while current_y>v3[1]:
            initial[0] = current_x_1
            initial[1] = current_y
            final[0] = current_x_2
            final[1] = current_y

            self.draw_horizontal_line(surface,color,distance, initial, final)
            current_y -= 1
            current_x_1 -= inverse_m1
            current_x_2 -= inverse_m2


    cpdef void flat_fill_bottom(self, surface, int distance, double[:] v1, double[:] v2, double[:] v3, unsigned char[:] color):
        """Goes through the pixels of a triangle which has a side paralel to the x axis.
        Assumes that the line v1-v2 is parralel to the x axis and v3[1]>v1[1]"""

                
        cdef double inverse_m1, inverse_m2, current_x_1, current_x_2, current_y
        
        cdef double initial[2]
        cdef double final[2]

        inverse_m2 = (v2[0]-v3[0]) / (v2[1] - v3[1])
        inverse_m1 = (v1[0]-v3[0]) / (v1[1] - v3[1])

        current_x_1 = v1[0]
        current_x_2 = v2[0]
        current_y = v1[1]

        while current_y<v3[1]:
            initial[0] = current_x_1
            initial[1] = current_y
            final[0] = current_x_2
            final[1] = current_y

            self.draw_horizontal_line(surface,color,distance, initial, final)
            current_y += 1
            current_x_1 += inverse_m1
            current_x_2 += inverse_m2

    cdef roundv(self, double[:] v):
        return [
            round(v[0]), round(v[1])
        ]
    def draw_triangle(self,surface, double[:] v1, double[:] v2, double[:] v3,
                            int distance,
                            unsigned char[:] color): 
        


        """ This function rasterizes the given triangle and draws each pixel onto the screen.
        The pixel is not drawn if there is anything else in that pixel which is closer.
        The algorithm basically splits the triangle into 2 triangles where each triangle has one side parallel to the x axis."""

        cdef double[3][2] temporary
        cdef double[2] v4
        cdef double m,y,b
        temporary[0][0] = v1[0]
        temporary[0][1] = v1[1]



        temporary[1][0] = v2[0]
        temporary[1][1] = v2[1]


        temporary[2][0] = v3[0]
        temporary[2][1] = v3[1]

        self.sort_v_by_ascending(temporary)
        #Now that they have been sorted, v1.y<v2.y<v3.y
        v1 = temporary[0]
        v2 = temporary[1]
        v3 = temporary[2]

        #If there are any horizontal edges, we treat them as special cases:
        if v3[1] == v2[1]:
            self.flat_fill_top(surface,distance, v2, v3 , v1, color)
            return 
        
        if v1[1] == v2[1]:
            self.flat_fill_bottom(surface,distance, v1, v2, v3, color)
            return 

        # General case is derived by splitting the triangle into two different triangles by drawing a horizontal 
        # line from v2 to the line v1-v3
        y = v2[1]


        if v1[0] == v3[0] or v1[1] == v3[1]: #to avoid zerodivisionerror
            v4[0] = v1[0]        
        else:
            m =  (v1[1]-v3[1]) / (v1[0]-v3[0])
            b = v1[1] - (v1[0]*m)
            v4[0] = (y-b)/m

        v4[1] = y 
            

        self.flat_fill_top(surface,distance, v2,v4,v1, color)
        self.flat_fill_bottom(surface,distance, v2,v4,v3, color)
