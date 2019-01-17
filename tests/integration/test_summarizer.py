# -*- coding: utf-8 -*-

import surya.paper_utils as dr
import surya.text_cleaner as text_cleaner

SINGLE_PAPER_LIST = ['jmir']
MULTIPLE_PAPERS_LIST = ['jmir', 'drug_saf', 'web_based_signal', 'plos', 'bmc', 'jbi']
SECTIONS_LIST = []

try:
    # Summarize a simple paper
    parsed_papers = dr.parse_papers_list(SINGLE_PAPER_LIST)
    # Test text_cleaner :
    n = parsed_papers[0].get_sections_names()
    t = text_cleaner.clean_section_text(
        parsed_papers[0].get_sections_texts_str(['Document-Term Matrix Weighting']))
    summary = dr.build_papers_sections_summary(SINGLE_PAPER_LIST, SECTIONS_LIST)
    print(summary)

    # Summarize a list of papers
    # sections_texts = dr.build_papers_sections_summary(PAPERS_LIST, SECTIONS_LIST)
    # print(sections_texts)
except ValueError:
    print('No summary generated')
