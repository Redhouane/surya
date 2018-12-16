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

    def get_sections_texts_list(self, sections_names=None):  # "None" correspond to case when a dict has no 'heading'
        """
        This method get a list of texts corresponding to a given list of paper's sections
        :param sections_names: A list of desired sections names
        :return: A list of str instances corresponding to the paper's sections names contents
        """
        paper = self.get_text()

        if sections_names is None or len(sections_names) == 0:
            all_sections_names = list(map(lambda l: l.get('heading'), paper))
            all_sections = list(filter(lambda l: l.get('heading') in all_sections_names, paper))
            return list(map(lambda l: l.get('text'), all_sections))
        else:
            sections_list = list(filter(lambda l: l.get('heading') in sections_names, paper))
            return list(map(lambda l: l.get('text'), sections_list))

    def get_sections_texts_as_str(self, sections_names=None):
        """
        This method get the text corresponding to a given list of paper's sections
        :param sections_names: A list of desired sections names
        :return: A str instance corresponding to the concatenated paper's sections names contents
        """
        return ' '.join(self.get_sections_texts_list(sections_names))

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


def summarize_paper(paper_object, sections_to_summarize=None, lang='english', sentences_count=10):
    """
    :param paper_object: An instance of class Paper
    :param sections_to_summarize: List of section's names to summarize
    :param lang: Language used to write the text to summarize
    :param sentences_count: Sentences count to consider for the outputted summary
    :return: A string containing article's summary
    """
    paper_text = paper_object.get_sections_texts_as_str(sections_to_summarize)
    parser = PlaintextParser.from_string(paper_text, Tokenizer(lang))
    summarizer = LsaSummarizer()
    summary_sentences = summarizer(parser.document, sentences_count)

    summary = ''
    for sentence in summary_sentences:
        summary += str(sentence) + ' '  # TODO: Create a class 'utils.py' with useful methods such as 'multi_str_concat'

    return summary


if __name__ == "__main__":
    os.system("")
