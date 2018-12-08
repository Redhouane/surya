# -*- coding: utf-8 -*-

import os

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
# from sumy.nlp.stemmers import Stemmer
# from sumy.utils import get_stop_words

# Directories for reading/writing files
PAPERS_DIRECTORY = '../../articles/'
BUFFER_DIRECTORY = '../../buffer/'

LANGUAGE = "english"
SENTENCES_COUNT = 10

if __name__ == "__main__":
    parser = PlaintextParser.from_file(os.path.join(BUFFER_DIRECTORY, "document.txt"), Tokenizer(LANGUAGE))
    # stemmer = Stemmer(LANGUAGE)
    # summarizer = Summarizer(stemmer)
    # summarizer.stop_words = get_stop_words(LANGUAGE)

    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, SENTENCES_COUNT)

    for sentence in summary:
        print(sentence)
