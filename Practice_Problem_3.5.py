'''
Implement a program that requests from the user a list of words (i.e., strings) and then prints
on the screen, one per line, all four-letter strings in the list.
>>>
Enter word list: ['stop', 'desktop', 'top', 'post']
stop
post
'''

list = ['stop', 'desktop', 'top', 'post']

for lst in list:
    if len(lst) == 4:
        print(lst)
