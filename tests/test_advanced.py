# -*- coding: utf-8 -*-

import drealib.paper as drea

# Parsing article
print("Parsed article:")
paper_parsed = drea.parse_paper("jmir")

summary = ''

if bool(paper_parsed):
    paper = drea.get_article_as_paper(paper_parsed)
    summary = drea.summarize_paper(paper)
    print(summary)
else:
    print(summary)