# -*- coding: utf-8 -*-

import os


class Paper:
    def __init__(self):
        self.title = ""
        self.year = ""
        self.abstract = ""
        self.text = ""
        self.authors = ""
        self.references = ""

    def get_title(self):
        """
        This method get the paper's title.
        :return: A str instance corresponding to the paper's title.
        """
        return self.title

    def get_year(self):
        """
        This method get the paper's year.
        :return: A int instance corresponding to the paper's year.
        """
        return self.year

    def get_abstract(self):
        """
        This method get the paper's abstract.
        :return: A str instance corresponding to the paper's abstract.
        """
        return self.abstract

    def get_text(self):
        """
        This method get the paper's text.
        :return: A list of dicts instances corresponding to the paper's text.
        Each dict contains a section (associated to the "heading" key) and the section content (with the "text" key).
        """
        return self.text

    def get_authors(self):
        """
        This method get the paper's authors
        :return: A list of dicts instances corresponding to the paper's authors.
        Each dict contains author (with the "name" key) and affiliation as a list (with the "affiliations" key).
        """
        return self.authors

    def get_references(self):
        """
        This method get the paper's references
        :return: A list of dicts instances corresponding to the paper's references.
        Each dict contains reference's title (associated to the "title" key), authors as a list (with the "authors"
        key), journal's name (associated to the "venue" key) and reference's year as integer (associated to the "year"
        key).
        """
        return self.references

    def get_sections_texts_list(self, sections_selection=None):  # "None" for cases when section's dict has no 'heading'
        """
        This method get a list of texts corresponding to a given list of paper's sections
        :param sections_selection: A list of desired sections names
        :return: A list of str instances corresponding to the paper's sections names contents
        """
        paper_sections = self.get_text()

        if sections_selection is None or len(sections_selection) == 0:
            all_sections_names = list(map(lambda l: l.get('heading'), paper_sections))

            # Filtering of sections handled with "None" value and corresponding to free article's texts
            all_sections = list(filter(lambda l: l.get('heading') in all_sections_names, paper_sections))
            return list(map(lambda l: l.get('text'), all_sections))
        else:
            sections_list = list(filter(lambda l: l.get('heading') in sections_selection, paper_sections))
            return list(map(lambda l: l.get('text'), sections_list))

    def get_sections_texts_str(self, sections_names=None):
        """
        This method get the text corresponding to a given list of paper's sections
        :param sections_names: A list of desired sections names
        :return: A str instance corresponding to the concatenated paper's sections names contents
        """
        return ' '.join(self.get_sections_texts_list(sections_names))

    @staticmethod
    def get_doi():
        """
        This method get the paper's doi identifier
        :return: A str instance corresponding to the paper's doi
        """
        return ''  # TODO: Add a pattern recognition based on a regex

    def get_keywords(self):
        """
        This method get the paper's keywords
        :return: A list instance corresponding to the paper's keywords
        """
        return list(filter(lambda l: l.get('heading') == "KEYWORDS", self.get_text())).pop().get('text').split(';')

    def get_abbreviations(self):
        """
        This method get the paper's abbreviations
        :return: A json instance corresponding to the paper's abbreviations
        """
        return list(filter(lambda l: l.get('heading') == "Abbreviations", self.get_text())).pop()

    @staticmethod
    def get_coi():  # coi is an acronym for "Conflicts of Interest"
        """
        This method get the paper's "Conflicts of Interest" declaration
        :return: A str instance corresponding to the paper's "Conflicts of Interest"
        """
        return ''  # TODO: Add a pattern recognition based on a regex


if __name__ == "__main__":
    os.system("")
