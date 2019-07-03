# -*- coding: utf-8 -*-

import unittest2

from surya import ARTICLES_DIRECTORY
import surya.paper_charts as surya_charts
import surya.paper_utils as surya_utils


class TestPaperCharts(unittest2.TestCase):

    def setUp(self):
        """
        Setting up an instance of class Paper
        """

        papers_list = ["jmir", "drug_saf", "web_based_signal", "plos", "bmc", "jbi"]
        self.func = surya_utils.parse_papers_list(papers_list)

    def test_papers_per_years_chart(self):
        """
        Testing if the count  of papers per year dictionary made for dashboard's plots are equal to the expected.
        :return: True if the calculated count dict corresponds to the expected one
        """

        expected_dict = {
            '2018': 3,
            '2015': 1,
            '2017': 1,
            '2016': 1
        }

        result_dict = surya_charts.count_papers_per_year(self.func)
        self.assertEqual(result_dict, expected_dict)


if __name__ == '__main__':
    unittest2.main(verbosity=2)
