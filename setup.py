#!/usr/bin/env python
# encoding: utf-8
# filename: setup.py

import os
import sys
import glob

from distutils.command.build_ext import build_ext
from setuptools import setup, Extension

use_cython = False
cython_opt_o3 = False
cython_force = False
cython_linetrace = ('CYTHON_TRACE_NOGIL=1', )
cython_directives = {
    'profile': False,
    'linetrace': False,
    'boundscheck': False,
    'wraparound': False,
    'cdivision': True,
    'embedsignature': False,
    }


if "--use-cython" in sys.argv:
    import cython
    from Cython.Distutils import build_ext
    from Cython.Build import cythonize

    use_cython = True
    cython_force = True
    if "develop" in sys.argv:
        cython_directives['profile'] = True
        cython_directives['linetrace'] = True
        cython_directives['embedsignature'] = True
    sys.argv.pop(sys.argv.index("--use-cython"))

if "--gcc-O3" in sys.argv:
    cython_opt_o3 = True
    sys.argv.pop(sys.argv.index("--gcc-O3"))


with open('requirements.txt', 'r') as fobj:
    dependencies = fobj.read()
dependencies = dependencies.splitlines()

extensions = []
packages = []
excude_dirs = []
for root, _, files in os.walk('proj'):
    if os.path.basename(root) in excude_dirs:
        continue
    packages.append(root)
    for file_ in files:
        file_ = os.path.join(root, file_)
        filepath, ext = os.path.splitext(file_)
        if use_cython and ext == '.pyx':
            if cython_directives['linetrace']:
                extmod = Extension(filepath, [file_],
                                   define_macros=[cython_linetrace])
            else:
                extmod = Extension(filepath, [file_])
            extensions.append(extmod)
        elif ext == '.c':
            extmod = Extension(filepath, [file_])
            extensions.append(extmod)

if use_cython:
    msg = 'Using cython version: {:s} ({:s})'
    print msg.format(cython.__version__, cython.__file__)
    extensions = cythonize(extensions, force=cython_force)

if cython_opt_o3:
    for x in extensions:
        x.extra_compile_args.append("-O3")

scripts = glob.glob(os.path.join('solvers', '*.py'))
setup(
    name='cython-template-project',
    description='Cython Template Project',
    author='Logan Page',
    author_email='page.lg@gmail.com',
    version='0.1',
    url='www.google.com',
    packages=packages,
    install_requires=dependencies,
    ext_modules=extensions,
    cmdclass={"build_ext": build_ext},
    scripts=scripts,
    )
