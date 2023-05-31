#!/usr/bin/env python
"""
File Name: translating_rna_to_protein.py
Edited: 05/15/2023

Question 8 of Rosalind BINF Stronghold
Named 'PROT' on the tree view of topic.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s.
"""

from sys import argv
from io_utilities import translator


def dna_to_protein(seq):
    """Translate DNA to Protein"""

    # Handle seqs of all lengths except 0
    if len(seq) % 3 == 0:
        pass
    elif len(seq) % 3 == 1:
        seq = seq[:-1]
        print("\nWarning: Input sequence is not a multiple of 3.\n")
    elif len(seq) % 3 == 2:
        seq = seq[:-2]
        print("\nWarning: Input sequence is not a multiple of 3.\n")

    codons = []
    amino_str = ''

    # iterate though codons
    for start in range(0, len(seq), 3):
        codon = seq[start: start + 3]
        codons.append(codon)

    for c in codons:
        if translator(c) == 'Stop':
            return amino_str
        else:
            amino_str += translator(c)

    print("Warning: no stop codon detected.\n")
    return amino_str


if __name__ == "__main__":
    if len(argv) != 2:
        exit("Please input exactly one sequence")
        # Future proofing: allow input to come from file instead of command line
    word = dna_to_protein(argv[1])
    print(word)
