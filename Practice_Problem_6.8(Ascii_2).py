'''
Write function char(low, high) that prints the characters corresponding to ASCII
decimal codes i for all values of i from low up to and including high.
char(62, 67)
62 : >
63 : ?
64 : @
65 : A
66 : B
67 : C
'''

def char():
    low = int(input("low:"))
    high = int(input("high:"))
    for i in range(low, 1 + high):
        print(f'{i} : {chr(i)}')


char()