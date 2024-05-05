'''
Write the for loop that will print the following sequences of numbers, one per line.
(a) Integers from 3 up to and including 12
(b) Integers from 0 up to but not including 9, but with a step of 2 instead of the default
of 1 (i.e., 0, 2, 4, 6, 8)
(c) Integers from 0 up to but not including 24 with a step of 3
(d) Integers from 3 up to but not including 12 with a step of 5
'''

# A -------------------------------------
for i in range(3, 13):
    print(i)
# B -------------------------------------
for i in range(0, 9, 2):
    print(i)
# C -------------------------------------
for i in range(0, 24, 3):
    print(i)
# D -------------------------------------
for i in range(3, 12, 5):
    print(i)
