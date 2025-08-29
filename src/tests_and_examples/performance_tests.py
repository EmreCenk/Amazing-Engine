from time import perf_counter
import pygame
from time import perf_counter
import pyximport
pyximport.install()
from cythonized_graphics.pixels import clear_z_buffer, efficient_clear_z_buffer, fill_screen

pygame.init()
window = pygame.display.set_mode((500,500), pygame.RESIZABLE)

pix = pygame.surfarray.pixels3d(window)
s = perf_counter()
fill_screen(pix, (255,255,255))
print(perf_counter()-s)
pygame.display.update()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            break
        
