# -*- coding: utf-8 -*-

import logging

ARTICLES_DIRECTORY = '../tests/fixtures/'  # Directories for reading/writing files

# Logging config
logging.basicConfig(level=logging.INFO,
                    filename='surya.log',
                    filemode='a',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
