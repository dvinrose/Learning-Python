'''
2.21 Write an expression involving strings s and t containing the last name and the first name, respectively, of a person that evaluates to the person’s initials.
If the two strings contained the first and last name of this book’s author, the expression would evaluate to 'LP'.
'''

s = 'Lopez' # last name
t = 'Pauline' # first name

initials = s[0] + t[0]
print(initials)
bookAutor = 'Lopez Pauline'

if s in bookAutor and t in bookAutor:
    print("LP")
