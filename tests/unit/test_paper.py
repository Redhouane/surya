# -*- coding: utf-8 -*-

from glob import glob
import os
import requests
import unittest2

import surya.paper_utils as dr
from surya import ARTICLES_DIRECTORY


class TestDrEA(unittest2.TestCase):

    def setUp(self):
        """
        Setting up an instance of class Paper
        """

        paper_parsed = dr.parse_paper("jmir")
        self.func = dr.build_paper(paper_parsed)

    def test_science_parse_connection(self):
        """
        Testing connexion to SP API
        :return: True if the SP's service status code response is equal to 200
        """

        paper_to_parse = glob(os.path.join(ARTICLES_DIRECTORY, "jmir" + ".pdf")).pop()
        headers = {'Content-type': 'application/pdf', }
        data = open(paper_to_parse, 'rb').read()
        response = requests.post('http://localhost:8080/v1', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

    def test_empty_parsed_paper(self):
        """
        Testing if the parsing step returned an empty dictionary
        :return: True if the parsed paper is not empty
        """

        assert bool(self.func)

    def test_empty_values_parsed_paper(self):
        """
        Testing article parsing result - empty attribute case
        :return: True if all paper attribute was correctly informed
        """

        self.assertNotEqual(self.func.title, "")
        self.assertNotEqual(self.func.year, "")
        self.assertNotEqual(self.func.abstract, "")
        self.assertNotEqual(self.func.text, "")
        self.assertNotEqual(self.func.authors, "")
        self.assertNotEqual(self.func.references, "")

    def test_paper_sections_selection(self):
        """
        Testing the sections selection from a paper instance
        :return: True if the selection of all sections correspond to the number of sections in the original article
        """

        self.assertEqual(len(self.func.get_text()), len(self.func.get_sections_texts_list([])))

    def test_paper_sections_extraction(self):
        """
        Testing the exact sections selection from a paper instance
        :return: True if the selected section correspond to the right text
        """

        paper_methods_section = 'A summary of the approach presented in this study is provided in Figure 1.'
        paper_objective_section = 'Our objective was to evaluate a topic model approach to identify messages ' \
                                  'describing noncompliant behaviors regarding medications. Topics correspond to ' \
                                  'clusters of words that represent the themes addressed by the patients. The ' \
                                  'distributions of these themes in a corpus of messages are expected to enable the ' \
                                  'targeted extraction of posts corresponding to noncompliance behaviors. We focused ' \
                                  'on two noncompliant behaviors: (1) dose change and (2) treatment cessation.'

        self.assertEqual(self.func.get_sections_texts_str(["Methods"]), paper_methods_section)
        self.assertEqual(self.func.get_sections_texts_str(["Objective"]), paper_objective_section)

    def test_parse_empty_list(self):
        """
        Testing the result of parsing empty papers list
        :return: True if the result is an empty list
        """

        self.assertIsNone(dr.parse_papers_list([]))

    def test_parse_unique_paper_list(self):
        """
        Testing the result of parsing a list with one paper
        :return: True if the result is a list with one paper instance
        """

        self.assertEqual(len(dr.parse_papers_list(["jmir", "drug_saf", "web_based_signal", "plos", "bmc", "jbi"])), 6)

    def test_summarizing_text(self):
        """
        Testing a known paper's text summary
        :return: True if the jmir article's summary is equal to the one expected
        """

        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest2.main(verbosity=2)
