import pyximport
pyximport.install()
from cythonized_graphics.managing_pixels import WindowManager
from graphics.managing_window_pixels import WindowManager as pymanag
import pygame
from time import perf_counter
import numpy as np


pygame.init()
window = pygame.display.set_mode((500,500), pygame.RESIZABLE)

pix = pygame.surfarray.pixels3d(window)
colman = np.array([255,255,255],dtype=np.ubyte)


Manager = WindowManager(pix, 500, 500, colman)
s = perf_counter()
a,b,c = np.array([100,100],dtype=np.double), \
    np.array([200,100],dtype=np.double), \
    np.array([50,50],dtype=np.double), 

Manager.flat_fill_top(
    window, 0, a, b, c, colman
)



print("function time:",perf_counter()-s,f"({1/(perf_counter()-s)} fps)")




pygame.display.update()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            break
        