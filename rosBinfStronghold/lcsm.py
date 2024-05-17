#!/usr/bin/env python
"""
File Name: lcsm.py
Edited: 04/04/2023

Question in Rosalind BINF Stronghold.
Named 'LCSM' on the tree view of topic.

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
"""

from sys import argv
from io_utilities import file_handler
from Bio import SeqIO


def longest_ss(infile):
    """
    Function takes a fasta file and returns the longest common string of the sequences.
    :param infile: A typical fasta file.
    :return: A string.
    """
    # Store seqs
    seqs = []
    for seq in SeqIO.parse(infile, "fasta"):
        seqs.append(seq.seq)

    # Store
    substrings = {}


    #print(num, sequence)
    first_seq_sub_seqs = index_first_seq(seqs[0], 4)
    print(first_seq_sub_seqs)


    print("CGTA" in "ACGTACGT")
    #sub_str = []
     #for start in range(0, len(sequence)):
        #sub_str.append(sequence[start: start + 3])
        #substrings[num + 1] = sub_str

    #for seq, ss in substrings.items():
    #u = substrings[0].union(substrings[])

    # for each substring, if it matches substring in another seq, extend it until it doesn't match
    # store matching substring in a dict as key, store length as value
    #print(substrings)
    return


def index_first_seq(first_seq, seq_length):
    """
    Breaks up a sequence into subseqs of set length, returns them.
    :param first_seq: The first sequence in a fasta file. Used as "seed" to find possible common strings.
    param seq_length: To adjust the length of substrings the sequences should be split into.
    :return: List of subseqs, in order.
    """
    subseqs = []

    for start in range(0, len(first_seq) - seq_length + 1):
        subseqs.append(first_seq[start:start+seq_length])

    return subseqs


if __name__ == "__main__":
    if len(argv) != 2:
        print("Must give a fasta file for parsing.")
        exit(1)

    fasta = file_handler(argv[1], "r")
    ls = longest_ss(fasta)
    #print(ls[0])
