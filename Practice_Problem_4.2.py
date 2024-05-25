'''
Assuming that variable forecast has been assigned string
'It will be a sunny day today'
write Python statements corresponding to these assignments:
(a) To variable count, the number of occurrences of string 'day' in string forecast.
(b) To variable weather, the index where substring 'sunny' starts.
(c) To variable change, a copy of forecast in which every occurrence of substring
'sunny' is replaced by 'cloudy'.
'''

forecast = 'It will be a sunny day today'

# A -----
count = forecast.count("day")
print(count)
# B -----
weather = forecast.index("sunny")
print(weather)
# C -----
change = forecast.replace("sunny","cloudy")
print(change)

print(4, 1.5, "hello", sep=";")


