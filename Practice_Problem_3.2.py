'''
Translate these conditional statements into Python if statements:
(a) If age is greater 62, print 'You can get your pension benefits'.
(b) If name is in list ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'],
print 'One of the top 5 baseball players, ever!'.
(c) If hits is greater than 10 and shield is 0, print 'You are dead...'.
(d) If at least one of the Boolean variables north, south, east, and west is True, print
'I can escape.'.
'''
# A --------------------------------
age = 63
if age > 62:
    print("You can get your pension benefits")
# B --------------------------------
lst = ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']
name = input("insert the name: ")
if name in lst:
    print('One of the top 5 baseball players, ever!')
# C --------------------------------
hits = 10
shield = 0
if hits == 10 and shield == 0:
    print("You are dead...")
# D --------------------------------
north,south,east,west = True, False,False,False
if north or south or east or west == True:
    print('I can escape.')