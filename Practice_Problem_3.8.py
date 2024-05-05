'''
Define, directly in the interactive shell, function perimeter() that takes, as input, the radius of a circle
(a nonnegative number) and returns the perimeter of the circle. A sample usage is:
>>> perimeter(1)
6.283185307179586
>>> perimeter (2)
12.566370614359172
Remember that you will need the value of π (defined in module math) to compute the
perimeter.
'''

import math
def perimeter(radius):
    perimeter = 2*math.pi*radius
    return perimeter

x = perimeter(2)
print(x)
