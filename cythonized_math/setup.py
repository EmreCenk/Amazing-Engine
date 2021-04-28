import pyximport
pyximport.install()
from cython_coordinate_system_3d import rotate

print(rotate([1,2,3], "x", 50))