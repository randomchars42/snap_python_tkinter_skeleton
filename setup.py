# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='python-tkinter-skeleton',
    version='0.1.0',
    license="The unlicense",
    python_requires='>=3.6',
    packages=['skeleton'],
    package_dir={'':'src'},
    scripts=[
        'bin/skeleton',
        ],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        ]
)
