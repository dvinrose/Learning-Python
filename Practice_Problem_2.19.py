'''
2.19 Start by assigning to variable answers a list containing an arbitrary sequence of strings
'Y' and 'N'. For example:
answers = ['Y', 'N', 'N', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'N', 'N']
Write Python statements corresponding to the following:
(a) Assign to variable numYes the number of occurrences of 'Y' in list answers.
(b) Assign to variable numNo the number of occurrences of 'N' in list answers.
(c) Assign to variable percentYes the percentage of strings in answers that are 'Y'.
(d) Sort the list answers.
(e) Assign to variable f the index of the first occurrence of 'Y' in sorted list answers
'''
answers = ['Y', 'N', 'N', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'N', 'N']
print(answers)
# A ----------------------------
numYes = answers.count('Y')
print(numYes)
# B ----------------------------
numNo = answers.count('N')
print(numNo)
# C ----------------------------
percentYes = (answers.count('Y') / len(answers)) * 100
print(percentYes)
# D ----------------------------
answers.sort()
print(answers)
# E ----------------------------
indexAnswers = answers.index('Y')
print(indexAnswers)