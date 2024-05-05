'''
Write Python expressions using s1, s2, and s3 and operators + and * that evaluate to:
(a) 'ant bat cod'
(b) 'ant ant ant ant ant ant ant ant ant ant '
(c) 'ant bat bat cod cod cod'
(d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat '
(e) 'batbatcod batbatcod batbatcod batbatcod batbatcod '
'''

s1 = "ant"
s2 = "bat"
s3 = "cod"

# (a) 'ant bat cod'
a = s1 + " " + s2 + " " + s3

# (b) 'ant ant ant ant ant ant ant ant ant ant '
b = (s1 + " ") * 10

# (c) 'ant bat bat cod cod cod'
c = s1 + " " + s2 + " " + s2 + " " + ((s3 + " ") *3)

# (d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat '
d = (s1 + " " +  s2 + " ") * 7

# (e) 'batbatcod batbatcod batbatcod batbatcod batbatcod '
e = (((s2 * 2) + s3) + " ") * 5

# ---------------------------------------------------

print(a), print(b), print(c), print(d), print(e)
