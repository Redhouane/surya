#!/Users/redhouaneabdellaoui/anaconda/envs/DrEA/bin/python python
# -*- coding: utf-8 -*-


import os


# Fonction de concatenation des paths
def _opj(path_1, path_2):
    """
    Join two paths.
    :param path_1: First part of destination directory path.
    :param path_2: Second part of destination directory path.
    :return: A path made by the join of path_1 and path_2.
    """
    return os.path.join(path_1, path_2)


if __name__ == "__main__":
    _opj(path_1="/Test", path_2="/Done")
    os.system("")
