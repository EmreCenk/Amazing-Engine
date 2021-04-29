
from pygame.gfxdraw import pixel

def update_pixels(window, to_loop):
    cdef int i = 0
    for i in range(len(to_loop)):
        pixel(window, to_loop[i][0], to_loop[i][1] ,(255,255,255))
        
