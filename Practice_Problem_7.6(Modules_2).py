'''
Add code to module example.py that calls the functions defined in the module and prints
 the values of variables defined in the module. The code should execute when the module is
 run as a top-level module only, such as when it is run from the shell:

 Testing module example:
 Executing f()
 Executing g()
'''

def f():
    print('Executing f()')


def g():
    print('Executing g()')


if __name__ == '__main__':
    f()
    g()

# --- --- --- --- --- --- --- --- ---

def f(x):
    return 2 * x + 1

print(f(3))

