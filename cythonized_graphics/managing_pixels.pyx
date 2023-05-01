import pygame
from pygame import Surface
from numpy import full, ndarray
from libc.math cimport round

import pyximport
pyximport.install()
from pixels import clear_z_buffer, efficient_clear_z_buffer, fill_screen

cdef class WindowManager:
    #This class implements a z buffer

    cdef int width
    cdef int height
    cdef double[:, :] pixel_depths
    cdef unsigned char[:, :, :] pixels

    ndarray
    def __init__(self, unsigned char[:, :, :] _pixels, int _height, int _width, unsigned char[:] background_color) :


        self.width = _width
        self.height = _height
        self.pixel_depths = full((self.width, self.height),float("inf"))

        self.pixels = _pixels
        
    cdef draw_pixel(self, int x, int y, unsigned char[:] color, int depth):
        if self.pixel_depths[x][y]<depth:
            return 

        self.pixel_depths[x][y] = depth
        self.pixels[x][y][0] = color[0]
        self.pixels[x][y][1] = color[1]
        self.pixels[x][y][2] = color[2]

    cpdef clear_z_buffer(self,):
        self.pixel_depths[0][0] = 0
        clear_z_buffer(self.pixel_depths,float("inf"))
    
    @staticmethod
    def sort_v_by_ascending(arr):
        # basically a very efficient insertion sort
        # This method uses as little operations as possible (3 operations)
        # This function also changes the array in place, so be very carefull when using this function
        if (arr[1][1] < arr[0][1]):
            arr[0], arr[1] = arr[1], arr[0]

        if (arr[2][1] < arr[1][1]):
            arr[1], arr[2] = arr[2], arr[1]
            if (arr[1][1] < arr[0][1]):
                arr[1], arr[0] = arr[0], arr[1]

        return arr

    def draw_horizontal_line(self, window, unsigned char[:] color, int distance, double[:] start_position, double[:] end_position ):


        cdef double y
        cdef double new_e_x
        cdef double new_s_x
        y = round(start_position[1])
        if y<0 or y>self.height:
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
        while new_s_x<new_e_x+1 and new_s_x<self.width:
            
            self.draw_pixel(int(new_s_x), int(y), color, distance)

            new_s_x += 1
