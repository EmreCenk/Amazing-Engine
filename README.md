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
from graphics.managing_graphics import Engine
import os
from models.using_obj_files.using_obj_files import obj_mesh
my_engine = Engine(600, 800, os.getcwd(), "script_name", delay_time=25) # initializing engine
mesh_object = obj_mesh("using_obj_files/sample_object_files/utah_teapot.obj", color = (0,255,255))

my_engine.add_model(mesh_object) #This function must be called when you create any 3d object
```
Whenever you create a new 3d object, you need to call the Engine.add_model function. Otherwise your 3d object will
 not be rendered.

At this point, the mesh_object class can be treated as if it was any other built in shape.
Any methods that are built into built in 3d shapes are also valid for a mesh_class object.
 
#### Other 3d objects:
The engine has many built in shapes. * insert examples *


 
 
####Universal Methods for all 3D objects:
All 3d objects have some common methods that can be called. (These 3d objects can be an obj_mesh class, or any other
 built in shape)

##### Moving objects
In order to move an object, you call the .move method for the object. The move method takes in two inputs:
1) axis: a string "x", "y" or "z". Instead of the axis values as strings, you can also input 0, 1, and 2 respectively.
2) amount: an integer, how much to move the object by

```python
from models.using_obj_files.using_obj_files import obj_mesh
mesh_object = obj_mesh("using_obj_files/sample_object_files/utah_teapot.obj", color = (0,255,255))

#MOVING ALONG THE X AXIS:
mesh_object.move("x", 10) #moves the object 10 units on the x axis
mesh_object.move(0, 10) #Equivalent to the above expression

#MOVING ALONG THE Y AXIS:
mesh_object.move(axis = "y", amount = -10) #moves the object -10 units on the x axis

```

##### Rotating objects
To rotate an object, you call the .rotate method. Takes in two inputs:
1) axis: The axis to rotate around, any string "x", "y", "z" or the integers 0, 1, 2 respectively
2) angle: How many degrees to rotate the object by, any float (By default, the input is in degrees, NOT RADIANS)

The rotate method also takes in one keyword arguement which is False by default:
3) radian_input: a boolean value specifying whether the input is in radians, when the input is True, the amount
 variable will be treated as radians
 
```python
from models.using_obj_files.using_obj_files import obj_mesh
mesh_object = obj_mesh("using_obj_files/sample_object_files/utah_teapot.obj", color = (0,255,255))\

mesh_object.rotate("x", 10) #rotates the mesh_object by 10 degrees along the x axis
mesh_object.rotate(axis = "y", angle = 1, radian_input=True) #rotates the mesh_object by 1 radian along the y axis
```
 



maybe:
This means that you can import any 3d model that you create in blender. All you need to do this
 export -> export as .obj.
Before exporting, inside the geometry settings,  uncheck all of the boxes except "Triangulate Faces".