'''
 Find the random module in one of the directories listed in sys.path, open it, and find the
 implementations of functions randrange(), random(), and sample(). Then import the
 module into the interpreter shell and view its attributes using the dir() function.
'''

import sys
import random

print('-----------')

import sys

# Imprimir todos los elementos en sys.path
#for path in sys.stdlib_module_names:
#    print(path)

for i in dir(sys):
    print(i)

if 'random' in sys.stdlib_module_names:
    print("--------------------------- yes")

import sys
import os

for path in sys.path:
    random_path = os.path.join(path, 'random.py')
    if os.path.exists(random_path):
        print(f"Found random module at: {random_path}")
        break


with open(random_path, 'r') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        if 'def randrange(' in line or 'def random(' in line or 'def sample(' in line:
            print(f"Found implementation at line {i+1}: {line.strip()}")
import random
print(dir(random))

import os
print("Current working directory:", os.getcwd())
print("List of files in current directory:", os.listdir())

print('My name is {}'.format(__name__))