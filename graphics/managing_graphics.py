from graphics.camera import camera
from models.using_obj_files.using_obj_files import obj_mesh
import models.shapes_3d as sh3
from time import perf_counter
import numpy as np
from a_ideas_on_hold.managing_window_pixels import WindowManager
from utils.coordinate_system_3d import *
import pygame

class graphics_manager:

    #TODO: add clipping for triangles
    #TODO: add camera angles

    def __init__(self,  width_window , height_window, delay_time = 100, background_color = (0,0,0)):
        self.delay_time = delay_time
        self.background_color = np.array(background_color,dtype=np.ubyte)
        self.height = height_window
        self.width = width_window
        self.delta_time = 1 #inital value. It gets updated every frame
        self.start_engine()

        #For some reason the following line needs to be there to track the centers of 3d objects
        self.width, self.height = pygame.display.get_window_size() 

        pix = pygame.surfarray.pixels3d(self.window)
        self.Window_Manager = WindowManager(pix, self.height, self.width, self.background_color)
        self.models_3d = []
        self.camera = camera(self.models_3d, z = 20)


        
    def start_engine(self):
        pygame.init()
        screen_size = (self.width, self.height)
        self.window = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
        # pygame.mouse.set_visible(False)



    def render_frame(self):
        #TODO: Refactor the followıng code so that we don't translate and rotate the objects relative to the camera
        #in every single frame

        camera_position = self.camera.position
        normalized_camera = normalized(camera_position)
        to_draw = []
        for model in self.models_3d:
            for triangle in model.triangles:




                if is_visible(triangle.vertices,normalized_camera):
                    to_draw.append(
                        [triangle, distance(triangle.get_centroid(),camera_position),triangle.vertices]
                    )

        to_draw.sort(key = lambda tri: tri[1], reverse=True)

        for liste in to_draw:
            liste[0].draw(self.window, self.camera.position, liste[2])


        # for model in self.models_3d:
        #     pygame.draw.circle(
        #         self.window,
        #     (255,255,255),
        #     project_3d_point_to_2d(model.center,self.width,self.height,self.camera.position),
        #     radius = 3)

    def add_model(self, obj_3d):
        self.models_3d.append(
                            obj_3d,
                            )

        obj_3d.move("x", -self.camera.x)
        obj_3d.move("y", -self.camera.y)
        obj_3d.move("z", -self.camera.z)
        self.camera.models_3d = self.models_3d # making sure the camera also has access to our list
        
    def init_loop(self, functions_to_call=None):

        if functions_to_call is None:
            functions_to_call = []

        shift = 0
        side = 5
        v1,v2,v3,v4,v5,v6,v7,v8 = [shift, shift, side], [side, shift, side], [side, shift, shift],[shift, shift, shift],\
        [shift,side, side],[side, side, side],[side,side, shift],[shift, side, shift]

        # self.tester_rectangle = sh3.rectangular_prism(v1, v2, v3, v4, v5, v6, v7, v8, color=(255,255,0)

        #                                               )
        # self.tester_rectangle = obj_mesh("graphics/using_obj_files/sample_object_files/sphere_5_scaled.obj", color = (255,0,0))
        #
        #
        # self.tester_rectangle = obj_mesh("models_3d/using_obj_files/sample_object_files/sphere_5_scaled.obj",
        #                                 color = (0,255,255))
        self.tester_rectangle = sh3.rectangular_prism(v1, v2, v3, v4, v5, v6, v7, v8, color = (255,255,255))


        K1,K2,K3,K4,K5,K6,K7,K8 = [shift, shift, side], [side, shift, side], [side, shift, shift],[shift, shift, shift],\
        [shift,side, side],[side, side, side],[side,side, shift],[shift, side, shift]


        self.tester_rectangle2 = sh3.rectangular_prism(K1,K2,K3,K4,K5,K6,K7,K8, color = (0,255,255))

        self.add_model(self.tester_rectangle)
        self.add_model(self.tester_rectangle2)
        p_original = 10
        p_z_original = 30

        x=0
        total=0

        while x<100:
            x+=1
            power_level = p_original * self.delta_time
            zpower = p_z_original * self.delta_time

            s = perf_counter()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    break
                elif event.type == pygame.VIDEORESIZE:
                    # self.Window_Manager.width, self.Window_Manager.height = self.width, self.height = pygame.display.get_window_size()
                    self.width, self.height = pygame.display.get_window_size()


                elif event.type == pygame.MOUSEBUTTONDOWN :
                    if event.button == 4:
                        self.camera.move("z",-zpower)

                    elif event.button == 5:
                        self.camera.move("z",+zpower)

                    # print(self.camera.position)





            # self.tester_rectangle.rotate("x", 1)

            for func in functions_to_call:
                func()

            # xr, yr = pygame.mouse.get_rel()
            #
            # dsd = 0.2
            # # self.camera.rotate("x",yr*dsd)
            # self.camera.rotate("y",xr*dsd)


            #
            keys = pygame.key.get_pressed()

            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.camera.move("y",-power_level)

            elif keys[pygame.K_UP] or keys[pygame.K_w]:
                self.camera.move("y",power_level)


            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.camera.move("x",power_level)

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.camera.move("x",-power_level)


            power_level += self.delta_time*10
            if keys[pygame.K_k]:
                self.camera.rotate("x", power_level)

            elif keys[pygame.K_i]:
                self.camera.rotate("x", -power_level)


            if keys[pygame.K_j]:
                self.camera.rotate("y",-power_level)

            if keys[pygame.K_l]:
                self.camera.rotate("y",+power_level)



            if keys[pygame.K_SPACE]:
                self.tester_rectangle.move("x", self.delta_time*10)

            # self.tester_mesh2.rotate("y",10*self.delta_time)
            # self.tester_rectangle.rotate("y",10*self.delta_time)
            # self.tester_mesh2.draw_faces(self.window, self.camera.position)
            self.render_frame()


            pygame.display.update()
            self.window.fill(self.background_color)

            time_took_for_frame = perf_counter()-s

            self.proper_delay(time_took_for_frame)

            self.delta_time = perf_counter()-s

            total += self.delta_time






        # AVERAGE TIME IT TAKES TO "wireframe_draw" (perspective projection) UTAH TEAPOT: 0.22753077799999993
        # AVERAGE TIME IT TAKES TO "wireframe_draw" (orthogonal projection) UTAH TEAPOT: 0.155137514

        # AVERAGE TIME IT TAKES TO "wireframe_draw" (perspective projection), delay_time = 0, utah teapot,
        # time per frame: 0.16953308399999995

        # AVERAGE TIME IT TAKES TO "draw_faces" UTAH TEAPOT: 0.2826867440000001, 0.2819358000000001
        # AVERAGE TIME IT TAKES TO "draw_faces" UTAH TEAPOT WITHOUT A SHADING FUNCTION: 0.24425682

        # AVERAGE "draw_faces" when laptop is charging : 0.23835497399999997

        #AFTER OPTIMIZATIONS 'draw_faces' TIME: 0.196687804
        #When plugged in: 0.12054579799999997

        #When I run the code from vscode, the time went down to 0.06948835800000003 (~0.07 seconds per frame)

        #With cython and vscode, the time went down to 0.045847264999999984 seconds

        print(f"Average time between frames: {total/x} ({1/(total/x)} fps)")

    def proper_delay(self, frame_time):
        if frame_time >= self.delay_time:
            return None

        pygame.time.delay(int(self.delay_time-frame_time*1000)) # multiply by 1000 to convert to milliseconds

