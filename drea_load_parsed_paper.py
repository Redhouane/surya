#!/Users/redhouaneabdellaoui/anaconda/envs/DrEA/bin/python python
# -*- coding: utf-8 -*-

import glob
import json
import os
from pandas.io.json import json_normalize


# Fonction de concatenation des paths
def _opj(path_1, path_2):
    return os.path.join(path_1, path_2)


# Repertoires de lecture des articles et d ecriture des versions parsee
PAPERS_DIRECTORY = '/Users/redhouaneabdellaoui/Documents/Red1/MyCoreTechs/DrEA/articles'
PARSED_PAPERS_DIRECTORY = '/Users/redhouaneabdellaoui/Documents/Red1/MyCoreTechs/DrEA/parsed_articles'

# Chargement de la liste d articles a parser
articles_to_parse = glob.glob(_opj(PARSED_PAPERS_DIRECTORY, '*_parsed.json'))

# Chargemenet du contenu du json
# https://www.kaggle.com/jboysen/quick-tutorial-flatten-nested-json-in-pandas

with open(articles_to_parse[0]) as paper:
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
