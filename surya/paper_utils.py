# -*- coding: utf-8 -*-

from glob import glob
import logging
import os
import requests
from requests.exceptions import ConnectionError

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

from surya import ARTICLES_DIRECTORY
from surya.paper import Paper

LANG = 'english'  # Predefined language for texts analyzed
SENTENCES_COUNT = 7  # Number of key sentences used for generate summarizes


def call_science_parse(articles_filename: str, articles_path: str = ARTICLES_DIRECTORY) -> dict:
    """
    This function call Science-Parse API for parsing an article
    :param articles_filename: Name of article to parse available in "articles" directory
    :param articles_path: Location to folder from where articles will be load
    :return: No value returned
    """

    papers_to_parse_paths = glob(os.path.join(articles_path, articles_filename + ".pdf"))
    assert papers_to_parse_paths,\
        "The specified folder do not contains pdf articles"

    logging.info("Papers Parsing...")
    headers = {'Content-type': 'application/pdf'}
    data = open(papers_to_parse_paths.pop(), 'rb').read()

    with requests.Session() as session:
        try:
            return session.post('http://localhost:8080/v1', headers=headers, data=data).json()
        except Exception:
            # At this step, any connection exception involves the same treatment
            logging.exception("Bad response from science parse tool")
            raise ConnectionError("No parsed paper.")


def build_paper_from_sp(parsed_paper: dict) -> Paper:
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


def parse_papers_list(articles_names_list: list) -> list:
    """
    This function apply the parsing paper process to a list of articles
    :param articles_names_list: The articles's names to parse
    :return: A list of Paper instances corresponding to the parsed articles
    """

    if not articles_names_list:
        logging.info("No article selected.")
    else:
        try:  # TODO: Specify the folder from which to read articles in the map below
            parsed_papers_list = list(map(call_science_parse, articles_names_list))
            return list(map(build_paper_from_sp, parsed_papers_list))
        except IndexError:
            # If an element in the given list do not exists
            logging.exception("Please check the articles loaded list. At least one of them seems do not exists.")


def build_summary_from_paper(paper_object: Paper, sections_selection=None) -> str:
    """
    This function summarize texts corresponding to selected sections in a paper instance
    :param paper_object: An instance of class Paper
    :param sections_selection: List of section's to summarize
    :return: A string containing article's summary
    """

    paper_text = paper_object.get_sections_texts_str(sections_selection)
    parser = PlaintextParser.from_string(paper_text, Tokenizer(LANG))
    summarizer = LsaSummarizer()
    summary_sentences = summarizer(parser.document, SENTENCES_COUNT)
    summary = ' '.join(list(map(str, summary_sentences)))

    return summary


def build_summary_from_papers_list(papers_list: list, sections_to_summarize: list) -> str:
    """
    Merge the texts corresponding to sections selected for generate a summary from different papers
    :param papers_list: A list of papers instances
    :param sections_to_summarize: A list of sections to summarize
    :return: A str object corresponding to selected sections texts summary
    """

    sections_texts = list(
        map(lambda paper: paper.get_sections_texts_str(sections_to_summarize), parse_papers_list(papers_list))
    )

    text = ' '.join(sections_texts)
    parser = PlaintextParser.from_string(text, Tokenizer(LANG))
    summarizer = LsaSummarizer()
    summary = ' '.join(list(map(str, summarizer(parser.document, SENTENCES_COUNT))))

    return summary


if __name__ == "__main__":
    os.system("Surya package. Utils functions source.")
