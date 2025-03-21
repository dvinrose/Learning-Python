'''

Implement function lookup() that implements a phone book lookup application. Your
function takes, as input, a dictionary representing a phone book. In the dictionary, tuples
containing first and last names of individual (the keys) are mapped to strings containing
phone numbers (the values). Here is an example:

phonebook = {('Anna','Karenina'):'(123)456-78-90',
('Yu', 'Tsun'):'(901)234-56-78',
('Hans', 'Castorp'):'(321)908-76-54'}

Your function should provide a simple user interface through which a user can enter the first
and last name of an individual and obtain the phone number assigned to that individual.

lookup(phonebook)

Enter the first name: Anna
Enter the last name: Karenina
(123)456-78-90
Enter the first name: Yu
Enter the last name: Tsun
(901)234-56-78

'''

phonebook = {('Anna','Karenina'):'(123)456-78-90',
('Yu', 'Tsun'):'(901)234-56-78',
('Hans', 'Castorp'):'(321)908-76-54'}

def lookup(phonebook):

    Fname = input("Enter the first name:")
    Sname = input("Enter the last name:")

    for key, value in phonebook.items():
        for Fname in key:
            if Fname in key[0] and Sname in key[1]:
                print(value)

        # clave es una tupla, así que podemos acceder a sus elementos
        #print(f"First Name: {clave[0]}, Last Name: {clave[1]}, Number: {valor}")

lookup(phonebook)

print(len(phonebook))

