#!/usr/bin/env python

"""
ADC121C_MQ9 Gas Sensor.

The MQ9 is capable of sensing carbon monoxide and combustible gas concentration levels.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
	       'Intended Audience :: Science/Research',
               'Programming Language :: Python :: 2.6',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware',
	       'Topic :: Scientific/Engineering :: Physics']

setup(
    name='ADC121C_mq9',
    version='0.0.0',
    author='EmbdEzaz9',
    author_email='embdezaz9@gmail.com',
    description="""This MQ-9sensor can detect multiple gases (CO, H2, CH4, LPG, propane, alcohol, smoke) and outputs analog voltage""",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    license='MIT',
    keywords=["ESP8266","Risc V","Raspberry Pi"],
    platforms = 'Linux',
    url='https://github.com/EmbdEzaz9/ADC121C_mq9',
    classifiers=classifiers,
    packages=['ADC121C_mq9'],
    dependency_links  = [],
    install_requires=[]
)
