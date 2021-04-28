
import pyximport
pyximport.install()
from time import perf_counter
from cythonized_math.cython_coordinate_system_3d import rotate as rotate_cython
from Mathematical_Functions.coordinate_system_3d import rotate
from random import uniform, randint, choice
function_cython = rotate_cython
function_python = rotate


x = 100

for i in range(x):
    
    a = [uniform(-2**10,2**10),uniform(-100,100),uniform(-100,100),]
    b = choice(["x","y","z"])
    c = uniform(0,720)

    if function_python(a,b,c) != function_cython(a,b,c):
        print("oh no")
        quit()

    else:print("Yes")

