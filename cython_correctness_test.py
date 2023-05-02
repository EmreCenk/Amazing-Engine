import pyximport
pyximport.install()
from cythonized_graphics.managing_pixels import WindowManager
from graphics.managing_window_pixels import WindowManager as pymanag
import pygame
from time import perf_counter
import numpy as np
from random import randint
pygame.init()
window = pygame.display.set_mode((500,500), pygame.RESIZABLE)
pix = pygame.surfarray.pixels3d(window)
colman = np.array([255,255,255],dtype=np.ubyte)
total=0
Manager = WindowManager(pix, 500, 500, colman)
manpy = pymanag(window,500,500)

a,b,c = np.array([100,100],dtype=np.double), \
    np.array([200,100],dtype=np.double), \
    np.array([50,50],dtype=np.double), 

# s = perf_counter()

# Manager.flat_fill_top(
#     window, 0, a, b, c, colman
# )

# print("function time:",perf_counter()-s,f"({1/(perf_counter()-s)} fps)")
k = 10
numtimes = 6300
for i in range(1,numtimes):
    if i%10==0:
        k*=-1
    s=perf_counter()
    Manager.draw_triangle(
        window, a, b, c, 0, colman
    )    
    total+=perf_counter()-s
    # a[0]+=k
    # a[1]+=k

    # b[0]+=k
    # b[1]+=k

    # c[0]+=k
    # c[1]+=k

print("TOTAL:",total,f"({1/total} fps)")
print("AVERAGE:",total/numtimes)
print("AREA:", -(a[0]-b[0])*(b[1]-c[1])/2)
pygame.display.update()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            break
        