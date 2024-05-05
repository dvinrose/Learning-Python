'''
2.29 Add one or more pairs of parentheses to each expression so that it evaluates to True.
(a) 0 == 1 == 2
(b) 2 + 3 == 4 + 5 == 7
(c) 1 < -1 == 3 > 4
For each expression, explain in what order the operators were evaluated.
'''

# A ----------------------------
a = 0 == (1 == 2)
print(a)
# B ----------------------------
b = 2 + (3 == 4) + 5 == 7
print(b)
# C ----------------------------
c = (1 < -1) == (3 > 4)
print(c)