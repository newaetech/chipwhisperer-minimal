#!/usr/bin/env python

from setuptools import setup, find_packages

__version__ = '5.7.0'
with open('chipwhisperer/version.py') as f:
    exec(f.read())
setup(
    name='chipwhisperer',
    version=__version__,
    description='ChipWhisperer Side-Channel Analysis Tool',
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
        'Source': 'https://github.com/newaetech/chipwhisperer-minimal',
        'Issue Tracker': 'https://github.com/newaetech/chipwhisperer-minimal/issues',
    },
    python_requires='~=3.7',
)
