
from Mathematical_Functions.projecting import project_triangle
import graphics.shapes_3d as sh3
import graphics.shapes_2d as sh2
import pygame


class graphics_manager:

    def __init__(self,  width_window , height_window, delay_time = 100, background_color = (0,0,0)):
        self.delay_time = delay_time
        self.background_color = background_color


        self.height = height_window
        self.width = width_window

    def start_engine(self):
        pygame.init()
        screen_size = (self.height,self.width)
        self.window = pygame.display.set_mode(screen_size, pygame.RESIZABLE)

    def init_loop(self, functions_to_call=None):

        if functions_to_call is None:
            functions_to_call = []

        shift = 1
        side = 100
        v1,v2,v3,v4,v5,v6,v7,v8 = [shift, shift, side], [side, shift, side], [side, shift, shift],[shift, shift, shift],\
        [shift,side, side],[side, side, side],[side,side, shift],[shift, side, shift]


        self.test_rect3 = sh3.rectangular_prism(

            v1,v2,v3,v4,v5,v6,v7,v8
        )

        self.test2d = sh2.quadrilateral(v1,v2,v3,v4,_color="green")

        self.start_engine()
        print(v1,v2,v3,v4,v5,v6,v7,v8)

        while True:
            pygame.time.delay(self.delay_time)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    break
                if event.type == pygame.VIDEORESIZE:
                    self.width, self.height = pygame.display.get_window_size()
                    print(self.width,self.height)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        pygame.quit()
                        quit()








            for func in functions_to_call:
                func()


            self.test2d.move("y",-5)
            self.test2d.draw(self.window)

            self.test_rect3.draw(self.window)

            self.test_rect3.move("y",-5)
            pygame.display.update()

            self.window.fill(self.background_color)



# class cube:
#     def __init__(self, center_x, center_y, center_z, side_length):
#         self.vertices = []
#     def generate_coordinates(self, center_x, center_y, center_z, side_length):


if __name__ == '__main__':
    a = graphics_manager(500,500,delay_time=100)
    a.init_loop()