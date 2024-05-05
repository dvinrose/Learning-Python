'''
Write Python expressions corresponding to the following:
(a) The length of the hypotenuse in a right triangle whose other two sides have lengths a and b
(b) The value of the expression that evaluates whether the length of the above hypotenuse is 5
(c) The area of a disk of radius a
(d) The value of the Boolean expression that checks whether a point with coordinates
 x and y is inside a circle with center (a, b) and radius r
'''

# A # -----------------------------------------------
import math
a = int(input("please insert side a:"))
b = int(input("please insert side b:"))
hypotenuse_Value = math.sqrt(a ** 2 + b ** 2)
print("The lenght of the hypotenuse in a right triangle is: ", hypotenuse_Value)
# B # -----------------------------------------------
if hypotenuse_Value == 5:
    print("yes,,, The length of the hypotenuse is 5")
else:
    print("The lenght of the hypotenuse isn't 5")

# C # ----------------------------------------------- Formula of a disk of radius a: A = pi*a**2
a = int(input("Please insert the radius of the disk to calculate the area: "))
A = math.pi * (a ** 2)
print("The area of a disk of radius a is: ", A)

# D # -----------------------------------------------
a, b = 0, 0

x = int(input("Please insert the coordenate X of the point: "))
y = int(input("Please insert the coordenate Y of the point: "))
r = int(input("Please insert the radius of the circle: "))
if math.sqrt(((x - a) ** 2) + ((y - b) ** 2)) < r:
    print("The point is inside the circle")
else:
    print("The point is not inside the circle")
