
import pygame
from pygame import gfxdraw

from typing import Sequence

class WindowManager:
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

        return arr


    def flat_fill_top(self, surface, v1: Sequence, v2: Sequence, v3: Sequence, color:Sequence = (255,255,255)):
        
        """
        v1: bottom right corner of triangle
        v2: bottom left corner
        v3: top of triangle

        Assumes that the y values of v1 and v2 are the same. 
        This function uses the fact that increasing y by one increases x by the inverse slope of the line:
        y=mx+b
        (y-b)/m = x
        (y+1-b)/m = x + (1/m)
        Using this fact, we loop through all the y values given, and find the respective x values"""

        inverse_m2 = (v2[0]-v3[0]) / (v2[1] - v3[1])
        inverse_m1 = (v1[0]-v3[0]) / (v1[1] - v3[1])

        current_x_1 = v1[0]
        current_x_2 = v2[0]
        current_y = v1[1]

        while current_y>=v3[1]:
            pygame.draw.line(surface,color, (current_x_1, current_y), (current_x_2, current_y))
            current_y -= 1
            current_x_1 -= inverse_m1
            current_x_2 -= inverse_m2

        
        
 
    def draw_triangle(self, v1: Sequence,v2: Sequence,v3: Sequence,
                            v1_distance: float, v2_distance: float, v3_distance: float):


        """ This function rasterizes the given triangle and draws each pixel onto the screen.
        The pixel is not drawn if there is anything else in that pixel which is closer.
        The algorithm basically splits the triangle into 2 triangles where each triangle has one side parallel to the x axis."""


        


if __name__ == '__main__':
    k=0
    from time import perf_counter
    screen = WindowManager(500,500)
    pygame.init()

    window = pygame.display.set_mode((500,500), pygame.RESIZABLE)

    

    #gfxdraw.pixel takes around 0.2 seconds for 250,000 pixels
    #pygame.surfarray.pixels3d takes 0.3 seconds
    #pygame.PixelArray(window) takes 0.096 seconds (~0.1)
    #pygame.draw.circle takes 0.3 seconds

    #with cython pixelarray takes 0.02 seconds


    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                break

        screen.flat_fill_top(window, [300,100],[100,100], [19,19])
        screen.render_all_pixels()
        pygame.display.update()

        pygame.time.delay(100)
        pygame.draw.polygon(window,(255,0,0),points = [[300,100],[100,100], [19,19]] )

