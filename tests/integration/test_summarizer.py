# -*- coding: utf-8 -*-

import surya.paper_utils as surya

SINGLE_PAPER_LIST = ['jmir']
MULTIPLE_PAPERS_LIST = ['jmir', 'drug_saf', 'web_based_signal', 'plos', 'bmc', 'jbi']
SECTIONS_LIST = ['Background', 'Materials', 'Method', 'Results']

try:
    # Summarize a simple paper
    parsed_papers = surya.parse_papers_list(MULTIPLE_PAPERS_LIST)

    summary = surya.build_summary_from_papers_list(MULTIPLE_PAPERS_LIST, SECTIONS_LIST)
    print(summary)

except ValueError:
    print('No summary generated')
