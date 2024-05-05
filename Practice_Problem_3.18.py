'''
3.18 Assume a, b, and c have been defined in the interactive shell as shown:
a, b, c = 3, 4, 5
Within the interactive shell, write if statements that print 'OK' if:
(a) a is less than b.
(b) c is less than b.
(c) The sum of a and b is equal to c.
(d) The sum of the squares a and b is equal to c squared.
'''

a, b, c = 3, 4, 5
# A
if a < b:
    print("ok")
else:
    print("not ok")
# B
if c < b:
    print("ok")
else:
    print("not ok")
# C
if (a+b) == c:
    print("ok")
else:
    print("not ok")
# D
if (a**2 + b**2) == c**2:
    print("ok")
else:
    print(" not ok")