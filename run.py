from graphics.managing_graphics import graphics_manager
a = graphics_manager(500,500,delay_time=0)
a.init_loop()


# NO SPINNING:

# NO CYTHON FRAME COMPUTATION TIME: 
# with 50 average: 0.05767583599999998
# with 500 average: 0.07503629079999993

# WITH CYTHON IMPLEMENTED IN THE COORDINATES
# with 50 average: 0.04944095000000001
# with 500 average: 0.0693012192000001 

# WITH ROTATION:

#WITH PYTHON:
# 50 average: 0.08283374199999999

#WITH CYTHON:
# 50 average: 0.05133066399999999
# 500 average: 0.0607807720000001
