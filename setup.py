#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup

setup(name='dotatools',
	version='0.0.2',
	description='An API wrapper for the OpenDota API',
	url='http://github.com/marcusmunch/dotatools',
	author='Marcus Grünewald',
	author_email='marcus@marcusmunch.dk',
	license='GNU General Public License v3.0',
	packages=['dotatools'],
	install_requires=[
		'requests',
	],
	zip_safe=False)
