'''
2.17 Using variables defined in Exercise 2.16, write Boolean expressions corresponding to
the following logical statements and evaluate the expressions:
(a) The sum of 17 and −9 is less than 10.
(b) The length of list inventory is more than five times the length of string fullname.
(c) c is no more than 24.
Chapter 2 Exercises 47
(d) 6.75 is between the values of integers a and b.
(e) The length of string middle is larger than the length of string first and smaller than
the length string last.
(f) Either the list inventory is empty or it has more than 10 objects in it.
'''
inventory = ['paper','staples','pencils']
first = 'John'
middle = 'Fitzgerald'
last = 'Kennedy'
a, b = 6, 7
# A ----------------------------
a = 17 - 9 < 10
print(a)
# B ----------------------------
len_inventory = len(inventory)
fullname = len(first + middle + last)
comparison = len_inventory > fullname
print(comparison)
# C ----------------------------
print(a)
print(b)
c = (( a + b ) / 2) < 24
print("c is no more than 24: ", c)
# D ----------------------------
d = a < 6.75 < b
print("(d) 6.75 is between the values of integers a and b : ", d)
# E ----------------------------
comparison_2 = len(first) < len(middle) < len(last)
print("comparison_2: ", comparison_2)
# F ----------------------------
comparison_3 = 0 == len_inventory > 10
print(comparison_3)