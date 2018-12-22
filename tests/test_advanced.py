# -*- coding: utf-8 -*-

import surya.paper_utils as dr

# Parsing articles

try:
    paper_parsed = dr.parse_papers_list(["jmir", "drug_saf", "web_based_signal", "plos", "bmc", "jbi"])
    paper = dr.build_paper(paper_parsed[0])
    summary = dr.summarize_paper(paper)
    print(summary)
except ValueError:
    print("No summary generated")
