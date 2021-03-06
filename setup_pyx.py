from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

setup(
    name='nuclitrack',
    version='1.0.8',
    description='Nuclei tracking program',
    author='Sam Cooper',
    author_email='sam@socooper.com',
    license='MIT',
    packages=['nuclitrack'],
    ext_modules=cythonize([
        Extension("ctooltracking", ["pyx_files/ctooltracking.pyx"], include_dirs=[numpy.get_include()]),
        Extension("classifyim", ["pyx_files/classifyim.pyx"], include_dirs=[numpy.get_include()]),
        Extension("ctoolsegmentation", ["pyx_files/ctoolsegmentation.pyx"], include_dirs=[numpy.get_include()]),
        Extension("numpytoimage", ["pyx_files/numpytoimage.pyx"], include_dirs=[numpy.get_include()])])
)
