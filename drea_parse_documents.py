#!/Users/redhouaneabdellaoui/anaconda/envs/DrEA/bin/python python
# -*- coding: utf-8 -*-

import os

# Parsind pdf article using science-parse
# https://github.com/allenai/science-parse

_PAPER_NAME_FILE = "Abdellaoui_et_al_2018"


def parse_paper(paper):
    print("Paper Parsing...")
    os.system('curl -v -H "Content-type: application/pdf" --data-binary @{0}.pdf "http://scienceparse.allenai.org/v1" > {1}.json'.format(paper, paper + "_parsed"))


parse_paper(_PAPER_NAME_FILE)
