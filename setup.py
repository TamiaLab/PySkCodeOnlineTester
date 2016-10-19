#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://docs.djangoproject.com/en/dev/intro/reusable-apps/

import os

from pip.req import parse_requirements

from setuptools import setup, find_packages


# Dump readme content as text
with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()


# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


# Setup config
setup(
    name='skcodeonlinetester',
    version='1.3.0',
    packages=find_packages(),
    include_package_data=True,
    license='AGPLv3',
    description='Online testing Website for the PySkCode project implemented with Django framework and Python 3.4',
    long_description=README,
    url='https://github.com/TamiaLab/PySkCodeOnlineTester',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[str(pkg.req) for pkg in parse_requirements('requirements.txt')],
    tests_require=[str(pkg.req) for pkg in parse_requirements('requirements-dev.txt')],
)
