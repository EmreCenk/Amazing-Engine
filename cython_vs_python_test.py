
import pyximport
pyximport.install()
from time import perf_counter
from cythonized_math.cython_coordinate_system_3d import translate_triangle_vertices as trcyth
from Mathematical_Functions.coordinate_system_3d import translate_triangle_vertices
function_cython = trcyth
function_python = translate_triangle_vertices
a=[[1,2,3],[1,2,3],[1,2,3]]
b=[2,3,4]

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

