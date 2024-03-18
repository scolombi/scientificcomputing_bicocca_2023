# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 17:09:51 2024

@author: stefa
"""

from setuptools import setup, find_packages

setup(name='GameOfLife',
      description='test module for the SciComp class',
      url='https://github.com/scolombi',
      author='Stefano Colombi',
      author_email='s.colombi11@campus.unimib.it',
      license='MIT',
      version='0.0.1',
      packages=find_packages(),
      install_requires=['numpy', 'matplotlib'])