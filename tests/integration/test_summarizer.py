# -*- coding: utf-8 -*-

import surya.paper_utils as dr
import surya.paper_cleaner as paper_cleaner

SINGLE_PAPER_LIST = ['jmir']
MULTIPLE_PAPERS_LIST = ['jmir', 'drug_saf', 'web_based_signal', 'plos', 'bmc', 'jbi']
SECTIONS_LIST = []

try:
    # Summarize a simple paper
    parsed_papers = dr.parse_papers_list(MULTIPLE_PAPERS_LIST)

    # Test text_cleaner :
    paper = parsed_papers[0]
    text_to_clean = paper.get_sections_texts_str(['Document-Term Matrix Weighting'])
    cleaned_section_text = paper_cleaner.clean_section_text(text_to_clean)

    summary = dr.build_papers_sections_summary(MULTIPLE_PAPERS_LIST, SECTIONS_LIST)
    print(summary)

except ValueError:
    print('No summary generated')
