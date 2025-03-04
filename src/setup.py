from setuptools import setup
from Cython.Build import cythonize

ext_modules = cythonize("main.py")
setup(
    Name = "Quick-Encrypt",
    ext_modules=ext_modules
)