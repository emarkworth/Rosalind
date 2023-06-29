#!/usr/bin/env python
"""
File Name: fibd.py
Edited: 06/22/2023

Question 11 of Rosalind BINF Stronghold
Named 'FIBD' on the tree view of topic.

Adapted from Kaggle: Rosalind problem solutions.
https://www.kaggle.com/code/mylesoneill/rosalind-problem-solutions/script

Given: Positive integers n≤100 and m≤20.
Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

Rabbits live for three months (they reproduce twice before dying).
"""

from sys import argv


def mortal_fib(n, m):
    """
    A Fibonacci type growth sequence describing rabbit reproduction, with mortal rabbits.
    :param n: Number of months in the sequence.
    :param m: Months that rabbits will rear offspring.
    :return: Number of pairs of rabbits alive at n number of months after the start.
    """
    n = int(n)
    m = int(m)

    pop = [1] + [0] * (m - 1)

    for month in range(n - 1):
        pop = [sum(pop[1:])] + pop[:-1]

    return sum(pop)


if __name__ == "__main__":
    if len(argv) != 3:
        print("\nPlease input: number of days in sequence, number of months a rabbit will rear offspring\n")
        exit(1)

    population = mortal_fib(argv[1], argv[2])
    print(population)
