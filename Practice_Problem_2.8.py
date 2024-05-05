"""
In what order are the operators in the following expressions evaluated?
(a) 2 + 3 == 4 or a >= 5
(b) lst[1] * -3 < -10 == 0
(c) (lst[1] * -3 < -10) in [0, True]
(d) 2 * 3**2
(e) 4 / 2 in [1, 2, 3]
"""

# (a) 2 + 3 == 4 or a >= 5
a = (( 2 + 3 ) == 4) or ( a >= 5 )  # correcto
a = 5 == 4 or ( a >= 5 )
a = False or ( a >= 5)

# (b) lst[1] * -3 < -10 == 0
b = ((lst[1] * -3 ) < -10) == 0 # correcto
b = -3 < -10 == 0
b = False == 0
b = True

# (c) (lst[1] * -3 < -10) in [0, True]
c = ((lst[1] * -3) < (-10)) in [0, True] # correcto
c = -3 < -10 in [0, True]
c = False in [0, True]
c = False

# (d) 2 * 3**2
d = 2 * 3**2
d = (2 * (3**2)) # correcto
d = 2 * 9
d = 18

# (e) 4 / 2 in [1, 2, 3]
e = 4 / 2 in [1, 2, 3]
e = (4 / 2) in [1, 2, 3] # correcto
e = 2 in [1, 2, 3]
e = True
