#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='chipwhisperer',
    version='5.6.1',
    description='Minimal version of ChipWhisperer that only supports the CW310',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='NewAE Technology Inc',
    author_email='sales@newae.com',
    license='apache',
    url='https://www.chipwhisperer.com',
    packages=find_packages('.'),
    package_dir={'': '.'},
    install_requires=[
        'pyserial',
        'libusb1',
        'Cython',
    ],
    project_urls={
        'Documentation': 'https://chipwhisperer.readthedocs.io',
        'Source': 'https://github.com/newaetech/chipwhisperer',
        'Issue Tracker': 'https://github.com/newaetech/chipwhisperer/issues',
    },
    python_requires='~=3.6',
)
