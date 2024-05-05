'''
2.26 A dartboard of radius 10 and the wall it is hanging on are represented using the two dimensional coordinate system, with the board’s center at coordinate (0, 0).
Variables x and y store the x- and y- coordinate of a dart hit. Write an expression using variables x and y
that evaluates to True if the dart hits (is within) the dartboard, and evaluate the expression
for these dart coordinates:
(a) (0, 0)
(b) (10, 10)
(c) (6, −6)
(d) (−7, 8)
'''

import math

coordinates = [
    (0, 0),
    (10, 10),
    (6, -6),
    (-7, 8)
]

boardRadius = math.sqrt(10**2)
# A ----------------------------
distance = math.sqrt(coordinates[0][0]**2 + coordinates[0][1]**2) <= boardRadius
print("A: ",distance)
# B ----------------------------
distance = math.sqrt(coordinates[1][0]**2 + coordinates[1][1]**2) <= boardRadius
print("B: ", distance)
# C ----------------------------
distance = math.sqrt(coordinates[2][0]**2 + coordinates[2][1]**2) <= boardRadius
print("C: ", distance)
# C ----------------------------
distance = math.sqrt(coordinates[3][0]**2 + coordinates[3][1]**2) <= boardRadius
print("D: ", distance)
