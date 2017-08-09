import os
import sys
from codecs import open

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

assert sys.version_info[0] == 3, "golosdata requires Python > 3"


def readme_file():
    return 'README.rst' if os.path.exists('README.rst') else 'README.md'


setup(
    name='golosdata',
    version='0.0.1',
    description='Python Utilities for parsing GOLOS blockchain',
    long_description=open(readme_file()).read(),
    url='https://github.com/pmartynov/golosdata',
    author='@steepshot',
    author_email='steepshot.org@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='golos golosio',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
        'steep-golos',
        'pymongo',
        'requests',
        'funcy',
        'werkzeug',
    ],

    extras_require={
        'dev': [''],
        'test': [''],
    },
)
