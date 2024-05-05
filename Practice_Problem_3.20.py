"""
Write a for loop that iterates over a list of strings lst and prints the first three characters of every word.
If lst is the list ['January', 'February', 'March'] then the following should be printed:
Jan
Feb
Mar
"""

lst = ['January', 'February', 'March']

for i in lst:
    print(i[0:3])
