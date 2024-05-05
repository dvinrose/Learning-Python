'''
2.22 The range of a list of numbers is the largest difference between any two numbers in the
list. Write a Python expression that computes the range of a list of numbers lst. If the list
lst is, say, [3, 7, -2, 12], the expression should evaluate to 14 (the difference between
12 and −2).
'''

lisR = [7, 7, -2, 12]
v = 0

for i in range(min(lisR),max(lisR)):
    v = v + 1

print(v)
