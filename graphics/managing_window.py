
import pygame
class window_manager:
    #This class implements a z buffer

    def __init__(self):
        self.width, self.height = pygame.display.get_window_size() #Getting the pixel width and height of the curent
        # window

        self.pixels = []

        for i in range(self.width):
            current = []
            for j in range(self.height):
                current.append(float("inf")) #set all the pixel values to infinity,

            self.pixels.append(current)


    def clear_z_buffer(self):
        for i in range(len(self.pixels)):
            for j in range(len(self.pixels[0])):
                self.pixels[i][j] = float("inf") # resets the z value of the pixel


