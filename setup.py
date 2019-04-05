#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

requirements = [
    'fire>=0.1.3',
]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Michael Bilow",
    author_email='michael.k.bilow@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python Fire Example",
    entry_points='''
        [console_scripts]
        widget=widget.cli:main
    ''',
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords='python-fire',
    name='widget',
    packages=find_packages(),
    setup_requires=setup_requirements,
    url='https://github.com/michaelbilow/python-fire-example',
    version='0.0.1',
    zip_safe=False,
)

