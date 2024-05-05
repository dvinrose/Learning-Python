'''
Implement a program that requests an integer n from the user and prints on the screen
the squares of all numbers from 0 up to, but not including, n.

Enter n: 3
0
1
4
'''

numberInt = int(input("Please enter a number: "))

for i in range(numberInt):
    x = i ** 2
    if i == numberInt:
        break
    print(x)