'''
Implement a program that requests a positive integer n and prints on the screen all the
positive divisors of n. Note: 0 is not a divisor of any integer, and n divides itself.

Enter n: 49
1
7
49
'''

#my solution
intNumb = int(input("Please enter a number: "))
for i in range(intNumb + 1):
    if i == 0:
        continue

    if intNumb % i == 0:
        print(i)

# ----------------------------------------------------

# not my solution
n = int(input("Ingrese un número: "))
divisores = [i for i in range(1, n//2 + 1) if n % i == 0] + [n]
print("Los divisores de", n, "son:", divisores)
