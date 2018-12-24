# -*- coding: utf-8 -*-

from glob import glob
import logging
import os
import requests

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

from surya.paper import Paper

LANG = 'english'  # Predefined language for texts analyzed
SENTENCES_COUNT = 7  # Number of key sentences used for generate summarizes
_ARTICLES_DIRECTORY = '../sample_articles/'  # Directories for reading/writing files

# Logging config
logging.basicConfig(level=logging.INFO,
                    filename='surya.log',
                    filemode='a',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def parse_paper(paper_filename):
    """
    This function call Science-Parse API for parsing an article
    :param paper_filename: Name of article to parse available in "articles" directory
    :return: No value returned
    """
    paper_to_parse_path = glob(os.path.join(_ARTICLES_DIRECTORY, paper_filename + ".pdf")).pop()

    logging.info("Papers Parsing...")
    headers = {'Content-type': 'application/pdf'}
    data = open(paper_to_parse_path, 'rb').read()

    try:
        return requests.post('http://localhost:8080/v1', headers=headers, data=data).json()
    except Exception:
        # At this step, any connection exception involves the same treatment
        logging.exception("Bad response from science parse tool")
        raise ValueError("No parsed paper.")  # TODO: Ensure that the right exception type is "ValueError"


def build_paper(parsed_paper):
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


def parse_papers_list(articles_names_list):
    """
    This function apply the parsing paper process to a list of articles
    :param articles_names_list: The articles's names to parse
    :return: A list of Paper instances corresponding to the parsed articles
    """
    if not articles_names_list:
        logging.warning("No article selected.")
    else:
        try:
            parsed_papers_list = list(map(parse_paper, articles_names_list))
            return list(map(build_paper, parsed_papers_list))
        except IndexError:
            # If an element in the given list do not exists
            logging.exception("Please check the articles loaded list. At least one of them seems do not exists.")


def build_paper_summary(paper_object, sections_selection=None):
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


def build_papers_sections_summary(papers_list, sections_to_summarize):
    """
    This function merge the texts corresponding to sections selected for generate a summary
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
