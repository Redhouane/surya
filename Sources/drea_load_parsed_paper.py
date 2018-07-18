#!/Users/redhouaneabdellaoui/anaconda/envs/DrEA/bin/python python
# -*- coding: utf-8 -*-


from DrEA_head.DrEA_context import *
from DrEA_head.DrEA_paper_class import *
from DrEA_head.DrEA_basic_operations import _opj

import glob
import json
from pandas.io.json import json_normalize


# Chargement de la liste d articles a parser
articles_to_parse = glob.glob(_opj(PARSED_PAPERS_DIRECTORY, '*_parsed.json'))

def read_paper(articles_to_parse):

    # Creation of a paper object for collecting parsed data
    my_paper = paper()

    # Chargemenet du contenu du json
    # https://www.kaggle.com/jboysen/quick-tutorial-flatten-nested-json-in-pandas
    with open(articles_to_parse) as article:
        paper_dictionnary = json.load(article)

    my_paper.Title = paper_dictionnary["title"]
    my_paper.Year = paper_dictionnary["year"]
    my_paper.Abstract = paper_dictionnary["abstractText"]
    my_paper.Text = json_normalize(paper_dictionnary['sections'])
    my_paper.References = json_normalize(paper_dictionnary['references'])
    my_paper.Authors = json_normalize(paper_dictionnary['authors'])

    return(my_paper)


abdellaoui_et_all_2018 = read_paper(articles_to_parse[0])

print("Title :")
print(abdellaoui_et_all_2018.Title)

print("Year :")
print(abdellaoui_et_all_2018.Year)

print("Abstract :")
print(abdellaoui_et_all_2018.Abstract)

print("Text")
print(abdellaoui_et_all_2018.Text)

print("References :")
print(abdellaoui_et_all_2018.References)

print("Authors :")
print(abdellaoui_et_all_2018.Authors)
