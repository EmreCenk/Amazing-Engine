# Amazing-3D-Engine-A3E-
A 3d Graphıcs Engine 

The coordinate system initially takes the camera as the origin (0,0,0).

In the initial camera configuration, the depth is the Z axis, left to right is the X axis and up/down is the Y axis. 

The Engine supports .obj files.
This means that you can import any 3d model that you create in blender. All you need to do this
 export -> export as .obj.
Before exporting, inside the geometry settings,  uncheck all of the boxes except "Triangulate Faces".

#### The shape class:
The shape class is the parent class of all 3D classes.
When you are using the engine as a user, you will almost never need to directly 
interact with the shape class.
Instead, you will interact with the functions that it provides. 
#####Universal Functions for all 3D objects:


#### Using the  obj_mesh class:

To import a .obj file to the engine, you need to use the obj_mesh class.
When initializing, you need to specify two values:
1) The path to the object
2) The desired color of the object

An example:
```python
from graphics.using_obj_files.using_obj_files import obj_mesh

mesh_object = obj_mesh("using_obj_files/sample_object_files/utah_teapot.obj", color = (0,255,255))


```