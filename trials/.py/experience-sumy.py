# -*- coding: utf-8 -*-

import os

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Directories for reading/writing files
PAPERS_DIRECTORY = '../../articles/'
BUFFER_DIRECTORY = '../../buffer/'

LANGUAGE = "english"
SENTENCES_COUNT = 5

text = """A report published by the World Health Organization (WHO) in 2003 highlighted that noncompliance (or 
nonadherence) to long-term treatment was a worldwide problem detrimental to the overall effectiveness of the health 
system [1]. Compliance is defined in this report as the degree of correspondence between a patient’s behavior (taking 
medications, following hygiene rules, and diet) and the recommendations made by a health care professional (HCP). 
Noncompliance with these recommendations has an impact on patients’ quality of life (QoL), outcomes, and health costs.
The WHO identified several causes of nonadherence to therapies, including the characteristics of the health system, 
the patient’s disease, and the course of treatment. For patients with depression, observance is linked to the frequency 
of administration of a drug and to concomitant therapy. For patients suffering from cancer, the fear of adverse effects 
(AEs) related to the treatment has negative impact on adherence. For diabetic patients, adherence may vary with age, 
sex, and the relationship with the physician. Several meta-analyses showed that current methods of improving medication 
adherence for chronic diseases were mostly complex and not very effective [2,3]. The Cochrane group concluded that (1) 
means to measure adherence more systematically and objectively and (2) innovations to assist patients to follow 
medication prescriptions for long-term medical disorders were major points to be considered in that field. Considering 
social media as platforms where patients can discuss about their treatments and share testimonies, they could be a new 
data source to measure adherence to treatment."""

if __name__ == "__main__":
    parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))

    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, SENTENCES_COUNT)

    for sentence in summary:
        print(sentence)
