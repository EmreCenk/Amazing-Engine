import pygame
from pygame import Surface
from numpy import full

cdef class WindowManager:
    #This class implements a z buffer

    cdef int width
    cdef int height
    cdef int[:, :] pixel_depths
    cdef float[:, :, :] pixels

    def __init__(self, float[:, :, :] _pixels, int _height, int _width, int[:] background_color) :


        self.width = _width
        self.height = _height
        self.pixel_depths = full((self.width, self.height),float("inf"))

        self.pixels = _pixels
        