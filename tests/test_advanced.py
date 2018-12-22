# -*- coding: utf-8 -*-

import surya.paper_utils as dr

# Parsing article

try:
    # paper_parsed = dr.parse_paper("jmir")
    paper_parsed = dr.parse_papers_list([])
    print(paper_parsed)

    # paper = dr.build_paper(paper_parsed[0])
    # summary = dr.summarize_paper(paper)
    # print(summary)
except ValueError:
    print("No summary generated")
