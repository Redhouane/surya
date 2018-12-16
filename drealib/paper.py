# -*- coding: utf-8 -*-

from glob import glob
import logging
import os
import requests

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


# Directories for reading/writing files
_ARTICLES_DIRECTORY = '../sample_articles/'

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

    def get_title(self):
        """
        This method get the paper's title.
        :return: A str instance corresponding to the paper's title.
        """
        return self.title

    def get_year(self):
        """
        This method get the paper's year.
        :return: A int instance corresponding to the paper's year.
        """
        return self.year

    def get_abstract(self):
        """
        This method get the paper's abstract.
        :return: A str instance corresponding to the paper's abstract.
        """
        return self.abstract

    def get_text(self):
        """
        This method get the paper's text.
        :return: A list of dicts instances corresponding to the paper's text.
        Each dict contains a section (associated to the "heading" key) and the section content (with the "text" key).
        """
        return self.text

    def get_authors(self):
        """
        This method get the paper's authors
        :return: A list of dicts instances corresponding to the paper's authors.
        Each dict contains author (with the "name" key) and affiliation as a list (with the "affiliations" key).
        """
        return self.authors

    def get_references(self):
        """
        This method get the paper's references
        :return: A list of dicts instances corresponding to the paper's references.
        Each dict contains reference's title (associated to the "title" key), authors as a list (with the "authors"
        key), journal's name (associated to the "venue" key) and reference's year as integer (associated to the "year"
        key).
        """
        return self.references

    def get_section_text(self, section_name=None):  # "None" correspond to the case when a dict has no 'heading'
        """
        This method get the text corresponding to a given section of the paper's text
        :param section_name: The name of the desired section
        :return: A str instance corresponding to the paper's section name content
        """
        return list(filter(lambda l: l.get('heading') == section_name, self.get_text())).pop().get('text')

    @staticmethod
    def get_doi():
        """
        This method get the paper's doi identifier
        :return: A str instance corresponding to the paper's doi
        """
        return ''

    @staticmethod
    def get_keywords():
        """
        This method get the paper's keywords
        :return: A list instance corresponding to the paper's keywords
        """
        return ''

    @staticmethod
    def get_abbreviations():
        """
        This method get the paper's abbreviations
        :return: A json instance corresponding to the paper's abbreviations
        """
        return ''

    @staticmethod
    def get_coi():  # coi is an acronym for "Conflicts of Interest"
        """
        This method get the paper's "Conflicts of Interest" declaration
        :return: A str instance corresponding to the paper's "Conflicts of Interest"
        """
        return ''

    def get_entire_text(self):
        """
        This method get text from article's sections et return all the text in one single String value.
        :return: A str instance containing article's plain text
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
    paper_to_parse = glob(os.path.join(_ARTICLES_DIRECTORY, paper_filename + ".pdf"))[0]

    logging.info("Papers Parsing...")
    headers = {'Content-type': 'application/pdf', }
    data = open(paper_to_parse, 'rb').read()

    try:
        return requests.post('http://localhost:8080/v1', headers=headers, data=data).json()
    except Exception:
        # At this step, any connection exception involves the same treatment
        logging.exception("Bad response from science parse tool")
        raise ValueError("No parsed paper")  # TODO: Ensure that the right exception type is "ValueError"


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
    paper_text = paper_object.get_entire_text()
    parser = PlaintextParser.from_string(paper_text, Tokenizer(lang))
    summarizer = LsaSummarizer()
    summary_sentences = summarizer(parser.document, sentences_count)

    summary = ''
    for sentence in summary_sentences:
        summary += str(sentence) + ' '  # TODO: Create a class 'utils.py' with useful methods such as 'multi_str_concat'

    return summary


if __name__ == "__main__":
    os.system("")
