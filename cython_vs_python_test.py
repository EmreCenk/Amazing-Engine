
import pyximport
pyximport.install()
from time import perf_counter
from cythonized_math.cython_coordinate_system_3d import translate as trcyth
from Mathematical_Functions.coordinate_system_3d import translate

s = perf_counter()
tim = 1000000

for i in range(tim):
    pass

intime = perf_counter() - s

s = perf_counter()

a=[1,2,3]
b=[2,3,4]
for i in range(tim):
    trcyth(a,b)
ctime = perf_counter()-s-intime

s = perf_counter()

for i in range(tim):
    translate(a,b)
ptime = perf_counter() - s - intime

print('PYTHON:',ptime)
print("CYTHON:",ctime)
print(f"Cython is {ptime/ctime} times faster.")

