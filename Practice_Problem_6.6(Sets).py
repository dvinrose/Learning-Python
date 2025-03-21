'''

Implement function sync() that takes a list of phone books (where each phone book is a
set of phone numbers) as input and returns a phone book (as a set) containing the union of
all the phone books.

phonebook4 = {'234-56-78', '456-78-90'}
phonebooks = [phonebook1, phonebook2, phonebook3, phonebook4]
sync(phonebooks)

{'234-56-78', '456-78-90', '123-45-67', '345-67-89'}

'''

phonebook1 = set({'234-56-78'})
phonebook2 = set({'234-56-78'})
phonebook3 = set({'345-67-89'})
phonebook4 = set({'434-56-78', '856-78-90'})
phonebooks = [phonebook1, phonebook2, phonebook3, phonebook4]
'''
def sync(phonebooks):
    # Inicializar un conjunto vacío para almacenar la unión de todos los números de teléfono
    union_phonebook = set()

    # Recorrer cada guía telefónica en la lista
    for phonebook in phonebooks:
        # Añadir los números de la guía telefónica actual al conjunto de unión
        union_phonebook.update(phonebook)

    # Devolver el conjunto de unión que contiene todos los números de teléfono
    return union_phonebook

x = sync(phonebooks)
print(x)
'''

def sync(phonebooks):
    phonebook = set()
    for x in phonebooks:
        phonebook = phonebook | x
    return phonebook

x = sync(phonebooks)
print(x)


'''
def sync(phonebooks):
    res = set() # initialize the accumulator
    for phonebook in phonebooks:
        res = res | phonebook # accumulate phonebook into res
    return res

x = sync(phonebooks)

print(x)
'''