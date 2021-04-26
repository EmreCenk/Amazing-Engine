
import pygame
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
        self.changed_pixels = set() #We store the pixels that were changed so that the program doesn't loop through
        # every single pixel when resetting z buffer

        for i in range(self.height):
            current = []
            for j in range(self.width):
                current.append(float("inf")) #set all the pixel values to infinity,

            self.pixels.append(current)


    def clear_z_buffer(self):
        for index in self.changed_pixels:
            self.pixels[index[0]][index[1]] = float("inf") # resets the z value of the pixel

    @staticmethod
    def draw_line(x1, y1, x2, y2):
        # An implementation of Bresenham's Line algorithm
        # The algorithm basically travels through all integer x coordinates between the two points and finds the
        # corresponding y value by keeping track of the y difference between points

        mn = 2 * (y2 - y1)
        sn = mn - (x2 - x1)

        y = y1
        for x in range(x1, x2 + 1):

            # DRAW TO THE PIXEL (X,Y)


            # Add slope to increment angle formed
            sn = sn + mn

            # Slope error reached limit, time to
            # increment y and update slope error.
            if (sn >= 0):
                y = y + 1
                sn = sn - 2 * (x2 - x1)
    def fill_top(self,v1,v2,v3):
        pass

    def fill_bottom(self,v1,v2,v3):
        pass


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


    def draw_triangle(self, v1: Sequence[float,float,float],
                            v2: Sequence[float,float,float],
                            v3: Sequence[float,float,float],
                            v1_distance: float, v2_distance: float, v3_distance: float):

        """ This function rasterizes the given triangle and draws each pixel onto the screen.
        The pixel is not drawn if there is anything else in that pixel which is closer.
        The algorithm basically splits the triangle into 2 triangles where each triangle has one side parallel to the x axis."""






if __name__ == '__main__':
    screen = window_manager(1920,1080)
    screen.clear_z_buffer()

