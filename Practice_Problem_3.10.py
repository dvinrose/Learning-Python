'''
Implement function noVowel() that takes a string s as input and returns True if no character in s is a vowel,
and False otherwise (i.e., some character in s is a vowel).
noVowel('crypt')
True
noVowel('cwm')
True
noVowel('car')
False
'''
'''---------------------------------------------------------------------------------'''
''' SOLUTION 1'''
def noVowel(s):
    # Definir una lista de vocales en mayúsculas y minúsculas
    vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    # Recorrer cada caracter de la cadena s
    for c in s:
        # Si el caracter es una vocal, devolver False
        if c in vocales:
            return False
    # Si se termina el bucle sin encontrar una vocal, devolver True
    return True
print(noVowel('hyk'))
'''---------------------------------------------------------------------------------'''
''' SOLUTION 2'''
def noVowels(s):
    # Vowel list
    vocales = ["a", "e", "i", "o", "u"]
    # Bucle for para recorrer cada caracter de s
    for c in s:
        # Bucle for para recorrer cada vocal de la lista
        for v in vocales:
            # si el caracter es igual a la vocal, se devuelve false
            if c == v:
                return False

print(noVowel("crypt")) # True
print(noVowel("car")) # False