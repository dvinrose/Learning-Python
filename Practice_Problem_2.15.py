'''
2.15 Write Python expressions corresponding to these statements:
(a) The number of characters in the word "anachronistically" is 1 more than the number
of characters in the word "counterintuitive."
(b) The word "misinterpretation" appears earlier in the dictionary than the word "misrepresentation."
(c) The letter "e" does not appear in the word "floccinaucinihilipilification."
(d) The number of characters in the word "counterrevolution" is equal to the sum of the
number of characters in words "counter" and "resolution."
'''

# A ----------------------------
a = len("anachronistically")
b = len("counterintuitive")
n = a > b
print(a)
print(b)
print(n)
# B ----------------------------
a = "misinterpretation"
b = "misrepresentation"
k = a < b
print(k)
# C ----------------------------
z = "e" in "floccinaucinihilipilification"
print(z)
# D ----------------------------
a = len("counterrevolution")
b = len("counter")
c = len("resolution")
d = a == c + b
print(d)
