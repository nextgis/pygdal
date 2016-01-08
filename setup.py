# -*- coding: utf-8 -*-
import os
from subprocess import check_output, CalledProcessError

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

GDAL_VERSION = open('GDAL_VERSION', 'r').read().strip()
PKG_VERSION = '3'

ENV_GDALHOME = 'GDALHOME'


class GDALConfigError(Exception):
    pass


def get_numpy_include():
    # Fix numpy installation using setuptools
    __builtins__.__NUMPY_SETUP__ = False

    import numpy
    return numpy.get_include()


def fetch_config(option, gdal_config='gdal-config'):
    try:
        return check_output([gdal_config, '--%s' % option]).decode('utf-8').strip()
    except CalledProcessError as e:
        raise GDALConfigError(e)


class gdal_ext(build_ext):

    GDAL_CONFIG = 'gdal-config'

    def run(self):
        inst_gdal_version = self.get_gdal_config('version')
        if inst_gdal_version != GDAL_VERSION:
            raise GDALConfigError('Version mismatch %s != %s' % (
                inst_gdal_version, GDAL_VERSION))

        build_ext.run(self)

    def initialize_options(self):
        build_ext.initialize_options(self)

        self.gdaldir = None
        self.gdal_config = self.GDAL_CONFIG

    def get_gdal_config(self, option):
        return fetch_config(option, gdal_config=self.gdal_config)

    def finalize_options(self):
        if self.libraries is None:
            self.libraries = ['gdal', ]

        build_ext.finalize_options(self)

        if ENV_GDALHOME in os.environ:
            print('GDAL prefix from environment variable %s' % ENV_GDALHOME)
            self.gdaldir = os.environ[ENV_GDALHOME]
        else:
            self.gdaldir = self.get_gdal_config('prefix')

        self.include_dirs.append(get_numpy_include())

        self.library_dirs.append(os.path.join(self.gdaldir, 'lib'))
        self.include_dirs.append(os.path.join(self.gdaldir, 'include', 'gdal'))
        self.include_dirs.append(os.path.join(self.gdaldir, 'include'))


extra_link_args = []
extra_compile_args = []

gdal_module = Extension(
    'osgeo._gdal',
    sources=['extensions/gdal_wrap.cpp'],
    extra_compile_args=extra_compile_args,
    extra_link_args=extra_link_args)

gdalconst_module = Extension(
    'osgeo._gdalconst',
    sources=['extensions/gdalconst_wrap.c'],
    extra_compile_args=extra_compile_args,
    extra_link_args=extra_link_args)

osr_module = Extension(
    'osgeo._osr',
    sources=['extensions/osr_wrap.cpp'],
    extra_compile_args=extra_compile_args,
    extra_link_args=extra_link_args)

ogr_module = Extension(
    'osgeo._ogr',
    sources=['extensions/ogr_wrap.cpp'],
    extra_compile_args=extra_compile_args,
    extra_link_args=extra_link_args)

gdal_array_module = Extension(
    'osgeo._gdal_array',
    sources=['extensions/gdal_array_wrap.cpp'],
    extra_compile_args=extra_compile_args,
    extra_link_args=extra_link_args)

ext_modules = [
    gdal_module,
    gdalconst_module,
    osr_module,
    ogr_module,
    gdal_array_module,
]

packages = ["osgeo", ]

name = 'pygdal'
version = GDAL_VERSION + '.' + PKG_VERSION

author = "Frank Warmerdam"
author_email = "warmerdam@pobox.com"

maintainer = "Aleksandr Dezhin"
maintainer_email = "me@dezhin.net"

description = "Virtualenv and setuptools friendly " \
    + "version of standard GDAL python bindings"

long_description = str(open('README.rst', 'rb').read())

url = "https://github.com/dezhin/pygdal"

license = "MIT"

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2',
    'Programming Language :: C',
    'Programming Language :: C++',
    'Topic :: Scientific/Engineering :: GIS',
    'Topic :: Scientific/Engineering :: Information Analysis',
]

requires = ['numpy>=1.0.0', ]

setup(
    name=name,
    version=version,

    author=author,
    author_email=author_email,

    maintainer=maintainer,
    maintainer_email=maintainer_email,

    description=description,
    long_description=long_description,
    url=url,

    license=license,

    classifiers=classifiers,

    setup_requires=requires,
    install_requires=requires,

    packages=packages,
    ext_modules=ext_modules,
    zip_safe=False,
    cmdclass=dict(build_ext=gdal_ext),
)
