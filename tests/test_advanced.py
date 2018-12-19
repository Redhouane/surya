# -*- coding: utf-8 -*-

import drealib.paper as drea

# Parsing article

try:
    paper_parsed = drea.parse_paper("jbi")
    paper = drea.get_article_as_paper(paper_parsed)
    summary = drea.summarize_paper(paper)
    print(summary)
except ValueError:
    print("No summary generated")
