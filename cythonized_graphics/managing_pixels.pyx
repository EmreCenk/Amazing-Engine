import pygame
from pygame import Surface
from numpy import full, ndarray


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

        

    
    cpdef clear_screen(self, unsigned char[:] new_color):
        cdef int i = 0
        cdef int j = 0
        cdef int N = self.pixel_depths.shape[0]
        cdef int K = self.pixel_depths.shape[1]
        for i in range(N):
            for j in range(K):
                self.draw_pixel(i, j, new_color, 0)

        print(self.pixels)