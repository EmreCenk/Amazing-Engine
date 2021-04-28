
import pyximport
pyximport.install()
from time import perf_counter
from cythonized_math.cython_coordinate_system_3d import distance as distance_cython
from Mathematical_Functions.coordinate_system_3d import distance
function_cython = distance_cython
function_python = distance

a = [6,7,8]
b = [1,2,3]
c = 62

s = perf_counter()
tim = 100000

for i in range(tim):
    pass

intime = 0

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

