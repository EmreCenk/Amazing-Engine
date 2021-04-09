
import pygame


class big_boi_3d:

    def __init__(self,  width_window , height_window):


        self.height = height_window
        self.width = width_window

    def start_engine(self):
        pygame.init()
        screen_size = (self.height,self.width)
        self.window = pygame.display.set_mode(screen_size, pygame.RESIZABLE)

    def init_loop(self, functions_to_call):

        self.start_engine()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    break
                if event.type == pygame.VIDEORESIZE:
                    self.height = pygame.display.get_window_size()
                    self.width, self.height = height

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        pygame.quit()
                        quit()

            for func in functions_to_call:
                func()


            pygame.display.update()



