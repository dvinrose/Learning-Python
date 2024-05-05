'''
2.30 Using an example of your own, explicitly convert some string to a list. Describe, in
your own words, the behavior of the list constructor on a string input
'''

s = "la palabra que se traduce"
translator = list(s) # This function just convert a type value into another
print(translator)

# --------------------------------------------------------

translator = s.split(" ") # SEPARATING WORD BY WORD
print(translator)
