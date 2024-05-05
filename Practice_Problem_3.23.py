'''
Write for loops that use the function range() and print the following sequences:
(a) 0 1
(b) 0
(c) 3 4 5 6
(d) 1
(e) 0 3
(f) 5 9 13 17 21
'''

# a
for i in range(2):
    print(i)
# b
for i in range(1):
    print(i)
# c
for i in range(3,7):
    print("(3 4 5 6):",i)
# d
for i in range(1,2):
    print(i)
# e
for i in range(0,4,3):
    print("(0, 3):",i)
# f
for i in range(5,22,4):
    print("(5 9 13 17 21):",i)
