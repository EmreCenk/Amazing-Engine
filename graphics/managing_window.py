
import pygame
from pygame import gfxdraw

from typing import Sequence

class window_manager:
    #This class implements a z buffer

    def __init__(self, width:int = None, height: int = None) :
        if width is None or height is None:
            self.width, self.height = pygame.display.get_window_size() #Getting the pixel width and height of the curent
            # window
        else:
            self.width, self.height = width, height


        self.pixels = []
        self.changed_pixels = {} #We store the pixels that were changed so that the program doesn't loop through
        # every single pixel when resetting z buffer

        for i in range(self.height):
            current = []
            for j in range(self.width):
                current.append(float("inf")) #set all the pixel values to infinity,

            self.pixels.append(current)


    def clear_z_buffer(self):
        for index in self.changed_pixels:
            self.pixels[index[0]][index[1]] = float("inf") # resets the z value of the pixel

        self.changed_pixels = {}

    def draw_proper_pixel(self, window,  x, y, d, color = (255,255,255)):
        global k
        k+=1
        if self.pixels[x][y]<=d:
            #There is already a pixel that is closer to the camera
            return None

        self.changed_pixels[(x,y)] = color
        self.pixels[x][y] = d


    def render_all_pixels(self):

        for index in self.changed_pixels:
            gfxdraw.pixel(window, index[0], index[1], self.changed_pixels[index])


    def draw_line(self, window, x1, y1, x2, y2, color = (255,255,255)):

        # An implementation of Bresenham's Line algorithm
        # The algorithm basically travels through all integer x coordinates between the two points and finds the
        # corresponding y value by keeping track of the y difference between points

        mn = 2 * (y2 - y1)
        sn = mn - (x2 - x1)

        y = y1
        for x in range(int(x1), int(x2) + 1):
            self.draw_proper_pixel(window, x, y , 0)
            sn += mn
            if sn >= 0:
                y += 1
                sn -= 2 * (x2 - x1)
    def fill_top(self,window, v1, v2, v3):
        inverse_slope_1 = (v3[0] - v1[0]) / (v3[1] - v1[1])
        inverse_slope_2 = (v3[0] - v2[0]) / (v3[1] - v2[1])
        curx1 = v3[0]
        curx2 = v3[0]

        s_line_y = v3[1]
        while s_line_y > v1[1]:

            self.draw_line(window, curx1, s_line_y, curx2, s_line_y)

            curx1 -= inverse_slope_1
            curx2 -= inverse_slope_2
            s_line_y -= 1


    def fill_bottom(self,window, v1,v2,v3):

        invslope1 = (v2[0] - v1[0]) / (v2[1] - v1[1])
        invslope2 = (v3[0] - v1[0]) / (v3[1] - v1[1])
        curx1 = curx2 = v3[0]

        s_line_y = v1
        while s_line_y <= v2[1]:
            self.draw_line(window, curx1, s_line_y, curx2, s_line_y)
            curx1 += invslope1
            curx2 += invslope2

            s_line_y += 1




    @staticmethod
    def sort_v_by_ascending(arr: Sequence) -> None:

        # basically an insertions sort
        # This method uses as little operations as possible
        # 3 operations
        if (arr[1] < arr[0]):
            arr[0], arr[1] = arr[1], arr[0]

        if (arr[2] < arr[1]):
            arr[1], arr[2] = arr[2], arr[1]
            if (arr[1] < arr[0]):
                arr[1], arr[0] = arr[0], arr[1]


    def draw_triangle(self, v1: Sequence,
                            v2: Sequence,
                            v3: Sequence,
                            v1_distance: float, v2_distance: float, v3_distance: float):

        """ This function rasterizes the given triangle and draws each pixel onto the screen.
        The pixel is not drawn if there is anything else in that pixel which is closer.
        The algorithm basically splits the triangle into 2 triangles where each triangle has one side parallel to the x axis."""






if __name__ == '__main__':
    k=0
    from time import perf_counter
    screen = window_manager(500,500)
    pygame.init()

    window = pygame.display.set_mode((500,500), pygame.RESIZABLE)

    #PERFORMANCE TEST:
    
    pixels = pygame.PixelArray(window)
    a=10
    total=0
    for k in range(a):
        s = perf_counter()

        for i in range(500):
            for j in range(500):
                pixels[i][j] = 1000

        total+=perf_counter()-s
                # gfxdraw.pixel(window,i,j,(255,255,255))

    #gfxdraw.pixel takes around 0.2 seconds for 250,000 pixels
    #pygame.surfarray.pixels3d takes 0.3 seconds
    #pygame.PixelArray(window) takes 0.096 seconds (~0.1)
    #pygame.draw.circle takes 0.3 seconds

    #with cython pixelarray takes 0.02 seconds
    screen.render_all_pixels()
    print('on average:',total/a)
    print(k)
    while 1:
        pygame.display.update()


