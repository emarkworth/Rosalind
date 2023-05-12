"""
Question 3 of Rosalind BINF Stronghold

Named 'REVC' on the tree view of topic.


Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s.
"""

# Given input
# AAAACCCGGT

# Expected output
# ACCGGGTTTT

compliment = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

instring = str(input())

new_string = [compliment[base] for base in instring]

outstring = ''.join(new_string[::-1])

print(outstring)