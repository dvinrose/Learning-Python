'''
Implement a program that requests the user to enter the x and y coordinates (each
between −10 and 10) of a dart and computes whether the dart has hit the dartboard, a circle
with center (0, 0) and radius 8. If so, string It is in! should be printed on the screen.

Enter x: 2.5
Enter y: 4
It is in!
'''
import math

x = float(input("Enter X: "))
y = float(input("Enter Y: "))

a,b = 0,0
radius = 8

if math.sqrt((x - a)**2 + (y - b)**2) < radius:
    print("It is in!")
else:
    print("It is out!")

