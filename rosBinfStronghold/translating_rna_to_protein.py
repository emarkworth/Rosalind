#!/usr/bin/env python
"""
File Name: translating_rna_to_protein.py
Edited: 05/15/2023

Question 8 of Rosalind BINF Stronghold
Named 'PROT' on the tree view of topic.

Given:
Return:
"""


def translator(string):
    """Translate DNA to Protein"""
    string = string.strip().split()

    return string


if __name__ == "__main__":
    word = translator(" ijas ofdjq")
    print(word)