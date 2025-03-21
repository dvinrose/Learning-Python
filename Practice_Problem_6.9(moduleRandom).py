'''
Implement function guess() that takes as input an integer n and implements a simple,
interactive number guessing game. The function should start by choosing a random number in the range
from 0 up to but not including n.The function will then repeatedly ask
the user to guess the chosen number; When the user guesses correctly, the function should
print a 'You got it.' message and terminate. Each time the user guesses incorrectly, the
function should help the user by printing message 'Too low.', or 'Too high.'.

guess(100)

Enter your guess: 50
Too low.
Enter your guess: 75
Too high.
Enter your guess: 62
Too high.
Enter your guess: 56
Too low.
Enter your guess: 59
Too high.
Enter your guess: 57
You got it!
'''

import random

def guess(b):
    y = b
    x = random.randint(0,y)
    if x < y/2:
        print("Too low")
    elif x == y:
        print("You got it!")
    else:
        print("Too high")
    print(x)

guess(int(input('Please insert a number: ')))