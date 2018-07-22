#!/Users/redhouaneabdellaoui/anaconda/envs/DrEA/bin/python python
# -*- coding: utf-8 -*-


from DrEA_head.DrEA_context import *
from DrEA_head.DrEA_paper_class import *
from DrEA_head.DrEA_basic_operations import _opj

import glob
from pyteaser import Summarize


# Upload list of articles to parse
articles_to_parse = glob.glob(_opj(PARSED_PAPERS_DIRECTORY, '*_parsed.json'))

# Initialization of paper object with article data and metadata
# See paper class method _read_paper()

abdellaoui_et_all_2018 = paper()
abdellaoui_et_all_2018 = abdellaoui_et_all_2018._read_paper(articles_to_parse[0])

# Summary is constituted using key phrases concatenation
key_phrases = Summarize(abdellaoui_et_all_2018.Title,
                        abdellaoui_et_all_2018._get_paper_text())

summary = '\n'.join(key_phrases)

print('\n')
print(summary)
