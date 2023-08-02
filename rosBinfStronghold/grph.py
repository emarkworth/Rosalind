#!/usr/bin/env python
"""
File Name: grph.py
Edited: 06/28/2023

Question 12 of Rosalind BINF Stronghold
Named 'GRPH' on the tree view of topic.

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
Return: The adjacency list corresponding to O3. You may return edges in any order.

!!!! DECODED: the prompt is pretty much asking to find the sequences which overlap with each other, using the tail of
one seq and the start of another. The length of the tail and starts are always of length k, which in this case
is set to 3.
"""

from io_utilities import file_handler
from sys import argv
from Bio import SeqIO


def adjacency(fasta, k):
    """
    Take a fasta file and return adjacencies of O3.
    :param fasta: A file containing fasta formatted DNA sequences.
    :return: Adjacent sequences of O3 in the fasta.
    """

    k = int(k)

    seqs = []

    # Get headers in seqs and put in list
    for seq_rec in SeqIO.parse(fasta, "fasta"):
        seqs.append(seq_rec)

    # iterate through seqs to get tails
    for s in seqs:
        t = s.seq[len(s.seq) - k::]

        # Iterate through seqs again to match tails to heads, exclude matching tail to own head
        for s2 in seqs:
            if t == s2.seq[:k:] and s.id != s2.id:
                print(s.id, s2.id)

    return


if __name__ == "__main__":
    if len(argv) != 3:
        print("Input requires a DNA fasta file and k length.")
        exit(1)

    infile = file_handler(argv[1], "r")
    adjacency(infile, argv[2])
