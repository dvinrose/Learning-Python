import time
'''
Start by setting t to be the local time 1, 500, 000, 000 seconds from the start of January 1,
1970 UTC:

import time
t = time.localtime(1500000000)

Construct the next strings by using the string time format function strftime():
(a) 'Thursday, July 13 2017'
(b) '09:40 PM Central Daylight Time on 07/13/2017'
(c) 'I will meet you on Thu July 13 at 09:40 PM.'
'''

print(time.strftime('%A %b /%d /%y %I:%M %p', time.localtime()))

import time
t = time.localtime(1500000000)

# A --------------

print(time.strftime('%A, %B %d %Y', time.localtime(1500000000)))

# B --------------

print(time.strftime('%I:%M %p Central Daylight Time on %y/%d/%Y', time.localtime(1500000000)))

# C --------------

print(time.strftime('I will meet you on %a %B %d at %I:%M %p', time.localtime(1500000000)))
