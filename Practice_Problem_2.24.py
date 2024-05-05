'''
2.24 Start by assigning to variable grades a list containing an arbitrary sequence of grades
(strings) 'A', 'B', 'C', 'D', and 'F'. For example:
grades = ['B','B','F','C','B','A','A','D','C','D','A','A','B']
Write a sequence of Python statements that ultimately produce a list count that contains
the numbers of occurrences of each grade in list grades in alphabetic order. For the given
example, the list count should be [4, 4, 2, 2, 1].
'''

grades = ['B','B','F','C','B','A','A','D','C','D','A','A','B']

a = grades.count('A')
b = grades.count('B')
c = grades.count('C')
d = grades.count('D')
f = grades.count('F')

lisCount = [a, b, c, d, f]

print(lisCount)