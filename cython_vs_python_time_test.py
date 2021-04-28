
import pyximport
pyximport.install()
from time import perf_counter
from cythonized_math.cython_coordinate_system_3d import magnitude as ma_cyth
from Mathematical_Functions.coordinate_system_3d import magnitude
function_cython = ma_cyth
function_python = magnitude

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
    
    function_cython(a)
ctime = perf_counter()-s-intime

s = perf_counter()

for i in range(tim):
    function_python(a)


ptime = perf_counter() - s - intime

print('PYTHON:',ptime)
print("CYTHON:",ctime)
print(f"Cython is {ptime/ctime} times faster.")

