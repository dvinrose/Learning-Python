'''Implement function roster() that takes a list containing student information and prints
out a roster, as shown below. The student information, consisting of the student’s last name,
first name, class, and average course grade, will be stored in that order in a list. Therefore,
the input list is a list of lists. Make sure the roster printed out has 10 slots for every string
value and 8 for the grade, including 2 slots for the decimal part.

students = []
students.append(['DeMoines', 'Jim', 'Sophomore', 3.45])
students.append(['Pierre', 'Sophie', 'Sophomore', 4.0])
students.append(['Columbus', 'Maria', 'Senior', 2.5])
students.append(['Phoenix', 'River', 'Junior', 2.45])
students.append(['Olympis', 'Edgar', 'Junior', 3.99])
roster(students)

Last First Class Average Grade
DeMoines Jim Sophomore 3.45
Pierre Sophie Sophomore 4.00
Columbus Maria Senior 2.50
Phoenix River Junior 2.45
Olympia Edgar Junior 3.99
'''
students = []
students.append(['DeMoines', 'Jim', 'Sophomore', 3.45])
students.append(['Pierre', 'Sophie', 'Sophomore', 4.0])
students.append(['Columbus', 'Maria', 'Senior', 2.5])
students.append(['Phoenix', 'River', 'Junior', 2.45])
students.append(['Olympis', 'Edgar', 'Junior', 3.99])

def roster(students):
#'prints average grade for a roster of students'
    print('\nLast First Class Average Grade\n')
    for student in students:
        print('{:10}{:10}{:10}{:8.2f}'.format(student[0], student[1], student[2], student[3]))
       
roster(students)