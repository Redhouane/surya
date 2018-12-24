# -*- coding: utf-8 -*-

import surya.paper_utils as dr

# Parsing articles

PAPERS_LIST = ["drug_saf", "jmir"]
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
    print("No summary generated")
