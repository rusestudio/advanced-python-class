from Cython.Build import cythonize
from setuptools import setup

#to compile code python to c  binary code
setup(
    ext_modules=cythonize(
        "julia_fn.pyx",
        compiler_directives={"language_level": "3"}
    )
)