'''
What is the type of the object that these expressions evaluate to?
(a) False + False
(b) 2 * 3**2.0
(c) 4 // 2 + 4 % 2
(d) 2 + 3 == 4 or 5 >= 5
'''

# (a) False + False
a = bool # While the two operands are Boolean, the + operator is an int operator, not a bool
         # operator. The result (0) is an int value.
         # so i did this wrong, it's not bool, it's int
print(a)
# (b) 2 * 3**2.0

b = float # correcto

# (c) 4 // 2 + 4 % 2

c = int # correcto

# (d) 2 + 3 == 4 or 5 >= 5

d = bool # correcto