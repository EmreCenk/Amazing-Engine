import pyximport
pyximport.install()

from cythonized_graphics.pixels import clear_z_buffer, efficient_clear_z_buffer
from time import perf_counter

from time import perf_counter
import numpy

alpha=numpy.full((500,500,3),(0,0,0))

real_bs = 0
numtimes = 50
total_average_time = 0
for AS in range(numtimes):
    total = 0
    for b in range(2,1000):


        s=perf_counter()
        clear_z_buffer(alpha, (255,255,255))
        cython = perf_counter()-s
        # print("CYTHON:", perf_counter()-s)


        thing = []
        for i in range(b):
            for j in range(b):
                thing.append([i,j])
        thing = numpy.array(thing)
        s=perf_counter()
        efficient_clear_z_buffer(alpha, thing, (255,255,255))
        efcython = perf_counter()-s

        total+=efcython+cython
        if efcython>cython:
            print("BREAKING POINT:",b,"ef:",efcython,"norm:",cython)
            
            real_bs += b
            

    total_average_time += total
    print("AVERAGE TIME:",(total)/(2*b))
print()
print()
print("overall average time:", total_average_time/numtimes)
print("average breakpoint:",real_bs/numtimes)