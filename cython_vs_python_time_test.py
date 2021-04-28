
import pyximport
pyximport.install()
from time import perf_counter
from cythonized_math.cython_coordinate_system_3d import is_visible as iscyth
from Mathematical_Functions.coordinate_system_3d import is_visible
function_cython = iscyth
function_python = is_visible

a = [[6,7,8],[6,7,8],[6,7,8]]
b = [0.5,0.8,0.1]
c = 62

s = perf_counter()
tim = 1000000

for i in range(tim):
    pass

intime = perf_counter() - s

s = perf_counter()


for i in range(tim):
    
    function_cython(a,b)
ctime = perf_counter()-s-intime

s = perf_counter()

for i in range(tim):
    function_python(a,b)


ptime = perf_counter() - s - intime

print('PYTHON:',ptime)
print("CYTHON:",ctime)
print(f"Cython is {ptime/ctime} times faster.")

