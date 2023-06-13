#!/usr/bin/env python
"""
File Name: finding_motif_dna.py
Edited: 06/02/2023

Question 10 of Rosalind BINF Stronghold
Named 'CONS' on the tree view of topic.

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
Sample Dataset
"""

from sys import argv
from io_utilities import file_handler


def profile(fasta):
    """
    TODO
    :param fasta: TODO
    :return: TODO
    """

    # Make dictionary of nucleotide base lists
    counter = 0
    prof_m = {'A': [], 'C': [], 'G': [], 'T': []}

    for line in fasta:
        line = line.strip()
        counter += 1

        # Just count seq length from first seq (Line 2)
        if counter == 2:
            # Make all bases have lists of length of the seqs
            for b in prof_m:
                prof_m[b] = [0] * len(line)
            for num, base in enumerate(line):
                # For each seq, for each base in seq, +1 to list for position in dictionary
                prof_m[base][num] += 1

        elif not line.startswith(">"):
            for num, base in enumerate(line):
                # For each seq, for each base in seq, +1 to list for position in dictionary
                prof_m[base][num] += 1

    # Return dictionary of nuc base lists
    return prof_m


def profile_print(prof_mat):
    """
    Print profile matrix.
    :param prof_mat:
    :return:
    """
    for key, values in prof_mat.items():
        counts = ''
        for v in values:
            v = str(v)
            counts += v
            counts += ' '
        print(f'{key}: {counts}')


def consensus(prof_matrix):
    """
    Provide the consensus sequence for the DNA string matrix.
    :param prof_matrix: TODO
    :return: TODO
    """
    #for val in prof_matrix.values():
        #print(len(val))
    consensus_string = ''
    con_count = [0]
    print(consensus_string)


if __name__ == "__main__":
    # Print consensus string then profile table
    infile = file_handler(argv[1], "r")

    # Create profile matrix
    pm = profile(infile)

    # Print output
    consensus(pm)
    profile_print(pm)

