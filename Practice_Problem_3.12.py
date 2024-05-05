'''
Write function negatives() that takes a list as input and prints, one per line, the negative
values in the list. The function should not return anything.
negatives([4, 0, -1, -3, 6, -9])
-1
-3
-9
'''

List = [4, 0, -1, -3, 6, -9]
def negatives(lst):
    for i in lst:
        if i < 0:
            print(i)

negatives(List)
