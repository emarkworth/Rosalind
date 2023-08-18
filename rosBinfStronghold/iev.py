#!/usr/bin/env python
"""
File Name: iev.py
Edited: 08/17/2023

Question 13 of Rosalind BINF Stronghold
Named 'IEV' on the tree view of topic.

Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples
in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the
number of couples having the following genotypes:

    1. AA-AA
    2. AA-Aa
    3. AA-aa
    4. Aa-Aa
    5. Aa-aa
    6. aa-aa

Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption
that every couple has exactly two offspring.
"""

from sys import argv


def exp_ofsp(p_types):
    """

    :return:
    """

    # Provide expected dominant offspring amounts for each genotype-couple (AA-AA or AA-Aa, etc.)
    probabilities = {1: 2, 2: 2, 3: 2, 4: 1.5, 5: 1, 6: 0}

    # Instate value for summing offspring count
    offspring = 0

    for count, pair in enumerate(p_types):
        offspring += (probabilities[count + 1] * int(pair))

    return offspring


if __name__ == "__main__":
    if len(argv) != 7:
        print("Needs quantities of the 6 types of parents")
        exit(1)

    inlist = (argv[1], argv[2], argv[3], argv[4], argv[5], argv[6])

    print(exp_ofsp(inlist))
