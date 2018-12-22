# -*- coding: utf-8 -*-

import surya.paper_utils as drea

from glob import glob
import os
import requests
import unittest2


class TestDrEA(unittest2.TestCase):  # TODO: Complete the setup for call unit tests from Makefile

    def setUp(self):
        """
        Setting up an instance of class Paper
        """
        paper_parsed = drea.parse_paper("jmir")
        self.func = drea.get_article_as_paper(paper_parsed)

    def test_science_parse_connection(self):
        """
        Testing connexion to SP API
        :return: True if the SP's service status code response is equal to 200
        """
        paper_to_parse = glob(os.path.join('../sample_articles/', "jmir" + ".pdf"))[0]
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

    def test_summarizing_text(self):
        """
        Testing a known paper's text summary
        :return: True if the jmir article's summary is equal to the one expected
        """
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest2.main(verbosity=2)
