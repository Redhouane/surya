#!/Users/redhouaneabdellaoui/anaconda/envs/DrEA/bin/python python
# -*- coding: utf-8 -*-

import drealib.paper as paper

from glob import glob
import os

# Parsing article
# paper.parse_paper("jmir")

# Upload list of articles to parse
red1_articles = glob(os.path.join(paper.BUFFER_DIRECTORY, '*_parsed.json'))

# Initialization of paper object with article data and metadata
# See paper class method _read_paper()

abdellaoui_et_all_2018 = paper.Paper()
abdellaoui_et_all_2018 = abdellaoui_et_all_2018.read_paper(red1_articles[0])

print(paper.generate_summary(abdellaoui_et_all_2018))
