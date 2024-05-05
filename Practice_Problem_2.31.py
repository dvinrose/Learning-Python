'''
2.31 In this chapter we have covered some, but not all, methods of class list. Using the
following interactive session as an aid, explain in your own words what the list methods
extend(), copy(), and clear() do.
>> lst = [2, 3, 4]
>> lst.extend([5, 6])
>> lst
[2, 3, 4, 5, 6]
>> lst2 = lst.copy()
>> lst2
[2, 3, 4, 5, 6]
>> lst.clear()
>> lst
[]
>> lst2
[2, 3, 4, 5, 6]
'''

lst = [2, 3, 4]
lst.extend([5, 6]) # this method adds some values at the end of list lst
print(lst)

lst2 = lst.copy()
print("printing the copy of list 1: ", lst2)

lst.clear() # this method cleans the list
print("cleaning the list: ",lst)

print("printing the copy of list 1 again: ",lst2)


# Crear una tupla con cuatro elementos de diferentes tipos
tupla = (1, "hola", 3.14, [1, 2, 3])
print(tupla)