'''
Translate these into Python if/else statements:
(a) If year is divisible by 4, print 'Could be a leap year.'; otherwise print 'Definitely not
a leap year.'
(b) If list ticket is equal to list lottery, print 'You won!'; else print 'Better luck next
time...'
'''

# A -------------------------------
year = 400
if year%4 == 0:
    print("Could be a leap year")
else:
    print("Definitely not a leap year")
# B -------------------------------
lottery = [3,4,6,4,7,9]
ticket = [3,4,6,4,7,9]
if lottery == ticket:
    print("You won")
else:
    print("Better luck next time...!")