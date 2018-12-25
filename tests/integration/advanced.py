# -*- coding: utf-8 -*-

import surya.paper_utils as dr
import surya.text_cleaner as text_cleaner

# Parsing articles

PAPERS_LIST = ['jmir']
# PAPERS_LIST = ['jmir', 'drug_saf', 'web_based_signal', 'plos', 'bmc', 'jbi']
SECTIONS_LIST = []

try:
    # Summarize a simple paper
    parsed_papers = dr.parse_papers_list(PAPERS_LIST)
    summary = dr.build_papers_sections_summary(PAPERS_LIST, SECTIONS_LIST)
    n = parsed_papers[0].get_sections_names()
    t = text_cleaner.clean_section_text(parsed_papers[0].get_sections_texts_str(['Document-Term Matrix Weighting']))
    print(summary)

    # Summarize a list of papers
    sections_texts = dr.build_papers_sections_summary(PAPERS_LIST, SECTIONS_LIST)
    print(sections_texts)
except ValueError:
    print('No summary generated')
