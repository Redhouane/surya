# -*- coding: utf-8 -*-

from glob import glob
import logging
import os
import requests

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


# Directories for reading/writing files
PAPERS_DIRECTORY = '../sample_articles/'

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.INFO,
                    filename='surya.log',
                    filemode='a',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class Paper:
    def __init__(self):
        self.title = ""
        self.year = ""
        self.abstract = ""
        self.text = ""
        self.authors = ""
        self.references = ""

    def get_text(self):
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
        logging.info("Bad response from science parse tool")


def get_article_as_paper(parsed_paper):
    """
    :param parsed_paper: article parsed using Science-Parse as python dictionary
    :return: A paper object containing article's texts and metadata
    """
    paper = Paper()

    paper.title = parsed_paper["title"]
    paper.year = parsed_paper["year"]
    paper.abstract = parsed_paper["abstractText"]
    paper.text = parsed_paper['sections']
    paper.references = parsed_paper['references']
    paper.authors = parsed_paper['authors']

    return paper


def summarize_paper(paper_object, lang='english', sentences_count=10):
    """
    :param paper_object: An instance of class Paper
    :param lang: Language used to write the text to summarize
    :param sentences_count: Sentences count to consider for the outputted summary
    :return: A string containing article's summary
    """
    paper_text = paper_object.get_text()
    parser = PlaintextParser.from_string(paper_text, Tokenizer(lang))
    summarizer = LsaSummarizer()
    summary_sentences = summarizer(parser.document, sentences_count)

    summary = ''
    for sentence in summary_sentences:
        summary += str(sentence) + ' '  # TODO: Create a class 'utils.py' with useful methods such as 'multi_str_concat'

    return summary


if __name__ == "__main__":
    os.system("")
