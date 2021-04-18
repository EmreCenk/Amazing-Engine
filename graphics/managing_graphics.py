import pygame
import graphics.shapes_3d as sh3
from graphics.camera import camera

class graphics_manager:

    def __init__(self,  width_window , height_window, delay_time = 100, background_color = (0,0,0)):
        self.delay_time = delay_time
        self.background_color = background_color
        self.height = height_window
        self.width = width_window
        self.camera = camera(z=300)

    def start_engine(self):
        pygame.init()
        screen_size = (self.height,self.width)
        self.window = pygame.display.set_mode(screen_size, pygame.RESIZABLE)

    def init_loop(self, functions_to_call=None):

        if functions_to_call is None:
            functions_to_call = []

        self.start_engine()
        s=200


        shift = 0
        side = 100
        v1,v2,v3,v4,v5,v6,v7,v8 = [shift, shift, side], [side, shift, side], [side, shift, shift],[shift, shift, shift],\
        [shift,side, side],[side, side, side],[side,side, shift],[shift, side, shift]

        self.tester_rectangle = sh3.rectangular_prism(v1, v2, v3, v4, v5, v6, v7, v8, color="green"

                                                      )

        self.tester_rectangle2 = sh3.rectangular_prism(v1, v2, v3, v4, v5, v6, v7, v8, color="white"

                                                      )
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






            # self.tester_rectangle.rotate("x", 1)

            for func in functions_to_call:
                func()


            keys = pygame.key.get_pressed()

            power_level=10
            if keys[pygame.K_DOWN]:
                self.camera.move("y",-power_level)

            if keys[pygame.K_UP]:
                self.camera.move("y",power_level)


            if keys[pygame.K_LEFT]:
                self.camera.move("x",-power_level)

            if keys[pygame.K_RIGHT]:
                self.camera.move("x",power_level)
            print(self.camera.position)
            # self.tester_rectangle.rotate("z", 10)
            self.tester_rectangle.rotate("y", 10)
            self.tester_rectangle.wireframe_draw(self.window, self.camera.position,orthogonal=False)

            pygame.display.update()
            self.window.fill(self.background_color)




# class cube:
#     def __init__(self, center_x, center_y, center_z, side_length):
#         self.vertices = []
#     def generate_coordinates(self, center_x, center_y, center_z, side_length):


if __name__ == '__main__':
    a = graphics_manager(500,500,delay_time=50)
    a.init_loop()