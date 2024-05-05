'''
2.27 A ladder put up right against a wall will fall over unless put up at a certain angle less
than 90 degrees. Given variables length and angle storing the length of the ladder and the
angle that it forms with the ground as it leans against the wall, write a Python expression
involving length and angle that computes the height reached by the ladder. Evaluate the
expression for these values of length and angle:
(a) 16 feet and 75 degrees
(b) 20 feet and 0 degrees
(c) 24 feet and 45 degrees
(d) 24 feet and 80 degrees
Note: You will need to use the trig formula:
height = length ∗ sin(angle)
The math module sin() function takes its input in radians. You will thus need to convert
the angle given in degrees to the angle given in radians using:
radians =
π ∗ degrees
180
'''

import math
# A ----------------------------
degrees = 75
length = 16
radians = ( math.pi * degrees ) / 180 # The math module sin() function takes its input in radians. You will thus need to convert
                                      # the angle given in degrees to the angle given in radians using:
angle = radians
height = length * math.sin(angle)
print("height A: ", height)
# B ----------------------------
degrees = 0
length = 20
radians = ( math.pi * degrees ) / 180 # The math module sin() function takes its input in radians. You will thus need to convert
                                      # the angle given in degrees to the angle given in radians using:
angle = radians
height = length * math.sin(angle)
print("height B: ", height)
# C ----------------------------
degrees = 45
length = 24
radians = ( math.pi * degrees ) / 180 # The math module sin() function takes its input in radians. You will thus need to convert
                                      # the angle given in degrees to the angle given in radians using:
angle = radians
height = length * math.sin(angle)
print("height C: ", height)
# D ----------------------------
degrees = 80
length = 24
radians = ( math.pi * degrees ) / 180 # The math module sin() function takes its input in radians. You will thus need to convert
                                      # the angle given in degrees to the angle given in radians using:
angle = radians
height = length * math.sin(angle)
print("height D: ", height)

t = 5
r = type(t)
print(r)