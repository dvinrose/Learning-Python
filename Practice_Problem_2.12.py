'''
Start by evaluating, in the interactive shell, the assignment:
#>>> s1 = '-'
#>>> s2 = '+'
Now write string expressions involving s1 and s2 and string operators + and * that evaluate
to:
(a) '-+'
(b) '-+-'
(c) '+––'
(d) '+––+––'
(e) '+––+––+––+––+––+––+––+––+––+––+'
(f) '+–+++––+–+++––+–+++––+–+++––+–+++––'
Try to make your string expressions as succinct as you can.
'''
s1 = '-'
s2 = '+'
s3 = "--+-+++"
s4_mix = s2 + s1
# A # -----------------------------------------------
print("A: ",s1 + s2)
# B # -----------------------------------------------
print("B: ", s1 + s2 + s1)
# C # -----------------------------------------------
print("C: ", s2 + (s1 * 2))
# D # -----------------------------------------------
print("D: ", (s2 + (s1 * 2)) * 2)
# E # -----------------------------------------------
print("E: ", (s2 + (s1 * 2)) * 10 + s2)
# F # -----------------------------------------------
print("F: ", s4_mix + (s2 * 3) + (s3 * 4) + (s1 * 2))