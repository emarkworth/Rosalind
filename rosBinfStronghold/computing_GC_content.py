#!/usr/bin/env python
"""
File Name: computing_GC_content.py
Edited: 05/10/2023

Question 5 of Rosalind BINF Stronghold
Named 'GC' on the tree view of topic.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on
absolute error below.
"""

from Bio import SeqIO
from io_utilities import gc_content
from sys import argv


def main(input_file):
    """Parse though seqs in a fasta file, run "gc_content" function, keep track of the highest GC seq"""
    # Tracker for most gc rich seq in file
    most_gc_percent = 0.0
    most_gc_str = ''

    for seq_rec in SeqIO.parse(input_file, "fasta"):
        if gc_content(seq_rec.seq) > most_gc_percent:
            most_gc_str = seq_rec.id
            most_gc_percent = gc_content(seq_rec.seq)
        else:
            pass

    return most_gc_percent, most_gc_str


if __name__ == "__main__":
    gc_percent, gc_str = main(argv[1])
    print(gc_str)
    print(f'{100 * gc_percent:.6f}')
