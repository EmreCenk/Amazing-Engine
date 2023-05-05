from time import perf_counter

from graphics.managing_graphics import graphics_manager
a = graphics_manager(800,600,delay_time=25)
a.init_loop()



# NO SPINNING:

# NO CYTHON FRAME COMPUTATION TIME: 2
# with 50 average: 0.05767583599999998
# with 500 average: 0.07503629079999993

# WITH CYTHON IMPLEMENTED IN THE COORDINATES
# with 50 average: 0.04944095000000001
# with 500 average: 0.0693012192000001 






# WITH ROTATION:
#WITH PYTHON:
# 50 average: 0.08283374199999999 (12.0723750474 fps)
# 500 average: 0.08010581060000002 (12.4834889318 fps)

#WITH CYTHON:
# 50 average: 0.05133066399999999 (19.4815325202 fps)
# 500 average: 0.0607807720000001 (16.4525715468 fps)

# when projecting was also written in cython:
# 50 average: 0.049037928000000036
# 500 average: 0.05049307179999995 (~20 fps )