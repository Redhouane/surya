#!/Users/redhouaneabdellaoui/anaconda/envs/DrEA/bin/python python
# -*- coding: utf-8 -*-

import json
from pyteaser import Summarize
from glob import glob
import os


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

    # TODO: Upgrade the parsing to SPv2 or to Apache Tika. The Science-Parse 1.0 API not working anymore.
    paper_to_parse = glob(os.path.join(PAPERS_DIRECTORY, paper_filename + ".pdf"))[0]
    print("Paper Parsing...")
    parsed_filename = paper_to_parse.split('.')[-2].split('/')[-1] + "_parsed"
    os.system("""curl -v -H "Content-type: application/pdf" --data-binary @{0}
        "http://scienceparse.allenai.org/v1" > {1}.json""".format(paper_to_parse, parsed_filename))

    # SPv2
    # os.system('curl -v --data-binary {0}.pdf "http://localhost:8081/v1/json/pdf" > {1}.json'.format(paper)

def generate_summary(paper_object):
    """
    :param paper_object: An instance of class Paper
    :return: A string containing article's summary
    """

    # Summary is constituted using key phrases concatenation
    key_phrases = Summarize(paper_object.title,
                            paper_object.get_paper_text())

    return '\n'.join(key_phrases)


if __name__ == "__main__":
    os.system("")
