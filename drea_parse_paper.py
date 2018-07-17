#!/Users/redhouaneabdellaoui/anaconda/envs/DrEA/bin/python python
# -*- coding: utf-8 -*-

import glob
import os


# Fonction de concatenation des paths
def _opj(path_1, path_2):
    return os.path.join(path_1, path_2)


PAPERS_DIRECTORY = '/Users/redhouaneabdellaoui/Documents/Red1/MyCoreTechs/DrEA/articles'

# Parsind pdf article using science-parse
# https://github.com/allenai/science-parse

_PAPER_NAME_FILE = glob.glob(_opj(PAPERS_DIRECTORY, '*.pdf'))

# import pdb; pdb.set_trace()

def parse_paper(paper):
    print("Paper Parsing...")
    parsed_file_name = paper.split('.')[0] + "_parsed"
    os.system('curl -v -H "Content-type: application/pdf" --data-binary @{0}.pdf "http://scienceparse.allenai.org/v1" > {1}.json'.format(paper, parsed_file_name))

    # SPv2
    # os.system('curl -v --data-binary {0}.pdf "http://localhost:8081/v1/json/pdf" > {1}.json'.format(paper)

[parse_paper(publi) for publi in _PAPER_NAME_FILE]
