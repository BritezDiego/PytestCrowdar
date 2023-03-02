"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_namespace_packages

setup(
 
    name='core',  # Required

    version='1.0.0',  # Required

    url='',  # Optional

    packages=find_namespace_packages(include=['core.*']),  # Required

    python_requires='>=3.7',
)
