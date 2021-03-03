# -*- coding: utf-8 -*-
"""Pokemon app."""
import os
import sys

from setuptools import find_packages
from setuptools import setup


NAME = "pokemon"

DESCRIPTION = ""

here = os.path.abspath(os.path.dirname(__file__))

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name=NAME,
    version="1",
    keywords="",
    setup_requires=["pytest-runner", "flake8"] if "test" in sys.argv else [],
    tests_require=[
        "pytest==3.0.7",
        "pytest-quickcheck==0.8.2",
        "coverage==4.3.4",
        "pytest-cov==2.4.0",
        "testfixtures==4.9.1",
    ],
    install_requires=required,
    description=DESCRIPTION,
    long_description="",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.7",
        "Environment :: Console",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
