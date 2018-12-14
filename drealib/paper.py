# -*- coding: utf-8 -*-

from glob import glob
import logging
import json
import os
import requests

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


# Directories for reading/writing files
PAPERS_DIRECTORY = '../articles/'
BUFFER_DIRECTORY = '../buffer/'


class Paper:
    def __init__(self):
        self.title = ""
        self.year = ""
        self.abstract = ""
        self.text = ""
        self.authors = ""
        self.references = ""

    def read_paper(self, articles_to_process):
        """
        :param articles_to_process: List of paths to articles (in json format) parsed using Science-Parser
        :return: A paper object containing article's texts and metadata
        """

        # TODO: Perform a better json read process
        # Loading Json's content
        # https://www.kaggle.com/jboysen/quick-tutorial-flatten-nested-json-in-pandas
        with open(articles_to_process) as article:
            paper_dictionary = json.load(article)

        self.title = paper_dictionary["title"]
        self.year = paper_dictionary["year"]
        self.abstract = paper_dictionary["abstractText"]
        self.text = paper_dictionary['sections']
        self.references = paper_dictionary['references']
        self.authors = paper_dictionary['authors']

        return self

    def get_paper_text(self):
        """
        This method extract text from article sections et return all the text in one single String value.
        :return: A String containing article's plain text
        """
        paper_text: str = ""

        for section in self.text:
            paper_text += section["text"]

        return paper_text


def parse_paper(paper_filename):
    """
    This function call Science-Parse API for parsing an article
    :param paper_filename: Name of article to parse available in "articles" directory
    :return: No value returned
    """

    paper_to_parse = glob(os.path.join(PAPERS_DIRECTORY, paper_filename + ".pdf"))[0]

    logging.info("Papers Parsing...")
    headers = {'Content-type': 'application/pdf', }
    data = open(paper_to_parse, 'rb').read()
    response = requests.post('http://localhost:8080/v1', headers=headers, data=data)

    if response.status_code == 200:
        return response.json()
    else:
        return logging.info("Bad response from science parse tool")


def generate_summary(paper_object, lang='english', sentences_count=10):
    """
    :param paper_object: An instance of class Paper
    :param lang: Language used to write the text to summarize
    :param sentences_count: Sentences count to consider for the ouptuted summary
    :return: A string containing article's summary
    """
    paper_text = paper_object.get_paper_text()
    parser = PlaintextParser.from_string(paper_text, Tokenizer(lang))
    summarizer = LsaSummarizer()
    summary_sentences = summarizer(parser.document, sentences_count)

    summary = ''
    for sentence in summary_sentences:
        summary += str(sentence) + ' '

    return summary


if __name__ == "__main__":
    os.system("")
