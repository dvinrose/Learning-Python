'''
Implement a program that requests a nonempty list from the user and prints on the
screen a message giving the first and last element of the list.

Enter a list: [3, 5, 7, 9]
The first list element is 3
The last list element is
'''

ListX = []

for i in range(4):
    ListX.append(input("Please write something, lol: "))


print("The first list element is: ", ListX[0])
print("The last list element is: ", ListX[-1])
