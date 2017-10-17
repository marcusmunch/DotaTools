from setuptools import setup

setup(name='dotatools',
	version='1.0',
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
