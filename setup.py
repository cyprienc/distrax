# Copyright 2021 DeepMind Technologies Limited. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Install script for setuptools."""

import os
from setuptools import find_namespace_packages
from setuptools import setup

_CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def _get_version():
  with open(os.path.join(_CURRENT_DIR, 'distrax', '__init__.py')) as fp:
    for line in fp:
      if line.startswith('__version__') and '=' in line:
        version = line[line.find('=') + 1:].strip(' \'"\n')
        if version:
          return version
    raise ValueError('`__version__` not defined in `distrax/__init__.py`')


def _parse_requirements(path):

  with open(os.path.join(_CURRENT_DIR, path)) as f:
    return [
        line.rstrip()
        for line in f
        if not (line.isspace() or line.startswith('#'))
    ]


setup(
    name='distrax',
    version=_get_version(),
    url='https://github.com/deepmind/distrax',
    license='Apache 2.0',
    author='DeepMind',
    description=('Distrax: Probability distributions in JAX.'),
    long_description=open(os.path.join(_CURRENT_DIR, 'README.md')).read(),
    long_description_content_type='text/markdown',
    author_email='distrax-dev@google.com',
    keywords='jax probability distribution python machine learning',
    packages=find_namespace_packages(exclude=['*_test.py']),
    install_requires=_parse_requirements(
        os.path.join(_CURRENT_DIR, 'requirements', 'requirements.txt')),
    tests_require=_parse_requirements(
        os.path.join(_CURRENT_DIR, 'requirements', 'requirements-tests.txt')),
    zip_safe=False,  # Required for full installation.
    include_package_data=True,
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
