#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup

setup(name='dotatools',
	version='0.1',
	description='OpenDota API wrapper',
	long_description='dotatools is an API wrapper for the open API supplied by OpenDota',
	url='http://github.com/marcusmunch/dotatools',
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Programming Language :: Python'
	],
	author='Marcus Grünewald',
	author_email='marcus@marcusmunch.dk',
	license='GNU General Public License v3.0',
	packages=['dotatools'],
	install_requires=[
		'requests',
	],
	zip_safe=False)
