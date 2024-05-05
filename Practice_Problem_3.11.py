'''
Implement function allEven() that takes a list of integers
and returns True if all integers in the list are even, and False otherwise.
allEven([8, 0, -2, 4, -6, 10])
True
allEven([8, 0, -1, 4, -6, 10])
False
'''
'''
 # Hice este ejercicio por mi cuenta, pero recibi ayuda,
 # por lo tanto al no estar satisfecho decidi resolverlo de otra manera por mi cuenta
 
def allEven(lst): 
        x = all( i%2 == 0 for i in lst)
        return x
print(allEven([0, 0, -4, 4, -6, 10]))
'''
integer_List = [8, 0, -1, 4, -6, 10]
def allEven(List):
       for i in List:
          if i%2 != 0:
            return False
       return True
x = allEven(integer_List)
print(x)