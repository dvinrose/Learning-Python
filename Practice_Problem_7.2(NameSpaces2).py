'''
For each name in the next module, indicate whether
it is a global name or whether it is local
in f(x) or local in g(x).

'''

def f(y):
    x = 2 # local
    return g(x)

def g(y):
    global x
    x = 4 # global
    return x*y

x = 0 # global
res = f(x)
print('x = {}, f(0) = {}'.format(x, res))
