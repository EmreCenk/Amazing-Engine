
import pyximport
pyximport.install()
from time import perf_counter
from cythonized_math.cython_coordinate_system_3d import rotate as rotate_cython
from Mathematical_Functions.coordinate_system_3d import rotate
function_cython = rotate_cython
function_python = rotate

a = [6,7,8]
b = "x"
c = 62

s = perf_counter()
tim = 1000

for i in range(tim):
    pass

intime = perf_counter() - s

s = perf_counter()


for i in range(tim):
    
    function_cython(a,b,c)
ctime = perf_counter()-s-intime

s = perf_counter()

for i in range(tim):
    function_python(a,b,c)

print(
    function_cython(a,b,c)
    )
print(function_python(a,b,c))
ptime = perf_counter() - s - intime

print('PYTHON:',ptime)
print("CYTHON:",ctime)
print(f"Cython is {ptime/ctime} times faster.")

