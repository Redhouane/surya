# -*- coding: utf-8 -*-

import surya.paper_utils as dr
import surya.text_cleaner as text_cleaner

# Parsing articles

PAPERS_LIST = ['web_based_signal', 'jmir', 'bmc']
# PAPERS_LIST = ["jmir", "drug_saf", "web_based_signal", "plos", "bmc", "jbi"]
SECTIONS_LIST = ["Conclusions"]

try:
    # Summarize a simple paper
    parsed_papers = dr.parse_papers_list(PAPERS_LIST)
    summary = dr.build_papers_sections_summary(PAPERS_LIST, SECTIONS_LIST)
    print(summary)

    # Summarize a list of papers
    sections_texts = dr.build_papers_sections_summary(PAPERS_LIST, SECTIONS_LIST)
    print(sections_texts)
except ValueError:
    print('No summary generated')
