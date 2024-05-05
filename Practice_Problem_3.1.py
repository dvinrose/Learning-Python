'''
Implement a program that requests the current temperature in degrees Fahrenheit from the
user and prints the temperature in degrees Celsius using the formula
celsius = 5/9(fahrenheit − 32)
Your program should execute as follows:
Enter the temperature in degrees Fahrenheit: 50
The temperature in degrees Celsius is 10.0
'''

fahrenheit = int(input("Please insert the current temperature in Fahrenheit: "))
celsius = 5/9*(fahrenheit - 32)
print(celsius)