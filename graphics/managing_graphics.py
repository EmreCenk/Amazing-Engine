import pygame
import graphics.shapes_3d as sh3
from graphics.camera import camera
from graphics.using_obj_files.using_obj_files import obj_mesh
from time import perf_counter

class graphics_manager:

    def __init__(self,  width_window , height_window, delay_time = 100, background_color = (0,0,0)):
        self.delay_time = delay_time
        self.background_color = background_color
        self.height = height_window
        self.width = width_window
        self.camera = camera( z = 20)

    def start_engine(self):
        pygame.init()
        screen_size = (self.height,self.width)
        self.window = pygame.display.set_mode(screen_size, pygame.RESIZABLE)

    def init_loop(self, functions_to_call=None):

        if functions_to_call is None:
            functions_to_call = []

        self.start_engine()

        shift = 0
        side = 5
        v1,v2,v3,v4,v5,v6,v7,v8 = [shift, shift, side], [side, shift, side], [side, shift, shift],[shift, shift, shift],\
        [shift,side, side],[side, side, side],[side,side, shift],[shift, side, shift]

        self.tester_rectangle = sh3.rectangular_prism(v1, v2, v3, v4, v5, v6, v7, v8, color="green"

                                                      )
        #
        # self.tester_rectangle2 = sh3.rectangular_prism(v1, v2, v3, v4, v5, v6, v7, v8, color="white"
        #
        #                                               )
        #
        # self.tester_mesh2 = obj_mesh("using_obj_files/sample_object_files/utah_teapot.obj")
        self.tester_mesh2 = obj_mesh("using_obj_files/sample_object_files/sphere_5_scaled.obj")
        # self.tester_mesh2.move("x",5)
        # self.tester_mesh.move("x",-5)
        power_level = 1
        zpower = 1

        x=0
        total=0
        while x<50:
            x+=1
            s = perf_counter()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    break
                elif event.type == pygame.VIDEORESIZE:
                    self.width, self.height = pygame.display.get_window_size()
                    print(self.width,self.height)

                elif event.type == pygame.MOUSEBUTTONDOWN :
                    if event.button == 4:
                        self.camera.move("z",-zpower)

                    elif event.button == 5:
                        self.camera.move("z",+zpower)

                    # print(self.camera.position)





            # self.tester_rectangle.rotate("x", 1)

            for func in functions_to_call:
                func()


            keys = pygame.key.get_pressed()

            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.camera.move("y",-power_level)

            elif keys[pygame.K_UP] or keys[pygame.K_w]:
                self.camera.move("y",power_level)


            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.camera.move("x",-power_level)

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.camera.move("x",power_level)



            self.tester_mesh2.wireframe_draw(self.window, self.camera.position)

            pygame.display.update()
            self.window.fill(self.background_color)

            time_took_for_frame = perf_counter()-s

            self.proper_delay(time_took_for_frame)

            total += perf_counter()-s





        # AVERAGE TIME IT TAKES TO "wireframe_draw" (perspective projection) UTAH TEAPOT: 0.22753077799999993
        # AVERAGE TIME IT TAKES TO "wireframe_draw" (orthogonal projection) UTAH TEAPOT: 0.155137514

        # AVERAGE TIME IT TAKES TO "wireframe_draw" (perspective projection), delay_time = 0, utah teapot,
        # time per frame: 0.16953308399999995

        # AVERAGE TIME IT TAKES TO "draw_faces" UTAH TEAPOT: 0.2826867440000001, 0.2819358000000001
        # AVERAGE TIME IT TAKES TO "draw_faces" UTAH TEAPOT WITHOUT A SHADING FUNCTION: 0.24425682
        print("AVERAGE:",total/x)

    def proper_delay(self, frame_time):
        if frame_time >= self.delay_time:
            return None

        pygame.time.delay(int(self.delay_time-frame_time*1000)) # multiply by 1000 to convert to milliseconds

if __name__ == '__main__':
    a = graphics_manager(500,500,delay_time=50)
    a.init_loop()