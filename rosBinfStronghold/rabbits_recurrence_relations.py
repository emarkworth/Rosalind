"""
Question 4 of Rosalind BINF Stronghold

Named 'FIB' on the tree view of topic.


Given: Positive integers n≤40 and k≤5.
Return: The total number of rabbit pairs that will be present after n months,
if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k
rabbit pairs (instead of only 1 pair).
"""

from functools import lru_cache

# Given input
# 5 3

# Expected output
# 19


#  Fn=Fn−1+Fn−2 (with F1=F2=1 to initiate the sequence)
@lru_cache
def fib_calc(num):
    #n = 5
    k = 4

    counter = 1
    while counter <= num:
        if num <= 2:
            counter += 1
            return 1

        else:
            counter += 1
            return (k * fib_calc(num - 2)) + fib_calc(num - 1)

print(fib_calc(2))

# one: 1
# two: 1
# three: 4
# four: 7
# five: 19
