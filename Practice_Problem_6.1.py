'''
Write a function birthState() that takes as input the full name of a recent U.S. president
(as a string) and returns his birth state. You should use this dictionary to store the birth state
for each recent president:
{'Barack Hussein Obama II':'Hawaii',
'George Walker Bush':'Connecticut',
'William Jefferson Clinton':'Arkansas',
'George Herbert Walker Bush':'Massachussetts',
'Ronald Wilson Reagan':'Illinois',
'James Earl Carter, Jr':'Georgia'}
birthState('Ronald Wilson Reagan')
'Illinois'
'''
def birthState(fullName):
     bs_Presidents = {'Barack Hussein Obama II':'Hawaii',
                      'George Walker Bush':'Connecticut',
                      'William Jefferson Clinton':'Arkansas',
                      'George Herbert Walker Bush':'Massachussetts',
                      'Ronald Wilson Reagan':'Illinois',
                      'James Earl Carter, Jr':'Georgia'}
     return bs_Presidents[fullName]

x = birthState('Ronald Wilson Reagan')
print(x)