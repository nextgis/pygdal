# -*- coding: utf-8 -*-
import os
import sys
from subprocess import check_output, CalledProcessError

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

from distutils.errors import CompileError

GDAL_VERSION = open('GDAL_VERSION', 'r').read().strip()
PKG_VERSION = '5'

ENV_GDALHOME = 'GDALHOME'

PY2 = sys.version_info[0] == 2


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


def supports_cxx11(compiler, compiler_flag=None):
    ret = False
    with open('gdal_python_cxx11_test.cpp', 'wt') as f:
        f.write("""
#if __cplusplus < 201103L
#error "C++11 required"
#endif
int main () { return 0; }""")
        f.close()
        extra_postargs = None
        if compiler_flag:
            extra_postargs = [compiler_flag]

        if os.name == 'posix':
            # Redirect stderr to /dev/null to hide any error messages
            # from the compiler.
            devnull = open(os.devnull, 'w')
            oldstderr = os.dup(sys.stderr.fileno())
            os.dup2(devnull.fileno(), sys.stderr.fileno())
            try:
                compiler.compile([f.name], extra_postargs=extra_postargs)
                ret = True
            except CompileError:
                pass
            os.dup2(oldstderr, sys.stderr.fileno())
            devnull.close()
        else:
            try:
                compiler.compile([f.name], extra_postargs=extra_postargs)
                ret = True
            except CompileError:
                pass
    os.unlink('gdal_python_cxx11_test.cpp')
    if os.path.exists('gdal_python_cxx11_test.o'):
        os.unlink('gdal_python_cxx11_test.o')
    return ret


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
        self.extra_cflags = []

    def get_gdal_config(self, option):
        return fetch_config(option, gdal_config=self.gdal_config)

    def build_extensions(self):
        # Add a -std=c++11 or similar flag if needed
        ct = self.compiler.compiler_type
        if ct == 'unix' and not supports_cxx11(self.compiler):
            cxx11_flag = None
            if supports_cxx11(self.compiler, '-std=c++11'):
                cxx11_flag = '-std=c++11'
            if cxx11_flag:
                for ext in self.extensions:
                    # gdalconst builds as a .c file
                    if ext.name != 'osgeo._gdalconst':
                        ext.extra_compile_args += [cxx11_flag]
        build_ext.build_extensions(self)

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

        cflags = self.get_gdal_config('cflags')
        if cflags:
            self.extra_cflags = cflags.split()

    def build_extension(self, ext):
        ext.extra_compile_args.extend(self.extra_cflags)
        return build_ext.build_extension(self, ext)


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

url = "https://github.com/nextgis/pygdal"

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

# NumPy doesn't support Python 2.x since 1.17
requires = ['numpy>=1.0.0' + (',<1.17' if PY2 else ''), ]

setup(
    name=name,
    version=version,

    author=author,
    author_email=author_email,

    maintainer=maintainer,
    maintainer_email=maintainer_email,

    description=description,
    long_description=long_description,
    long_description_content_type='text/x-rst',
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
