from setuptools import setup
from Cython.Build import cythonize

names = [
    "cythonized_projecting.pyx",
    "cython_coordinate_system_3d.pyx"
]
for name in names:
    setup(
        ext_modules = cythonize(name)
    )


# Use this command to compile:
# python setup.py build_ext --inplace