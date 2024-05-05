'''
Start by executing
s = 'goodbye'
Then write a Boolean expression that checks whether:
(a) The first character of string s is 'g'
(b) The seventh character of s is 'g'
(c) The first two characters of s are 'g' and 'a'
(d) The next to last character of s is 'x'
(e) The middle character of s is 'd'
(f) The first and last characters of string s are equal
(g) The last four characters of string s match the string 'tion'
Note: These seven statements should evaluate to True, False, False, False, True, False,
and False, respectively.
'''
s = "goodbye"
# A ----------------------------
a = s[0] == "g"
print("(a) The first character of string s is 'g': " , a)
# B ----------------------------
#b = s[7] == "g"

# C ----------------------------
c = s[:2]  == "ga"
print("The first two characters of s are 'g' and 'a' : " , c)
# D ----------------------------
d = s[-1:] == "x"
print("(d) The next to last character of s is 'x' : " , d)
# E ----------------------------
e = s[3] == "d"
print("(e) The middle character of s is 'd' : " , e)
# F ----------------------------
f = min(s) == max(s)
print("(f) The first and last characters of string s are equal : ", f)
# G ----------------------------
g = s[4:] == "tion"
print("(g) The last four characters of string s match the string 'tion' : ", g)
