'''
Implement a program that requests a positive integer n from the user and prints the
first four multiples of n.

Enter n: 5
0
5
10
15
'''

number_int = int(input("Please enter a number: "))

def mult(x):
    for i in range(4):
        x = number_int * i
        print(x)

mult(number_int)
