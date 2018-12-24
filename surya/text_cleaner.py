# -*- coding: utf-8 -*-

import re


def clean_section_title(section_title):
    """
    Clean a section's title from numbers
    :param section_title: A section title
    :return: An str instance corresponding to the cleaned section title converted to lower cases
    """
    return re.sub(r'^(\d[.\-\d\s]*)', '', section_title).lower()
