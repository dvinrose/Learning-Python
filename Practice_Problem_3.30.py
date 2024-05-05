'''
Implement a program that requests four numbers (integer or floating-point) from the
user. Your program should compute the average of the first three numbers and compare the
average to the fourth number. If they are equal, your program should print 'Equal' on the
screen.

Enter first number: 4.5
Enter second number: 3
Enter third number: 3
Enter last number: 3.5
Equal
'''
listNums = []
for i in range(4):
    listNums.append(float(input("Enter a number: ")))

s = sum(listNums[0:3])
print("la suma de los datos en la lista es: ", s)

average = s/3
print("El promedio entre los 3 primeros datos en la lista es: ", average)

if listNums[3] == average:
    print("They are equal")
else:
    print("Ther are not equal")