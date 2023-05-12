#!/usr/bin/env python
"""
File Name: counting_point_mutations.py
Edited: 05/10/2023

Question 6 of Rosalind BINF Stronghold
Named 'HAMM' on the tree view of topic.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
"""


def main():
    """Find Hamming distance between two strings.
    @param: string one
    @param: string two
    @return: hamming distance"""

    print("This program compares the hamming distance (or number of character differences) between two strings of same "
          "length.")
    str_one = input(f"Input string one: ")
    str_two = input(f"Input string two: ")

    if len(str_one) != len(str_two):
        exit("Strings must be of the same length.")

    ham_dist = 0

    # Mismatches at same indexes in strings add 1 to hamming distance value
    for num, char in enumerate(str_one):
        if char != str_two[num]:
            ham_dist += 1

    return ham_dist


if __name__ == "__main__":
    ham = main()
    print(ham)
