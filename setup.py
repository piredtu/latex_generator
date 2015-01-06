from distutils.core import setup
from setuptools import find_packages

setup(
    name='latex_generator',
    version='0.1',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires = ['pypandoc'],
    url='https://github.com/piredtu/latex_generator',
    license='AGPL v3.0',
    author='Pierre-Elouan Rethore',
    author_email='pire@dtu.dk',
    description='A report and slide generator using python and latex'
)
