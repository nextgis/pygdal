pygdal
======

Virtualenv and setuptools friendly version of standard GDAL python bindings. 

This package is for you if you had problems installing GDAL in your virtualenv. You can install GDAL into your virtualenv using this package but you still need to install GDAL library and its header files on your system. On Ubuntu it can be done this way:

::

  $ sudo apt-get install libgdal1-dev

Version of the same package, and GDAL, so that if you have installed GDAL 1.8.1 you need to install the version 1.8.1 of this package:

::

  $ gdal-config --version
  1.8.1
  
  $ git clone git@github.com:dezhin/pygdal.git
  $ cd pygdal
  $ virtualenv --no-site-packages env
  $ env/bin/pip install 1.8.1/

Or you can install package directly from PyPi:

::

  $ virtualenv --no-site-packages env
  $ env/bin/pip install pygdal==1.8.1

Only a small set of GDAL versions is currently supported. At this point they are: ``1.8.1``, ``1.9.2``, ``1.10.0``, ``1.10.1``, ``1.11.0`` and ``1.11.1``. Package ``numpy`` is also listed as a dependency (using ``setup_requires`` and ``install_requires`` directives), so you do not need to install it before installing GDAL.

After package is installed you can use is same way as standard GDAL bindings:

::

  from osgeo import gdal

