'''
Implement a program that starts by asking the user to enter a login id (i.e., a string). The
program then checks whether the id entered by the user is in the list ['joe', 'sue',
'hani', 'sophie'] of valid users. Depending on the outcome, an appropriate message
should be printed. Regardless of the outcome, your function should print 'Done.' before
terminating. Here is an example of a successful login:

Login: joe
You are in!
Done.

And here is one that is not:
Login: john
User unknown.
Done.
'''

lst = ['joe', 'sue', 'hani', 'sophie']
name = input("Please Write The Name: ")
if name in lst:
    print('You are in!')
else:
    print('User unknown')

print('Done.')
