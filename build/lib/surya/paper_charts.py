# -*- coding: utf-8 -*-

from collections import Counter
import os


def count_papers_per_year(papers_list: list) -> dict:
    """
    Counts number of papers per year in a papers list
    :param papers_list: A list of paper objects
    :return: a dict with each year as key and the corresponding count as value
    """
    years = list(map(lambda p: str(p.get_year()), papers_list))
    return dict(Counter(years))


if __name__ == "__main__":
    os.system("Surya package. Chats data functions source.")
