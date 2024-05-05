'''
2.25 Repeat Problem 2.24 with the following modification: variable grades is defined to
be of type tuple rather than of type list:
grades = ('B','B','F','C','B','A','A','D','C','D','A','A','B')
Variable count should still refer to a list.
'''

grades = ('B','B','F','C','B','A','A','D','C','D','A','A','B')

a = grades.count('A')
b = grades.count('B')
c = grades.count('C')
d = grades.count('D')
f = grades.count('F')

lisCount = [a, b, c, d, f]

print(lisCount)