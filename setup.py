# -*- coding: utf-8 -*-


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="surya",
    version="0.0.1",
    author="Redhouane Abdellaoui",
    author_email="redhouane.a@gmail.com",
    description="Manipulating research articles.",
    long_description="This package allow to parse, summarize and manipulate data from a collection of articles.",
    long_description_content_type="text/markdown",
    url="https://gitlab.com/Red1/surya.git",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS/Linux",
    ),
)