#!/Users/redhouaneabdellaoui/anaconda/envs/DrEA/bin/python python
# -*- coding: utf-8 -*-


import json


class paper:
    def __init__(self):
        self.Title = "Title"
        self.Year = "Year"
        self.Abstract = "Abstract"
        self.Text = "Text"
        self.Authors = "Authors"
        self.References = "References"

    def _read_paper(self, articles_to_process):

        """
        :param articles_to_process: List of paths to articles (in json format) parsed using Science-Parser
        :return: A paper object containing article's texts and metadata
        """

        # Chargemenet du contenu du json
        # https://www.kaggle.com/jboysen/quick-tutorial-flatten-nested-json-in-pandas
        with open(articles_to_process) as article:
            paper_dictionnary = json.load(article)

        self.Title = paper_dictionnary["title"]
        self.Year = paper_dictionnary["year"]
        self.Abstract = paper_dictionnary["abstractText"]
        self.Text = paper_dictionnary['sections']
        self.References = paper_dictionnary['references']
        self.Authors = paper_dictionnary['authors']

        return self

    def _get_paper_text(self):

        """
        This method extract text from article sections et return all the text in one single String value.
        :return:
        """

        paper_text = ""

        for section in self.Text:
            paper_text += section["text"]

        return paper_text
