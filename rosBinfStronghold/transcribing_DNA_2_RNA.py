"""
Question 2 of Rosalind BINF Stronghold

Named 'RNA' on the tree view of topic.


Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
"""

# Given input
# GATGGAACTTGACTACGTAAATT

# Expected output
# GAUGGAACUUGACUACGUAAAUU

instring = str(input())
print(instring.replace('T', 'U'))