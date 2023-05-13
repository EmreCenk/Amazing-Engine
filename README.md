# Amazing-3D-Engine-A3E-

####What is Amazing Engine?
Amazing Engine is a 3D graphics Engine that brings a third dimension to pygame.
Pygame is a 2d python graphics library 
You can use this engine to either create 3d games from scratch, or to add 3d graphics to existing pygame games

** Insert Example Gifs **


###Getting Started
Getting set up with Amazing Engine is a very easy process.
#####Importing and initializing engine:
There are 3 mandatory arguments you need to provide when initializing the engine:
* The screen width
* The screen height
* The current working directory 
* The name of the script you are currently running
```python
from graphics.managing_graphics import Engine
import os
screen_width = 800
screen_height = 600
script_name = "my_script"
my_engine = Engine(screen_width, screen_height, os.getcwd(), script_name, delay_time=25)

```

###Creating 3D objects:
Amazing Engine has a variety of 3d shapes such as rectangular prisms. The Engine also supports .obj files. 

#### Importing .obj files:

To import a .obj file to the engine, you need to use the obj_mesh class.
When initializing, you need to specify two values:
1) The path to the object
2) The desired color of the object

An example:
```python
from models.using_obj_files.using_obj_files import obj_mesh
mesh_object = obj_mesh("using_obj_files/sample_object_files/utah_teapot.obj", color = (0,255,255))
```
####Universal Functions for all 3D objects:




maybe:
This means that you can import any 3d model that you create in blender. All you need to do this
 export -> export as .obj.
Before exporting, inside the geometry settings,  uncheck all of the boxes except "Triangulate Faces".