[![PyPI](https://img.shields.io/pypi/v/pynut2.svg)](https://pypi.python.org/pypi/pynut2)

python-nut2
===========

This is an API overhaul of [PyNUT](https://github.com/networkupstools/nut/tree/master/scripts/python),
a Python library to allow communication with NUT ([Network UPS Tools](http://www.networkupstools.org/))
servers.

**Note**: This is an unofficial project, and is in no way supported or
endorsed by the [Network UPS Tools developers](https://github.com/networkupstools).

Original code by rshipp with Python3 modifications by hordurk.

## Requirements

The module itself requires only Python (known to work with versions 2.6 through
3.4). If you wish to run the tests, do `pip install -r requirements-testing.txt`.

## Usage

```python
from nut2 import PyNUTClient
client = PyNUTClient()
client.help()
client.list_ups()
client.list_vars("My_UPS")
```

Please note that this module has completely and intentionally broken
backwards compatibility with PyNUT 1.X.

## Installation

    python setup.py install

## PyNUT

The following information is copied from the original PyNUT README:

> This directory contains various NUT Client related Python scripts, written by
> David Goncalves, and released under GPL v3.
> 
> * "module": this directory contains PyNUT.py, which is a Python abstraction
> class to access NUT server(s). You can use it in Python programs to access NUT's
> upsd data server in a simple way, without having to know the NUT protocol.
> 
> To import it on Python programs you have to use the following (case sensitive) :
> 'import PyNUT'
> 
> This module provides a 'PyNUTClient' class that can be used to connect and get
> data from an upsd data server.
> 
> To install the PyNUT module on Debian/Ubuntu, copy it to:
> /usr/share/python-support/python-pynut/
> 
> This directory also contains test_nutclient.py, which is a PyNUT test program.
> For this to be fully functional, you will need to adapt the login, password and
> upsname to fit your configuration.
