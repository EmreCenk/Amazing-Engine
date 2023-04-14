
from Mathematical_Functions.projecting import project_triangle
import graphics.shapes_2d as shapes_2d

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

        self.test_triangle = shapes_2d.triangle([100,100,100],[200,200,100],[300,300,100])
        self.test_triangle_2 = shapes_2d.triangle([-200,-200,50],[200,200,50],[0,500,50],color="blue")

        self.quad_test = shapes_2d.quadrilateral([200,-200,50], [200,200,50], [0,500,50], [1000,1000,50],
                                                 _color = "green")

        self.test_cube = shapes_2d.shape_2d(color="blue")

        self.test_cube.triangles.extend([
            shapes_2d.quadrilateral.convert_to_triangles(self.test_cube,(0,0,1),(0,0,0),(1,0,0),(1,0,1))
        ])
        s=10
        t=-100


        self.start_engine()

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





            self.test_triangle_2.move("z",-1)
            self.quad_test.move("z",-1)


            self.quad_test.draw(self.window)
            # self.test_triangle_2.draw(self.window)
            # self.test_triangle.draw(self.window)



            for func in functions_to_call:
                func()




            pygame.display.update()

            self.window.fill(self.background_color)



# class cube:
#     def __init__(self, center_x, center_y, center_z, side_length):
#         self.vertices = []
#     def generate_coordinates(self, center_x, center_y, center_z, side_length):


if __name__ == '__main__':
    a = graphics_manager(500,500,delay_time=100)
    a.init_loop()