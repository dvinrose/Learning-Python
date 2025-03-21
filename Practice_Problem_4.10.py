'''
Implement function myGrep() that takes as input two strings, a file name and a target string,
and prints every line of the file that contains the target string as a substring.
myGrep('example.txt', 'line')
The 3 lines in this file end with the new line character.
There is a blank line above this line.
'''

def myGrep(file_Name, strinfo):
    file_Name = open(file_Name, 'r')
    for eachLine in file_Name:
        print(eachLine, end= ' ')

myGrep('example.txt', 'line')
