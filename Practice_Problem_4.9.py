'''
Write function words() that takes one input argument—a file name—and returns the list
of actual words (without punctuation symbols !,.:;?) in the file.
words('example.txt')
['The', '3', 'lines', 'in', 'this', 'file', 'end', 'with',
'the', 'new', 'line', 'character', 'There', 'is', 'a',
'blank', 'line', 'above', 'this', 'line']
'''

def words(file_Name):
    file_Name = open(file_Name, 'r')
    content = file_Name.read()
    file_Name.close()
    table = content.maketrans('!,.:;?', 6 * ' ')
    content = content.translate(table)
    content = content.lower()
    print(content)
    return content.split()

x = words('example.txt')
print(x)

file_Name = open('example.txt')
for line in file_Name:
    print(line,end='')
