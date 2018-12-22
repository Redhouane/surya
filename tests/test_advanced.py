# -*- coding: utf-8 -*-

import surya.paper_utils as drea

# Parsing article

try:
    paper_parsed = drea.parse_paper("jmir")
    paper = drea.get_article_as_paper(paper_parsed)
    summary = drea.summarize_paper(paper)
    print(summary)
except ValueError:
    print("No summary generated")
