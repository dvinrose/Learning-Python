'''
Implement function swapFL() that takes a list as input and swaps the first and last elements of the list.
You may assume the list will be nonempty. The function should not return anything.
ingredients = ['flour', 'sugar', 'butter', 'apples']
swapFL(ingredients)
ingredients
['apples', 'sugar', 'butter', 'flour']
'''

ingredients = ['flour', 'sugar', 'butter', 'apples']

def swapFL(lst):
    lst[0], lst[3] = lst[3], lst[0]

swapFL(ingredients)
print(ingredients)