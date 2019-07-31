# -*- coding: utf-8 -*-

from glob import glob
import os
import requests
import unittest2

import surya.paper_utils as surya
from surya import ARTICLES_DIRECTORY


class TestPaper(unittest2.TestCase):

    def setUp(self):
        """
        Setting up an instance of class Paper
        """

        paper_parsed = surya.call_science_parse("jmir")
        self.func = surya.build_paper_from_sp(paper_parsed)

    def test_science_parse_connection(self):
        """
        Testing connexion to SP API
        :return: True if the SP's service status code response is equal to 200
        """

        paper_to_parse = glob(os.path.join(ARTICLES_DIRECTORY, "jmir" + ".pdf")).pop()
        headers = {'Content-type': 'application/pdf', }
        data = open(paper_to_parse, 'rb').read()  # TODO: File open but never close. Use a with keyword.
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

        self.assertEqual(len(self.func.get_sections_texts()), len(self.func.get_sections_texts_list([])))

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

        self.assertIsNone(surya.parse_papers_list([]))

    def test_parse_n_papers_list(self):
        """
        Testing the result of parsing a list with n papers
        :return: True if the result is a list with n paper instance
        """

        self.assertEqual(
            len(surya.parse_papers_list(["jmir", "drug_saf", "web_based_signal", "plos", "bmc", "jbi"])), 6
        )

    def test_citation_info_retrieval(self):
        """
        Testing the retrieval of data that constitute citation
        :return: True if the extracted citation data corresponds to the expected citation data
        """

        extracted_citation_data = self.func.get_paper_citation_infos()
        expected_citation_data = {
            'title': 'Detection of Cases of Noncompliance to Drug Treatment in Patient Forum Posts: '
                     'Topic Model Approach',
            'first_author': 'Redhouane Abdellaoui',
            'year': 2018,
            'journal': 'Coming Soon'
        }

        self.assertTrue(extracted_citation_data == expected_citation_data)

    def test_sections_names_and_texts(self):
        """
        Testing if we did retrieve all sections and corresponding texts
        :return: True if the all sections and texts were extracted
        """

        self.assertEqual(len(self.func.get_sections_names()), 36)
        self.assertEqual(len(self.func.get_sections_texts_list()), 36)


if __name__ == '__main__':
    unittest2.main(verbosity=2)
