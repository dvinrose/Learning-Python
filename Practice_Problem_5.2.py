'''
Write a function named powers() that takes a positive integer n as input and prints, on the
screen, all the powers of 2 from 2**1 to 2**n

powers(6)
2 4 8 16 32 64
'''

def powers(n):
    for i in range(1, n):
        print(2**i, end=', ')

powers(6)