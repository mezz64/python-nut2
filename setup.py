import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='nut2',
    version='2.0.0',
    modules=['nut2'],
    include_package_data=True,
    install_requires=[],
    license='GPL3',
    description='A Python abstraction class to access NUT servers.',
    long_description=README,
    url='https://github.com/george2/python-nut2',
    author='george2',
    author_email='rpubaddr0@gmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Power (UPS)',
        'Topic :: System :: Systems Administration',
    ],
)