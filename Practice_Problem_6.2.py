'''
Implement function rlookup() that provides the reverse lookup feature of a phone book.
Your function takes, as input, a dictionary representing a phone book. In the dictionary,
phone numbers (keys) are mapped to individuals (values). Your function should provide a
simple user interface through which a user can enter a phone number and obtain the first
and last name of the individual assigned that number.

rphonebook = {'(123)456-78-90':['Anna','Karenina'],
              '(901)234-56-78':['Yu', 'Tsun'],
              '(321)908-76-54':['Hans', 'Castorp']}
rlookup(rphonebook)

Enter phone number in the format (xxx)xxx-xx-xx: (123)456-78-90
('Anna', 'Karenina')
Enter phone number in the format (xxx)xxx-xx-xx: (453)454-55-00
The number you entered is not in use.
Enter phone number in the format (xxx)xxx-xx-xx:
'''
def rlookup():
    rphonebook = {'(123)456-78-90': ['Anna', 'Karenina'],
                  '(901)234-56-78': ['Yu', 'Tsun'],
                  '(321)908-76-54': ['Hans', 'Castorp']}

    while True:
        print(rphonebook.keys())
        number = input('Please enter the number: ')
        if number not in rphonebook:
            print('El número es diferente a todas las llaves del diccionario.')
        print(rphonebook[number])
        break
rlookup()