# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='photopysnap',
    version='0.1.0',
    #description='Picture management (tagging, renaming)',
    #long_description_markdown_filename='README.md',
    author='Eike Kühn',
    author_email='',
    url='https://github.com/randomchars42/photopy',
    license="MIT",
    keywords='Photos,Pictures,Tags',
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
