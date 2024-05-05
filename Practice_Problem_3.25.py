'''
Implement a program that requests a list of student names from the user and prints
those names that start with letters A through M.

Enter list: ['Ellie', 'Steve', 'Sam', 'Owen', 'Gavin']
Ellie
Gavin
'''

listAM = []
list_Input = []
separator = ' '

for letra in range(0, 5): # NAMES
    list_Input.append(input("Please Enter a name: "))

# ------------------------------

import string
for letra in string.ascii_uppercase: # FIRST LETTER
    listAM.append(letra)
    if letra == 'M':
        break

'''
The join method in Python works by joining the elements of an iterable
(such as a list, string, or tuple) by a string separator 
(the string on which the join method is called) and returns the concatenated string.
'''

abcAM = separator.join(listAM) # Join Method
print(abcAM)

for i in list_Input: # MATCHING
    for x in listAM:
       if i[0] == x:
           print(i)