'''
Write a program that requests a positive four-digit integer from the user and prints its
digits. You are not allowed to use the string data type operations to do this task.
Your program should simply read the input as an integer and process it as an integer,
using standard arithmetic operations (+, *, -, /, %, etc).

Enter n: 1234
1
2
3
4
'''



n = int(input("Ingrese un número de cuatro dígitos: "))
while n > 0:
    residuo = n % 10 # obtener el último dígito
    print(residuo) # imprimir el dígito
    n = n // 10 # eliminar el último dígito

'''
n1 = 56
n2 = 10
n = n1 % n2
print(n)'''
