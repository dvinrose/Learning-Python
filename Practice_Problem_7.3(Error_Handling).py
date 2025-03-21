'''

 Create a “wrapper” function safe_open() for the open() function. Recall that when open()
 is called to open a file that doesn’t exist in the current working directory, an exception is
 raised:

 open('ch7.px', 'r')

 Traceback (most recent call last):
 File "<pyshell#19>", line 1, in <module>
 open('ch7.px', 'r')
 IOError: [Errno 2] No such file or directory: 'ch7.px'

 If the file exist, a reference to the opened file object is returned:

 open('ch7.py', 'r')

 <_io.TextIOWrapper name='ch7.py' encoding='US-ASCII'>

 When safe-open() is used to open a file, a reference to the opened file object should be
 returned if no exception is raised, just like for the open() function. If an exception is raised
 while trying to open the file, safe-open() should return None.

safe-open('ch7.py', 'r')

 <_io.TextIOWrapper name='ch7.py' encoding='US-ASCII'>

safe-open('ch7.px', 'r')

'''

def safe_open():
    try:
        file = open('ch7.px', 'r')
        return file
    except IOError:
        return None

safe_open()

# ------------------------------------------------

def h(n):
    print('Start h')
    try:
        print(1/n)
    except ZeroDivisionError:
        print('Caught!')
    print(n)

def g(n):
    print('Start g')
    h(n-1)
    print(n)

def f(n):
    print('Start f')
    g(n-1)
    print(n)
import sys
# Ejecutar la función f(2)
f(2)

