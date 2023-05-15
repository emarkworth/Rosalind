#!/usr/bin/env python
"""
File Name: mendels_first_law.py
Edited: 05/10/2023

Question 7 of Rosalind BINF Stronghold
Named 'IPRB' on the tree view of topic.

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant
allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""


def main():
    """Logic"""
    # 2 2 2 returns 0.78333
    k = float(input("Enter k value: "))
    m = float(input("Enter m value: "))
    n = float(input("Enter n value: "))

    # Establish population size
    pop = k + m + n

    # P(k + m(k) + m(m * 0.75) + m(n * 0.5) + n(k) + n(m * 0.5) )
    pk = k / pop
    pmk = (m / pop) * (k / (k + (m - 1) + n))
    pmm = (m / pop) * ((m - 1) / (k + (m - 1) + n)) * 0.75
    pmn = (m / pop) * (n / (k + m + (n - 1))) * 0.5
    pnk = (n / pop) * (k / (k + m + (n - 1)))
    pnm = (n / pop) * (m / (k + m + (n - 1))) * 0.5

    return pk + pmk + pmm + pmn + pnk + pnm


if __name__ == "__main__":
    prob = main()
    print(f"{prob:.5f}")
