from graphics.camera import Camera
from time import perf_counter
from a_ideas_on_hold.managing_window_pixels import WindowManager
from constants import SOLID, WIREFRAME
from utils.coordinate_system_3d import *
from graphics.shading import Light
import pygame
import sys
import os
import models.shapes_3d as sh3 #DO NOT DELETE. Due to some import dependencies, we need to first import
# this before importing the obj_mesh class
from models.using_obj_files.using_obj_files import obj_mesh

class Engine:

    #TODO: add clipping for triangles


    def __init__(self,  width_window , height_window, __file, window = None, delay_time = 100,background_color = (
        0,0,0)):
        self.keep_the_engine_going = True

        self.delay_time = delay_time
        self.background_color = background_color
        self.height = height_window
        self.width = width_window
        self.__file = __file

        self.delta_time = 1 #inital value. It gets updated every frame

        if window == None:
            screen_size = (self.width, self.height)
            self.window = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
        else:
            self.window = window


        #For some reason the following line needs to be there to track the centers of 3d objects

        pix = pygame.surfarray.pixels3d(self.window)
        self.Window_Manager = WindowManager(pix, self.height, self.width, self.background_color)

        self.models_3d = [] #list of all 3d objects crated
        self.light = Light(0,0,0,50)
        self.camera = Camera(self.models_3d, z = 20)

        self.event_bindings = {} # pygame events mapped to functions

    def create_text(self, text, center_position, spacing, font_size):

        letter_objs = []
        y_offset = 0
        x_offset = 0
        text = text.upper()
        for i in range(len(text)):

            if text[i] == " " or text[i].upper() not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ\n":
                continue

            if text[i] == "\n":
                y_offset -= 30*font_size
                x_offset += (i+1)*spacing
                continue

            car = obj_mesh(rf"models\using_obj_files\obj_letters\uploads_files_1950256_{text[i]}.obj",
                           (255, 255, 255))
            car.teleport(center_position[0] - spacing*i + x_offset, center_position[1] + y_offset, -10)
            car.rotate("x", -90)
            car.rotate("y", 180)
            car.scale(font_size)
            letter_objs.append(car)
            self.add_model(car)

        return letter_objs

    def render_frame(self):

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
            if liste[0].draw_style == SOLID:
                liste[0].draw(self.window, liste[2],  self.light.position, self.light.luminosity)
            else:
                liste[0].wireframe_draw(self.window, self.camera.position)


        # for model in self.models_3d:
        #     pygame.draw.circle(
        #         self.window,
        #     (255,255,255),
        #     project_3d_point_to_2d(model.center,self.width,self.height,self.Camera.position),
        #     radius = 3)

    def add_model(self, obj_3d):
        self.models_3d.append(
                            obj_3d,
                            )

        obj_3d.shift("x", -self.camera.x)
        obj_3d.shift("y", -self.camera.y)
        obj_3d.shift("z", -self.camera.z)
        self.camera.models_3d = self.models_3d # making sure the Camera also has access to our list


    def bind_event(self, event_type, function_to_execute):
        self.event_bindings[event_type] = function_to_execute
    def start_engine(self, ):
        path, name = os.path.split(self.__file)
        sys.path.append(path)

        if ".py" in name:
            name = name.replace(".py", "")
        main_script = __import__(name)
        try:
            main_script.start()
        except:
            print("WARNING: 'start' function not found in script")

        try:
            update = main_script.update
        except:
            def update():
                pass

            print("WARNING: 'update' function not found in script")

        p_original = 10
        p_z_original = 30

        x=0
        total=0

        while self.keep_the_engine_going:
            x += 1

            s = perf_counter()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    break
                elif event.type == pygame.VIDEORESIZE:
                    self.width, self.height = pygame.display.get_window_size()


                elif event.type in self.event_bindings:
                    self.event_bindings[event.type](event)



            update()




            self.render_frame()
            pygame.display.update()
            self.window.fill(self.background_color)
            time_took_for_frame = perf_counter()-s
            self.proper_delay(time_took_for_frame)
            self.delta_time = perf_counter()-s
            total += self.delta_time






        print(f"Average time between frames: {total/x} ({1/(total/x)} fps)")



    def proper_delay(self, frame_time):
        if frame_time >= self.delay_time:
            return None

        pygame.time.delay(int(self.delay_time-frame_time*1000)) # multiply by 1000 to convert to milliseconds

    def stop_engine(self):
        self.keep_the_engine_going = False
