from graphics.managing_graphics import Engine
from models.using_obj_files.using_obj_files import obj_mesh
from constants import WIREFRAME
screen_width = 800
screen_height = 600

engine = Engine(screen_width, screen_height, __file__, delay_time=25)
engine.light.luminosity = 10
teapot = obj_mesh("models/using_obj_files/sample_object_files/utah_teapot.obj", (255,255,255))
teapot.shift("z", 15)
teapot.shift("y", -2)
teapot.rotate("x", -30)
teapot.rotate("y", -30)

# teapot.change_draw_style(WIREFRAME)

engine.add_model(teapot)
engine.camera.shift("z",-0.4)

def update():
    pass
engine.start_engine()