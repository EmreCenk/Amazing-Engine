import pyximport
pyximport.install()

from cythonized_graphics.pixels import clear_z_buffer
from time import perf_counter

from time import perf_counter
import numpy
alpha=numpy.full((500,500,3),(0,0,0))

print(alpha)

s=perf_counter()
clear_z_buffer(alpha, (255,255,255))
print("CYTHON:", perf_counter()-s)

print(alpha)