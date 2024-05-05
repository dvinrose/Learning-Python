'''
3.17 Use the eval() function to evaluate these strings as Python expressions:
(a) '2 * 3 + 1'
(b) 'hello'
(c) "'hello' + ' ' + 'world!'"
(d) "'ASCII'.count('I')"
(e) 'x = 5'
'''

a = eval('2 * 3 + 1')
print(a)

#b = eval('hello')
#print(b)

c = eval("'hello' + ' ' + 'world!'")
print(c)

d = eval("'ASCII'.count('I')")
print(d)

e = eval('x = 5')
print(e)

#  name 'hello' is not defined.