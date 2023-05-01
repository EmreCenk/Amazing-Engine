from setuptools import setup
from Cython.Build import cythonize

names = [
    "managing_pixels.pyx",
    # "cython_coordinate_system_3d.pyx"
]
for name in names:
    setup(
        ext_modules = cythonize(name, annotate=True)
    )


# Use this command to compile:
# python setup.py build_ext --inplace