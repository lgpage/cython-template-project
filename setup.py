#!/usr/bin/env python
# encoding: utf-8
# filename: setup.py

import os
import sys
import glob

from distutils.command.build_ext import build_ext
from setuptools import setup, Extension
from setuptools.command.test import test as TestCommand

use_cython = False
cython_opt_o3 = False
cython_force = False
cython_macros = [('CYTHON_TRACE', '1'), ('CYTHON_TRACE_NOGIL', '1')]
cython_directives = {
    'profile': True,
    'linetrace': True,
    'boundscheck': False,
    'wraparound': False,
    'cdivision': True,
    'embedsignature': True,
    }


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)


if "--use-cython" in sys.argv:
    import cython
    from Cython.Distutils import build_ext
    from Cython.Build import cythonize

    use_cython = True
    cython_force = True
    sys.argv.pop(sys.argv.index("--use-cython"))

if "--gcc-O3" in sys.argv:
    cython_opt_o3 = True
    sys.argv.pop(sys.argv.index("--gcc-O3"))

dependencies = []
if os.path.exists('requirements.txt'):
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
            extmod = Extension(filepath, [file_],
                               define_macros=cython_macros)
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
    cmdclass={
        "build_ext": build_ext,
        "test": Tox,
        },
    scripts=scripts,
    entry_points={
        'console_scripts': [
            'coveralls = coveralls.cli:main',
            ],
        },
    )
