import pygame
from numpy import full
from typing import Sequence
import pygame
import pyximport
pyximport.install()
from cythonized_graphics.pixels import clear_z_buffer, efficient_clear_z_buffer, fill_screen

class WindowManager:
    #This class implements a z buffer

    def __init__(self,pixels, height: int, width:int, background_color: Sequence = None) :
        if background_color is None:
            background_color = (0,0,0)


        self.width = width
        self.height = height
        
        self.pixel_depths = full((self.width, self.height),float("inf"))

        self.pixels = pixels
        print(self.width)
        print(self.height)


    

    def draw_pixel(self, x: int, y: int, color:Sequence, depth:int = 0):
        # print(len(self.pixel_depths),len(self.pixel_depths[0]), x, y)
        if self.pixel_depths[x][y]<=depth:
            return 
        self.pixel_depths[x][y] = depth
        self.pixels[x][y][0] = color[0]
        self.pixels[x][y][1] = color[1]
        self.pixels[x][y][2] = color[2]
    def clear_z_buffer(self, background):
        clear_z_buffer(self.pixel_depths,float("inf"))




    @staticmethod
    def sort_v_by_ascending(arr: Sequence) -> Sequence:
        # basically an insertions sort
        # This method uses as little operations as possible
        # This function also changes the array in place, so be very carefull when using this function

        if (arr[1][1] < arr[0][1]):
            arr[0], arr[1] = arr[1], arr[0]

        if (arr[2][1] < arr[1][1]):
            arr[1], arr[2] = arr[2], arr[1]
            if (arr[1][1] < arr[0][1]):
                arr[1], arr[0] = arr[0], arr[1]

        return arr


    def draw_horizontal_line(self, window, color, distance:int, start_position: Sequence, end_position: Sequence, ):

        y = round(start_position[1])
        if y<0 or y>self.height:
            return 

        
        if start_position[0]<end_position[0]:
            new_s_x, new_e_x = round(start_position[0]), round(end_position[0])
        else:
            new_e_x, new_s_x = round(start_position[0]), round(end_position[0])
        
        if new_s_x<0:
            new_s_x = 0
        while new_s_x<new_e_x+1 and new_s_x<self.width:
            
            self.draw_pixel(new_s_x, y, color, distance)

            new_s_x += 1


    def flat_fill_top(self, surface, distance: int, v1: Sequence, v2: Sequence, v3: Sequence, color:Sequence = (255,255,255)):
        
        """
        v1, v2: bottom left and bottom right corners of the triangle (in any order)
        v3: top of triangle

        Assumes that the y values of v1 and v2 are the same. 
        This function uses the fact that increasing y by one increases x by the inverse slope of the line:
        y=mx+b
        (y-b)/m = x
        (y+1-b)/m = x + (1/m)
        Using this fact, we loop through all the y values given, and find the respective x values"""

        try:
            inverse_m1 = (v1[0]-v3[0]) / (v1[1] - v3[1])
            inverse_m2 = (v2[0]-v3[0]) / (v2[1] - v3[1])
        except ZeroDivisionError:
            return 

        current_x_1 = v1[0]
        current_x_2 = v2[0]
        current_y = v1[1]

        while current_y>v3[1]:
            self.draw_horizontal_line(surface,color,distance, (current_x_1, current_y), (current_x_2, current_y))
            current_y -= 1
            current_x_1 -= inverse_m1
            current_x_2 -= inverse_m2

        
    def flat_fill_bottom(self, surface, distance:int, v1: Sequence, v2: Sequence, v3: Sequence, color:Sequence = (255,255,255)):
        """Goes through the pixels of a triangle which has a side paralel to the x axis.
        Assumes that the line v1-v2 is parralel to the x axis and v3[1]>v1[1]"""
        inverse_m2 = (v2[0]-v3[0]) / (v2[1] - v3[1])
        inverse_m1 = (v1[0]-v3[0]) / (v1[1] - v3[1])

        current_x_1 = v1[0]
        current_x_2 = v2[0]
        current_y = v1[1]

        while current_y<v3[1]:
            self.draw_horizontal_line(surface,color,distance, (current_x_1, current_y), (current_x_2, current_y))
            current_y += 1
            current_x_1 += inverse_m1
            current_x_2 += inverse_m2
    
    @staticmethod
    def roundv(v):
        return [
            round(v[0]), round(v[1])
        ]
    def draw_triangle(self,surface, v1: Sequence,v2: Sequence,v3: Sequence,
                            distance:float,
                            color = (255,255,255)) -> None: 
        


        """ This function rasterizes the given triangle and draws each pixel onto the screen.
        The pixel is not drawn if there is anything else in that pixel which is closer.
        The algorithm basically splits the triangle into 2 triangles where each triangle has one side parallel to the x axis."""

        v1, v2, v3 = self.sort_v_by_ascending([self.roundv(v1),self.roundv(v2),self.roundv(v3)])
        #Now that they have been sorted, v1.y<v2.y<v3.y


        #If there are any horizontal edges, we treat them as special cases:
        if v3[1] == v2[1]:
            self.flat_fill_top(surface,distance, v2, v3 , v1, color)
            return 
        
        if v1[1] == v2[1]:
            self.flat_fill_bottom(surface,distance, v1, v2, v3, color)
            return 

        # General case is derived by splitting the triangle into two different triangles by drawing a horizontal 
        # line from v2 to the line v1-v3
        y = v2[1]


        try:
            m =  (v1[1]-v3[1]) / (v1[0]-v3[0])
            b = v1[1] - (v1[0]*m)
            v4 = [ (y-b)/m, y ]
        except ZeroDivisionError:
            v4 = [v1[0], y]

        self.flat_fill_top(surface,distance, v2,v4,v1, color)
        self.flat_fill_bottom(surface,distance, v2,v4,v3, color)

        


        
            


if __name__ == '__main__':
    from random import randint
    from time import perf_counter
    pygame.init()

    window = pygame.display.set_mode((500,500), pygame.RESIZABLE)
    screen = WindowManager(window,500,500)

    # for i in range(2):
    #     a = [randint(0,500),randint(0,500)]
    #     b = [randint(0,500),randint(0,500)]
    #     c = [randint(0,500),randint(0,500)]
    #     col = [randint(0,255),randint(0,255),randint(0,255),]
    #     screen.draw_triangle(window, a,b,c, 0, 0, 0, col)
    screen.draw_triangle(window,[250, 312], [225, 337], [250, 338] ,0, (255,0,0))
    #    screen.draw_triangle(window,[375, 203], [242, 272], [332, 346],0, 0, 0, (255,0,0))

    # pygame.draw.polygon(window, (255,0,255), [[250, 312], [225, 337], [250, 338]])
    
    pygame.display.update()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                break
        
