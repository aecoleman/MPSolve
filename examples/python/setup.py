from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import os

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("mpsolve",
                             sources=["mpsolve.pyx"],
                             libraries=["mps", "gmp"],
                             extra_link_args = [ "-L", "../.." + "/src/libmps/.libs" ],
                             include_dirs=[ "../.." + '/include'])]
)