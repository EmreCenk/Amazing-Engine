import pyximport
pyximport.install()

from cythonized_graphics.pixels import update_pixels as cython_update

from performance_tests import update_pixels
from time import perf_counter
import pygame
pygame.init()
window = pygame.display.set_mode((500,500), pygame.RESIZABLE)

s = perf_counter()
window.fill((255,255,255))
print(perf_counter()-s)




while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            break

    pygame.display.update()