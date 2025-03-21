'''

Define functions f() and g() in this way:
def f(y):
x = 2
print('In f(): x = {}, y = {}'.format(x,y))
g(3)
print('In f(): x = {}, y = {}'.format(x,y))
def g(y):
x = 4
print('In g(): x = {}, y = {}'.format(x,y))
Using Figure 7.1 as your model, show graphically the variables names, their values, and the
namespaces of functions f() and g() during the execution of function g() when this call
is made:
f(1)

'''


def f(y):
    x = 2
    print('In f(): x = {}, y = {}'.format(x,y))
    g(3)
    print('In f(): x = {}, y = {}'.format(x,y))
def g(y):
    x = 4
    print('In g(): x = {}, y = {}'.format(x,y))
    


f(1)
