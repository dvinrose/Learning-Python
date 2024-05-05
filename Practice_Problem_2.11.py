'''
Write Python expressions corresponding to these statements:
(a) The sum of negative integers −7 through −1
(b) The average age of a group of kids at a summer camp given than 17 are 9 years old,
24 are 10 years old, 21 are 11 years old, and 27 are 12 years old
(c) 2 to the power −20
(d) The number of times 61 goes into 4356
(e) The remainder when 4365 is divided by 61
'''

# A # -----------------------------------------------
x = - 7 - 1
print(x)
# B # -----------------------------------------------
kids_9 = 17
kids_10 = 24
kids_11 = 21
kids_12 = 27
Total_People = kids_9 + kids_10 + kids_11 + kids_12
Grouping = kids_9 * 9 + kids_10 * 10 + kids_11 * 11 + kids_12 * 12
Average_Kids_Age = Grouping/Total_People
print(Average_Kids_Age)
# C # -----------------------------------------------
Powering = 2**-20
print("2 to the power −20 is:", Powering)
# D # -----------------------------------------------
Number_Of_Times = 4356 // 61
print("The number of times 61 goes into 4356 is: ", Number_Of_Times)
# E # -----------------------------------------------
Remainder = 4365 % 61
print("The remainder when 4365 is divided by 61 is: ", Remainder)