# /usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""

import setuptools
from distutils.core import setup
import codecs
import os
import sys

try:
	from setuptools import setup, find_packages
except:
	from distutils import setup

with open('README.md', 'r', encoding="utf-8") as fp:
	readme = fp.read()

VERSION = "1.0.1"
LICENSE = "MIT"

setup(
	name='taobao-openapi',
	version=VERSION,
	description=(
		'集合了淘宝开放平台的商铺OPEN API，并适配了Python3'
	),
	author='samzong.lu',
	author_email='samzong.lu@gmail.com',
	maintainer='samzong.lu',
	maintainer_email='samzong.lu@gmail.com',
	license=LICENSE,
	packages=find_packages(),
	platforms=["all"],
	url='https://github.com/SAMZONG/taobao-sdk-python3',
	install_requires=[
		"requests"
		],
	classifiers=[
		'Development Status :: 4 - Beta',
		'Operating System :: OS Independent',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Programming Language :: Python',
		'Programming Language :: Python :: Implementation',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Topic :: Software Development :: Libraries'
		],
	)
