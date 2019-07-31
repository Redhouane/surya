# -*- coding: utf-8 -*-

import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="surya",
    version="1.0.0",
    author="Redhouane Abdellaoui",
    author_email="redhouane.a@gmail.com",
    description="Parse and retrieve information from biomedical research articles in pdf format",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/Red1/surya.git",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: MacOS/Linux",
    ],
)
