import pyximport
pyximport.install()
from cythonized_graphics.managing_pixels import WindowManager
import pygame
from time import perf_counter
import numpy as np

pygame.init()
window = pygame.display.set_mode((500,500), pygame.RESIZABLE)

pix = pygame.surfarray.pixels3d(window)
colman = np.array([255,255,255],dtype=np.ubyte)

s = perf_counter()
Manager = WindowManager(pix, 500, 500, colman)
print("init:",perf_counter()-s)
s=perf_counter()
Manager.clear_screen(colman)
print("fill:",perf_counter()-s,f"({1/(perf_counter()-s)} fps)")


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            break
        