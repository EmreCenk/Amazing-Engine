
from Mathematical_Functions.projecting import project_triangle


import pygame


class graphics_manager:

    def __init__(self,  width_window , height_window, background_color = (0,0,0)):
        self.background_color = background_color


        self.height = height_window
        self.width = width_window

    def start_engine(self):
        pygame.init()
        screen_size = (self.height,self.width)
        self.window = pygame.display.set_mode(screen_size, pygame.RESIZABLE)

    def init_loop(self,delay_time = 100, functions_to_call=None):

        if functions_to_call is None:
            functions_to_call = []

        self.test_triangle = triangle([100,100,100],[200,200,100],[300,300,100])
        self.test_triangle_2 = triangle([1000,1000,100],[2000,2000,100],[6000,3000,100])
        self.start_engine()

        while True:
            pygame.time.delay(delay_time)
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


            self.test_triangle.vertex1[0] -= 1
            self.test_triangle.vertex2[0] -= 1
            self.test_triangle.vertex3[0] -= 1
            new_vertices = project_triangle(self.test_triangle.vertex1,
                                   self.test_triangle.vertex2,
                                   self.test_triangle.vertex3,
                                    self.width,
                                    self.height

                                            )

            self.test_triangle_2.vertex1[2] -= 1
            self.test_triangle_2.vertex2[2] -= 1
            self.test_triangle_2.vertex3[2] -= 1
            new_vertices2 = project_triangle(self.test_triangle_2.vertex1,
                                   self.test_triangle_2.vertex2,
                                   self.test_triangle_2.vertex3,
                                             self.width,
                                             self.height
                                             )
            pygame.draw.polygon(self.window, points = new_vertices,color = "white")
            pygame.draw.polygon(self.window, points = new_vertices2,color = "blue")
            print(new_vertices)
            for func in functions_to_call:
                func()




            pygame.display.update()

            self.window.fill(self.background_color)

class triangle:
    def __init__(self,vertex1,vertex2,vertex3):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex3 = vertex3

if __name__ == '__main__':
    a = graphics_manager(500,500)
    a.init_loop()