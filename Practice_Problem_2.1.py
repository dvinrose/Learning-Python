'''
Write Python algebraic expressions corresponding to the following statements:
(a) The sum of the first five positive integers
(b) The average age of Sara (age 23), Mark (age 19), and Fatima (age 31)
(c) The number of times 73 goes into 403
(d) The remainder when 403 is divided by 73
(e) 2 to the 10th power
(f) The absolute value of the difference between Sara’s height (54 inches) and Mark’s height (57 inches)
(g) The lowest price among the following prices: $34.99, $29.95, and $31.50
'''

# (a) The sum of the first five positive integers

first_five_positive_integer = 1 + 2 + 3 + 4 + 5

print("The sum of the first five positive integers is: ", first_five_positive_integer)

# (b) The average age of Sara (age 23), Mark (age 19), and Fatima (age 31)

sara_age = 23
mark_age = 19
fatima_age = 31

average_age = (sara_age + mark_age + fatima_age) / 3

print("the average age is:", average_age)

# (c) The number of times 73 goes into 403
division = 403 // 73

print("The number of times 73 goes into 403: ", division)

# (d) The remainder when 403 is divided by 73

remainder = 403 % 73

print("the remainder is: ", remainder)

# (e) 2 to the 10th power

e = 2**10

print("2 to the 10th power: ", e)

# (f) The absolute value of the difference between Sara’s height (54 inches) and Mark’s height (57 inches)

print("abs of the difference between SarThea’s height (54 inches) and Mark’s height (57 inches): ", abs(54 - 57)) # otra forma
resta = 54 - 57
valor_abs = abs(resta)
print("abs of the difference between SarThea’s height (54 inches) and Mark’s height (57 inches): ", valor_abs)

# (g) The lowest price among the following prices: $34.99, $29.95, and $31.50

print("The lowest price among the following prices: $34.99, $29.95, and $31.50: ", min(34.99, 29.95, 31.50))

