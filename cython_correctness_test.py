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


Manager = WindowManager(pix, 500, 500, colman)
s = perf_counter()

for i in range(500):
    if i%2 == 0 :
        Manager.draw_horizontal_line(window, np.array([255,255,255],dtype=np.ubyte),0,
        np.array([0,i], dtype=np.double),
        np.array([500,i],  dtype=np.double))



print("function time:",perf_counter()-s,f"({1/(perf_counter()-s)} fps)")

pygame.display.update()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            break
        