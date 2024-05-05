'''
2.20 Write an expression involving a three-letter string s that evaluates to a string whose
characters are the characters of s in reverse order. If s is 'top', the expression should
evaluate to 'pot'
'''

s = 'top'
reversed_String = s[::-1] # specifies slicing from the beginning to the end, with a step of -1, effectively reversing the order.
# notacion de slicing, se usa para extraer indices de una cadena

print(reversed_String)