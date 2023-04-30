from time import perf_counter
import pygame
from time import perf_counter
pygame.init()
window = pygame.display.set_mode((500,500), pygame.RESIZABLE)

pix = pygame.surfarray.pixels3d(window)
s = perf_counter()
for i in range(500):
    for j in range(500):
        pix[i][j] = (255,255,255)

print(perf_counter()-s)
pygame.display.update()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            break
        
