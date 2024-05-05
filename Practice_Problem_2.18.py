'''
2.18 Write Python statements corresponding to the following:
(a) Assign to variable flowers a list containing strings 'rose', 'bougainvillea', 'yucca', 'marigold', 'daylilly', and 'lilly of the valley'.
(b) Write a Boolean expression that evaluates to True if string 'potato' is in list flowers, and evaluate the expression.
(c) Assign to list thorny the sublist consisting of the first three objects in list flowers.
(d) Assign to list poisonous the sublist consisting of just the last object of list flowers.
(e) Assign to list dangerous the concatenation of lists thorny and poisonous.
'''
# A ----------------------------
flowers = ['rose','bougainvillea','yucca','marigold','daylilly','lilly of the valley']
# B ----------------------------
evaluation = "potato" in flowers
print(evaluation)
# C ----------------------------
thorny = flowers[0:3]
print(thorny)
# D ----------------------------
poisonous = flowers[4:6]
print(poisonous)
# E ----------------------------
dangerous = thorny + poisonous
print(dangerous)