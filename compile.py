########################################################
# This program builds .so files from .py files
# and delete '.py', '.c' and '.pyc' files.# install cpython:
# sudo pip install cython
# Command to run build:
# python compile.py build_ext --inplace
########################################################

import os
import sys
from distutils.core import setup
from distutils.extension import Extension
from pathlib import Path

from Cython.Build import cythonize

# Get current folder path
mash_path = os.path.dirname(sys.argv[0])

### Get .py files
extensions = []
excludefiles = ['compile', '__init__', 'main', 'routes']

### build .so files from .py files ###
for file in list(Path(mash_path).glob('**/*.py')):
    # Take out file name without .py ext
    filename = Path(file).resolve().stem
    if file.stat().st_size != 0 and filename not in excludefiles:
        relpath = os.path.relpath(os.path.dirname(file.absolute().as_posix()), mash_path)
        packagename = relpath.replace('/', '.') + '.' + filename if relpath != '.' else filename
        extensions.append([Extension(packagename, [str(file)])])

for ext in extensions:
    setup(ext_modules=cythonize(ext, compiler_directives={
        'c_string_type': 'str',
        'c_string_encoding': 'utf8',
        'language_level': 3}))

def deletefiles(file_type):
    cfiles = list(Path(mash_path).glob('**/*.' + file_type))
    for cfile in cfiles:
        filename = Path(cfile).resolve().stem
        if filename not in excludefiles:
            cfile.unlink()

### delete *.py files ###
deletefiles('py')

### delete *.c files #####
deletefiles('c')

### delete *.pyc files #####
deletefiles('pyc')
