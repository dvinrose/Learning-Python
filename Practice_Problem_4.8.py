'''
Write function stringCount() that takes two string inputs—a file name and a target string—
and returns the number of occurrences of the target string in the file.
stringCount('example.txt', 'line')
4
'''

def stringCount(x, s):
    document = open(x)
    content = document.read()
    document.close()
    return content.count(s)

x = stringCount('example.txt', 'line')
print(x)