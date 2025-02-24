#!/usr/bin/env python
"""
File Name: protein_mass_prtm.py
Edited: 02/19/2025

Question in Rosalind BINF Stronghold.
Named 'PRTM' on the tree view of topic.

Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table .
"""

mass_table = {'A': 71.03711,
              'C': 103.00919,
              'D': 115.02694,
              'E': 129.04259,
              'F': 147.06841,
              'G': 57.02146,
              'H': 137.05891,
              'I': 113.08406,
              'K': 128.09496,
              'L': 113.08406,
              'M': 131.04049,
              'N': 114.04293,
              'P': 97.05276,
              'Q': 128.05858,
              'R': 156.10111,
              'S': 87.03203,
              'T': 101.04768,
              'V': 99.06841,
              'W': 186.07931,
              'Y': 163.06333}


def main(aa_in):
    """
    Calculate mass from input Amino Acid chain
    :param aa_in: an Amino Acid chain specified by the user
    :return: mono-isotopic mass of the Amino acid chain
    """
    amino_acids = [i.upper() for i in aa_in]

    mass = 0
    for i in amino_acids:
        mass += mass_table[i]

    print(f"{mass: .3f}")


if __name__ == "__main__":
    aa_input = input("Amino Acid: ")
    main(aa_input)
