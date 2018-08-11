#!/Users/redhouaneabdellaoui/anaconda/envs/DrEA/bin/python python
# -*- coding: utf-8 -*-


import pydeepl


sentence = 'I like turtles.'
from_language = 'EN'
to_language = 'FR'

translation = pydeepl.translate(sentence, to_language, from_lang=from_language)
print(translation)

# Using auto-detection
translation = pydeepl.translate(sentence, to_language)
print(translation)