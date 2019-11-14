# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in approved_accounting/__init__.py
from approved_accounting import __version__ as version

setup(
	name='approved_accounting',
	version=version,
	description='Approved Accounting for ERPnext',
	author='One Asset Management',
	author_email='massimo.fierro@one-asset.co.kr',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
