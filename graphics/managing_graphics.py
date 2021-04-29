import pygame
import graphics.shapes_3d as sh3
from graphics.camera import camera
from graphics.using_obj_files.using_obj_files import obj_mesh
from time import perf_counter

try:
    #Try importing the cython files:
    # import pyximport
    # pyximport.install()
    from cythonized_math.cython_coordinate_system_3d import distance,rotate,get_normal,is_visible,normalize_triangle_vertices, normalized
    from cythonized_math.cythonized_projecting import project_3d_point_to_2d, translate, efficient_triangle_projection

except Exception as E:
    #If the cython files don't work, then use the pure pyhton implementations
    from Mathematical_Functions.projecting import project_3d_point_to_2d, translate, efficient_triangle_projection
    from Mathematical_Functions.coordinate_system_3d import distance, rotate,get_normal,is_visible,normalize_triangle_vertices, normalized

from Mathematical_Functions.shading import get_color

class graphics_manager:

    def __init__(self,  width_window , height_window, delay_time = 100, background_color = (0,0,0)):
        self.delay_time = delay_time
        self.background_color = background_color
        self.height = height_window
        self.width = width_window
        self.camera = camera( z = 20)
        self.delta_time = 1 #inital value. It gets updated every frame
        self.models = []

        
    def start_engine(self):
        pygame.init()
        screen_size = (self.height,self.width)
        self.window = pygame.display.set_mode(screen_size, pygame.RESIZABLE)

    def render_frame(self):
        camera_position = self.camera.position
        normalized_camera = normalized(camera_position)
        to_draw = []
        for model in self.models:
            for triangle in model.triangles:

                translated_vert = triangle.get_translated(camera_position)
                if is_visible(translated_vert,normalized_camera):
                    to_draw.append(
                        [triangle, distance(triangle.get_centroid(),camera_position),translated_vert]
                    )

        to_draw.sort(key = lambda tri: tri[1], reverse=True)

        for liste in to_draw:
            new_color = get_color(liste[0],
                                    normalized_light_source=normalized_camera
                                    , rgb_colour = liste[0].color)

            w, h = pygame.display.get_window_size()
            coordiantes = efficient_triangle_projection(liste[2],w,h)

            pygame.draw.polygon(self.window,points=coordiantes,color=new_color)
                    

    def init_loop(self, functions_to_call=None):

        if functions_to_call is None:
            functions_to_call = []

        self.start_engine()

        shift = 0
        side = 5
        v1,v2,v3,v4,v5,v6,v7,v8 = [shift, shift, side], [side, shift, side], [side, shift, shift],[shift, shift, shift],\
        [shift,side, side],[side, side, side],[side,side, shift],[shift, side, shift]

        # self.tester_rectangle = sh3.rectangular_prism(v1, v2, v3, v4, v5, v6, v7, v8, color=(255,255,0)

        #                                               )
        self.tester_rectangle = obj_mesh("graphics/using_obj_files/sample_object_files/sphere_5_scaled.obj", color = (255,0,0))


        self.tester_mesh = obj_mesh("graphics/using_obj_files/sample_object_files/sphere_5_scaled.obj", color = (255,255,0))
        # self.tester_rectangle2 = sh3.rectangular_prism(v1, v2, v3, v4, v5, v6, v7, v8, color="white"
        #
        #                                               )


        # self.tester_mesh2 = obj_mesh("using_obj_files/sample_object_files/utah_teapot.obj")
        self.tester_mesh2 = obj_mesh("graphics/using_obj_files/sample_object_files/sphere_5_scaled.obj", color = (0,255,255))


        self.tester_rectangle.move("x",11)
        self.tester_mesh2.move("x",-11)

        # self.tester_mesh2.move("x",-10)

        
        self.models.extend([self.tester_mesh2,
                            self.tester_mesh,
                            self.tester_rectangle])
        # self.tester_mesh2.move("x",5)a
        # self.tester_mesh.move("x",-5)
        p_original = 10
        p_z_original = 10

        x=0
        total=0
        while x<500:
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


            self.tester_mesh2.rotate("y",1)
            self.tester_rectangle.rotate("y",1)
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

