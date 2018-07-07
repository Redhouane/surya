#!/Users/redhouaneabdellaoui/anaconda/envs/DrEA/bin/python python
# -*- coding: utf-8 -*-

import json
from pandas.io.json import json_normalize


# Chargemenet du contenu du json
# https://www.kaggle.com/jboysen/quick-tutorial-flatten-nested-json-in-pandas

with open('Abdellaoui_et_al_2018_parsed.json') as paper:
    paper_dictionnary = json.load(paper)

paper_df = json_normalize(paper_dictionnary['sections'])

print("sections:")
print(paper_dictionnary.keys())

print("df shape:")
print(paper_df.shape)

print("df columns:")
print(paper_df.columns)

print("les en-têtes:")
print(paper_df["heading"].unique())

print("Nombre d'en-têtes:")
print(len(paper_df["heading"].unique()))

print(paper_df.head(10))
