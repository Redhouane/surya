#!/Users/redhouaneabdellaoui/anaconda/envs/DrEA/bin/python python
# -*- coding: utf-8 -*-

import json
from pandas.io.json import json_normalize


# Chargemenet du contenu du json
# https://www.kaggle.com/jboysen/quick-tutorial-flatten-nested-json-in-pandas

with open('Abdellaoui_et_al_2018_parsed.json') as paper:
    paper_dictionnary = json.load(paper)

paper_text = json_normalize(paper_dictionnary['sections'])
paper_references = json_normalize(paper_dictionnary['references'])
paper_authors = json_normalize(paper_dictionnary['authors'])

print("Science-Parser ID:")
print(paper_dictionnary["id"])

print("Parsed Data:")
print(paper_dictionnary.keys())

print("Titre:")
print(paper_dictionnary["title"])

print("Année:")
print(paper_dictionnary["year"])

print("Abstract:")
print(paper_dictionnary["abstractText"])

print("Texte:")
print(paper_text.head())

print("Références:")
print(paper_references.head())

print("Auteurs:")
print(paper_authors.head())
