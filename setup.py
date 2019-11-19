#!/usr/bin/python3

import glob
import os

from setuptools import setup

setup(
    name = "scylla",
    version = "0.0.1",
    author = "Kory Findley (k0fin)",
    author_email = "technicalsyn@gmail.com",
    description = ("A command-line client for scylla.sh"),
    license = "BSD",
    install_requires=[
      'bs4',
      'requests',
        ],
    keywords = "scylla breach data creds credentials passwords disclosure",
    url = "https://www.github.com/k0fin/scylla",
    scripts = ['scripts/scylla'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
