'''
Suppose a nonempty list team has been assigned. Write a Python statement or statements
that swap the first and last value of the list. So, if the original list is:
team = ['Ava', 'Eleanor', 'Clare', 'Sarah']
then the resulting list should be:
team
['Sarah', 'Eleanor', 'Clare', 'Ava']
'''

team = ['Ava', 'Eleanor', 'Clare', 'Sarah']
team[0], team[3] = team[3], team[0]
print(team)

