'''
Add appropriate docstrings to functions average() and negatives() from Practice Problems 3.9 and 3.12.
Check your work using the help() documentation tool.
You should get, for example:
help(average)
Help on function average in module __main__:
average(x, y)
returns average of x and y
'''

def average( a, b):
    'returns the average of two numbers'
    return (a+b) / 2

print(average( 2, 3.5))

'''---------------------------------------------------'''

List = [4, 0, -1, -3, 6, -9]
def negatives(lst):
    "returns only the negative numbers in the list"
    for i in lst:
        if i < 0:
            print(i)
negatives(List)

help(average)
help(negatives)

