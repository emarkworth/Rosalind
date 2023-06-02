#!/usr/bin/env python
"""
File Name: finding_motif_dna.py
Edited: 05/31/2023

Question 9 of Rosalind BINF Stronghold
Named 'SUBS' on the tree view of topic.

Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s
"""

from sys import argv
from io_utilities import file_handler


def motif(template=str, substring=str):
    """
    Return all locations of substrings as they occur in the template.
    :param template: DNA sequence to be parsed for substrings. Larger string.
    :param substring: DNA motif to be found within template at any amount of locations.
    :return:
    """
    for start in range(0, len(template) - len(substring) + 1):
        if substring == template[start: start + len(substring)]:
            print(start + 1)

    return


if __name__ == "__main__":
    file = file_handler(argv[1], "r")
    file_objs = []
    for line in file:
        line = line.strip()
        file_objs.append(line)
    motif(file_objs[0], file_objs[1])
