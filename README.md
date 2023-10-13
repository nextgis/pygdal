# Virtualenv friendly GDAL bindings for Python

This package is for you if you had problems installing GDAL in your virtualenv.
You can install GDAL into your virtualenv using this package but you still need
to install GDAL library and its header files on your system. On Ubuntu it can be
done this way:

```bash
$ sudo apt-get install libgdal1-dev
```

Version of the same package, and GDAL, so that if you have installed GDAL 3.6.4
you need to install 3.6.4.\* of this package:

```bash
$ gdal-config --version
3.6.4
$ virtualenv --no-site-packages env
$ env/bin/pip install pygdal=="3.6.4.*"
```

The trick with range of versions required to support pygdal versioning.

Package `numpy` is also listed as a dependency, so you do not need to install it
before installing GDAL. After package is installed you can use is same way as
standard GDAL bindings:

```python
from osgeo import gdal, ogr, osr

# ...
```
