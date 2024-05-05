'''
3.24 Implement a program that requests a list of words from the user and then prints each
word in the list that is not 'secret'.

Enter list of words: ['cia','secret','mi6','isi','secret']
cia
mi6
isi
'''
emptyList = []
for i in range(5):
    emptyList.append(input("Insert: "))
    # if "secret" in emptyList: # esta fue mi solucion original
    if emptyList[-1] == "secret": # El operador [-1] se usa para acceder al último elemento de la lista
        emptyList.pop()

print(emptyList)

