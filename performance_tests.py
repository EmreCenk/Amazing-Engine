from time import perf_counter
from pygame.gfxdraw import pixel

def update_pixels(window, A):
    for i in range(len(A)):
        pixel(window, A[i][0], A[i][1] ,(255,255,255))
      
