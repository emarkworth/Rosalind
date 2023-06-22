#!/usr/bin/env python
"""
File Name: finding_motif_dna.py
Edited: 06/02/2023

Question 10 of Rosalind BINF Stronghold
Named 'CONS' on the tree view of topic.

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist,
then you may return any one of them.)
Sample Dataset
"""

#################################################
# This script is currently not formatting properly. to get correct formatting, see "proofing_con&prof.py".
# It does give the right answer, however.
#################################################

from sys import argv
from io_utilities import file_handler


def profile(fasta):
    """
    TODO
    :param fasta: TODO
    :return: TODO
    """

    # Make dictionary of nucleotide base lists
    prof_m = {'A': [], 'C': [], 'G': [], 'T': []}

    # Make a list of sequences
    sqlist = []
    seq = ""

    for line in fasta:
        line = line.strip()

        # Don't add headers to sequence construction
        if line.startswith(">"):
            if seq != "":
                # Add sequence being built to list of full sequences if a header is reached
                sqlist.append(seq)
            seq = ""
        else:
            seq += line

    # Catch leftover building sequence
    sqlist.append(seq)

    # Make all bases have lists of length of the seqs
    for base in prof_m:
        prof_m[base] = [0] * len(sqlist[0])

    # For each seq, for each base in seq, +1 to list for position in dictionary
    for full_len_seq in sqlist:
        for num, base in enumerate(full_len_seq):
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
        counts = []
        for v in values:
            v = str(v)
            counts.append(v)
        print(f'{key}: {" ".join(counts)}')


def consensus(prof_matrix):
    """
    Provide the consensus sequence for the DNA string matrix.
    :param prof_matrix: TODO
    :return: TODO
    """
    string_length = 0
    for val in prof_matrix.values():
        string_length = len(val)
    consensus_string = [0] * string_length
    con_count = [0] * string_length

    for key, val in prof_matrix.items():
        for num, v in enumerate(val):
            if v > con_count[num]:
                con_count[num] = v
                consensus_string[num] = key

    print(''.join([str(x) for x in consensus_string]))


if __name__ == "__main__":
    # Print consensus string then profile table
    infile = file_handler(argv[1], "r")

    # Create profile matrix
    pm = profile(infile)

    # Print output
    consensus(pm)
    profile_print(pm)
