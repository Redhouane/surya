# -*- coding: utf-8 -*-

import os


class Paper:
    """
    The Paper class collects the information related to an article (Texts, Metadata, Title).
    """

    def __init__(self):
        self.title = ""
        self.year = ""
        self.abstract = ""
        self.text = ""
        self.authors = ""
        self.references = ""

    def get_title(self) -> str:
        """
        Get the paper's title.
        :return: The paper's title.
        """

        return self.title

    def get_year(self) -> str:
        """
        Get the paper's year.
        :return: The paper's year.
        """

        return self.year

    def get_abstract(self) -> str:
        """
        Get the paper's abstract.
        :return: The paper's abstract.
        """

        return self.abstract

    def get_sections_texts(self) -> str:
        """
        Get the paper's texts by section.
        :return: A list of json strings (as dicts) corresponding to the paper's texts.
        Each dict contains a section (associated to the "heading" key) and the section content (with the "text" value).
        """

        return self.text

    def get_authors(self) -> str:
        """
        Get the paper's authors
        :return: A list of json strings (as dicts) corresponding to the paper's authors.
        Each dict contains author (with the "name" key) and affiliation as a list (with the "affiliations" value).
        """

        return self.authors

    def get_references(self) -> str:
        """
        Get the paper's references
        :return: A list of json strings (as dicts) corresponding to the paper's references.
        Each dict contains reference's title (associated to the "title" key), authors as a list (with the "authors"
        key), journal's name (associated to the "venue" key) and reference's year as integer (associated to the "year"
        key).
        """

        return self.references

    def get_paper_citation_infos(self) -> dict:
        """
        Get information related to a paper (title, fst author, year and journal
        :return: a dictionary with these information
        """

        infos_dict = {
            'title': self.get_title(),
            'first_author': dict(self.get_authors()[0])['name'],
            'year': self.get_year(),
            'journal': 'Coming Soon'  # TODO: Find a way to parse the journal's name
        }
        return infos_dict

    def get_sections_names(self) -> list:
        """
        Get section's names from the paper
        :return: A str list of sections names
        """

        return list(map(lambda texts_list: texts_list.get('heading'), self.get_sections_texts()))

    def get_sections_texts_list(self, sections_selection=None) -> list:  # "None" if section's dict has no 'heading'
        """
        Get a list of texts corresponding to paper's sections content
        :param sections_selection: A list of desired sections names
        :return: A list of str corresponding to the paper's sections selection contents
        """

        paper_sections = self.get_sections_texts()

        if sections_selection is None or len(sections_selection) == 0:
            all_sections_names = self.get_sections_names()

            # Filtering of sections handled with "None" value and corresponding to free article's texts
            all_sections = list(filter(lambda l: l.get('heading') in all_sections_names, paper_sections))
            return list(map(lambda l: l.get('text'), all_sections))
        else:
            sections_list = list(filter(lambda l: l.get('heading') in sections_selection, paper_sections))
            return list(map(lambda l: l.get('text'), sections_list))

    def get_sections_texts_str(self, sections_names=None) -> str:
        """
        Get the text corresponding to a given list of paper's sections
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

    def get_keywords(self) -> list:
        """
        Get the paper's related keywords
        :return: A list corresponding to the paper's keywords
        """

        return list(
            filter(lambda l: l.get('heading') == "KEYWORDS", self.get_sections_texts())
        ).pop().get('text').split(';')

    def get_abbreviations(self) -> dict:
        """
        Get the paper's abbreviations
        :return: A dict corresponding to the paper's abbreviations
        """

        return list(filter(lambda l: l.get('heading') == "Abbreviations", self.get_sections_texts())).pop()

    @staticmethod
    def get_coi():  # coi is an acronym for "Conflicts of Interest"
        """
        This method get the paper's "Conflicts of Interest" declaration
        :return: A str instance corresponding to the paper's "Conflicts of Interest"
        """

        return ''  # TODO: Add a pattern recognition based on a regex


if __name__ == "__main__":
    os.system("Surya package. Paper class source.")
