# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='photopysnap',
    version=git,
    license="MIT",
    python_requires='>=3.6',
    packages=['photopy'],
    package_dir={'':'src'},
    scripts=[
        'bin/photopy',
        ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        ]
)
