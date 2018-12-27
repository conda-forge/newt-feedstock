from setuptools import setup, find_packages, Extension
import os

snack = Extension('_snack',
                  libraries = ['newt', 'slang'],
                  sources = ['snack.c'])

setup (name = os.environ['PKG_NAME'],
       version = os.environ['PKG_VERSION'],
       description = 'Newt is a library for color text mode, widget based user interfaces',
       py_modules=['snack'],
       url = 'https://github.com/conda-forge/newt-feedstock',
       ext_modules = [snack])
