# -*- coding: utf-8 -*-

"""
The surya package contains every components related to the data extraction from a set of research articles.

This package consists of the following components:
:paper: This class collects data from a parsed pdf articles.
:paper_utils: This module consists of functions to parse the loaded pdfs and generate summarizes.
:text_cleaner: This method contains methods to clean the text extracted from pdfs.
"""

import logging

ARTICLES_DIRECTORY = '../tests/fixtures/'  # Directories for reading/writing files

# Logging config
logging.basicConfig(level=logging.INFO,
                    filename='../surya.log',
                    filemode='a',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
