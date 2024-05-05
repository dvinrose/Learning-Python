'''
Translate the following statements into Python Boolean expressions and evaluate them:
(a) The sum of 2 and 2 is less than 4.
(b) The value of 7 // 3 is equal to 1 + 1.
(c) The sum of 3 squared and 4 squared is equal to 25.
(d) The sum of 2, 4, and 6 is greater than 12.
(e) 1387 is divisible by 19.
(f) 31 is even. (Hint: what does the remainder when you divide by 2 tell you?)
(g) The lowest price among $34.99, $29.95, and $31.50 is less than $30.00.
'''

# (a) The sum of 2 and 2 is less than 4.

sum = 2 + 2 < 4
print("The sum of 2 and 2 is less than 4: ", sum)

# (b) The value of 7 // 3 is equal to 1 + 1.

var = 7 // 3 == 1 + 1
print("The value of 7 // 3 is equal to 1 + 1: ", var)

# (c) The sum of 3 squared and 4 squared is equal to 25.

sum = ((3**2) + (4**2)) == 25
print("The sum of 3 squared and 4 squared is equal to 25: ", sum)

# (d) The sum of 2, 4, and 6 is greater than 12.

sum = (2 + 4 + 6) > 12
print("The sum of 2, 4, and 6 is greater than 12: ", sum)

# (e) 1387 is divisible by 19.

div = 1387 / 19 # mi error, la respuesta correcta es 1389 % 19, siendo el resultado 0
print("1387 is divisible by 19: ", div)

# (f) 31 is even. (Hint: what does the remainder when you divide by 2 tell you?)

s = 31 % 2
print("the remainder tell us when a number is even or not when the output is 0, "
      "\nin this case we can see 31 is odd: ", s)

# (g) The lowest price among $34.99, $29.95, and $31.50 is less than $30.00.

lowest_price = (min(34.99, 29.95, 31.50) < 30)
print("The lowest price among $34.99, $29.95, and $31.50 is less than $30.00: ", lowest_price)