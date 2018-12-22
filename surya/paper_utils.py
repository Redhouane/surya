# -*- coding: utf-8 -*-

from glob import glob
import logging
import os
import requests

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

from surya.paper import Paper

# Directories for reading/writing files
_ARTICLES_DIRECTORY = '../sample_articles/'

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
    paper_to_parse_path = glob(os.path.join(_ARTICLES_DIRECTORY, paper_filename + ".pdf"))[0]

    logging.info("Papers Parsing...")
    headers = {'Content-type': 'application/pdf'}
    data = open(paper_to_parse_path, 'rb').read()

    try:
        return requests.post('http://localhost:8080/v1', headers=headers, data=data).json()
    except Exception:
        # At this step, any connection exception involves the same treatment
        logging.exception("Bad response from science parse tool")
        raise ValueError("No parsed paper.")  # TODO: Ensure that the right exception type is "ValueError"


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


def summarize_paper(paper_object, sections_selection=None, lang='english', sentences_count=10):
    """
    :param paper_object: An instance of class Paper
    :param sections_selection: List of section's to summarize
    :param lang: Language used to write the text to summarize
    :param sentences_count: Sentences count to consider for the outputted summary
    :return: A string containing article's summary
    """
    paper_text = paper_object.get_sections_texts_as_str(sections_selection)
    parser = PlaintextParser.from_string(paper_text, Tokenizer(lang))
    summarizer = LsaSummarizer()
    summary_sentences = summarizer(parser.document, sentences_count)

    summary = ''
    for sentence in summary_sentences:
        summary += str(sentence) + ' '

    return summary


if __name__ == "__main__":
    os.system("")
