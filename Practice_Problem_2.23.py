'''
2.23 Start by assigning to variables monthsL and monthsT a list and a tuple, respectively,
both containing strings 'Jan', 'Feb', 'Mar', and 'May', in that order. Then attempt the
following with both containers:
(a) Insert string 'Apr' between 'Mar' and 'May'.
(b) Append string 'Jun'.
(c) Pop the container.
(d) Remove the second item in the container.
(e) Reverse the order of items in the container.
(f) Sort the container.
Note: when attempting these on tuple monthsT you should expect errors.
'''

monthsL = ['Jan', 'Feb', 'Mar', 'May']
monthsT = ('Jan', 'Feb', 'Mar', 'May')
# A ----------------------------
monthsL.insert(3, "Apr")
print(monthsL)
# B ----------------------------
monthsL.append('Jun')
print(monthsL)
# C ----------------------------
monthsL.pop()
print(monthsL)
# D ----------------------------
monthsL.reverse()
print(monthsL)
# E ----------------------------
monthsL.sort()
print(monthsL)

# ===

monthsT.insert(3, "Apr")
print(monthsL)