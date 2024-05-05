'''
Given the list of student homework grades
grades = [9, 7, 7, 10, 3, 9, 6, 6, 2]
write:
(a) An expression that evaluates to the number of 7 grades
(b) A statement that changes the last grade to 4
(c) An expression that evaluates to the maximum grade
(d) A statement that sorts the list grades
(e) An expression that evaluates to the average grade
'''
grades = [9, 7, 7, 10, 3, 9, 6, 6, 2]

#(a) An expression that evaluates to the number of 7 grades
a = grades[1] # incorrecto, correct = grades.count(7)
print(a)

#(b) A statement that changes the last grade to 4
grades[8] = 4 # correcto, otra forma de hacerlo es grades[-1] = 4
print(grades)

#(c) An expression that evaluates to the maximum grade
c = max(grades) # correcto
print("the maximum grade: ", c)

#(d) A statement that sorts the list grades
grades.sort() # correcto
print(grades)

#(e) An expression that evaluates to the average grade
e = sum(grades) / len(grades) # correcto
print("the average grade is: ", e)

# rich educated old man