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
  $ env/bin/pip install pygdal>=1.8.1.0,<=1.8.1.999

The trick with range of versions required to support pygdal versioning.

Only a small set of GDAL versions is currently supported. At this point they are: ``1.8.1``, ``1.9.2``, ``1.10.0``, ``1.10.1``, ``1.11.0``, ``1.11.1``, ``1.11.2``, ``1.11.3``, ``1.11.4`` and ``2.1.0``. Package ``numpy`` is also listed as a dependency (using ``setup_requires`` and ``install_requires`` directives), so you do not need to install it before installing GDAL.

If you installed GDAL using the `KyngChaos frameworks <http://www.kyngchaos.com/software/frameworks/>`_, you may need to override the default values returned by ``gdal-config --prefix`` in order to install this package. This can be accomplished by setting the ``GDALHOME`` environment variable, e.g.

::

  $ export GDALHOME="/Library/Frameworks/GDAL.framework/Versions/Current/unix/"
  $ env/bin/pip install pygdal>=1.8.1.0,<=1.8.1.999

After package is installed you can use is same way as standard GDAL bindings:

::

  from osgeo import gdal

