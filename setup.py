import setuptools
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Based on: https://circleci.com/blog/continuously-deploying-python-packages-to-pypi-with-circleci/
"""
:copyright: (c) 2018 by Antonio Feregrino
:license: MIT, see LICENSE for more details.
"""
import os
import sys

from setuptools import setup
from setuptools.command.install import install

# Package version
VERSION = "0.5.0"

class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this library: {1}".format(
                tag, VERSION
            )
            sys.exit(info)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="m16_mlutils",
    version=VERSION,
    author="Antonio Feregrino",
    author_email="antonio.feregrino@gmail.com",
    description="Some stuff that is probably better implemented somewhere else but I'm still a newbie to find out where...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/messier16/m16_mlutils",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    cmdclass={
        'verify': VerifyVersionCommand,
    }
)