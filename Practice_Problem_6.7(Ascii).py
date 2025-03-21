'''
Write a function encoding() that takes a string as input and prints the ASCII code—in
decimal, hex, and binary notation—of every character in it.

encoding('dad')

Char Decimal Hex Binary
d 100 64 1100100
a 97 61 1100001
d 100 64 1100100
'''

def encoding(str):

    dec = ''
    bit = ''
    print('Char    Decimal    Hex    Binary')
    for x in str:
        string = x
        dec_Number = ord(x)
        hex_Number = hex(dec_Number)
        binary_Number = bin(dec_Number)

        print('{:6} {:4}        {:3}   {:8}'.format(string, dec_Number, hex_Number, binary_Number ))
        #print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

encoding(input("Insert String:"))

