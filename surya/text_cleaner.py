# -*- coding: utf-8 -*-

import re


def clean_section_title(section_title):
    """
    Clean a section's title from numbers
    :param section_title: A section title
    :return: An str instance corresponding to the cleaned section title converted to lower cases
    """
    return re.sub(r'^(\d[.\-\d\s]*)', '', section_title).lower()


def clean_section_text(section_text):
    """
    Clean text from Journal of Medical Internet Research footers
    :param section_text:
    :return:
    """
    semi_cleaned_text = re.sub(r'[\\n\w]*J Med Internet Res \d+\s\|\svol\.\s\d+\s\|\siss\.\s\d+\s\|\s\w\d+\s\|\s\w\.\d+'
                               r'https?:/+(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
                               r'[/\d\w]*\s\([\w+\s]*\)\\n[A-Z•]*\s[A-Za-z\\n?]*', '', section_text)

    cleaned_text = re.sub(r'J Med Internet Res \d+;\d+\(\d+\):\w+\d+\)\sdoi:(\d+\.\d+)/\w+\.\d+',
                          '',
                          semi_cleaned_text)

    return cleaned_text


def standardize_sections_title(section_title):
    """
    Standardize sections names
    :param section_title: A section title
    :return: An str instance corresponding to the standardized section name
    """
    if 'introduction' in section_title:
        return section_title
