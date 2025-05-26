'''

 Implement a GUI app that contains two buttons labeled “Localtime” and “Greenwichtime”.
 When the first button is pressed, the local time should be printed in the shell. When the second
 button is pressed, the Greenwich Mean Time should be printed.

 Local time
 Day: 08 Jul 2011
 Time: 13:19:43 PM

 Greenwich time
 Day: 08 Jul 2011
 Time: 18:19:46 PM

 You can obtain the current Greenwich Mean Time using the function gmtime() from module time.

'''

from tkinter import Tk, Button
from time import strftime, localtime, gmtime

def click_LocalTime():
    print("Local time")
    """Imprime la fecha y hora actual."""
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n', localtime())
    print(time)

def click_GreenwichTime():
    print("Greenwich time")
    """Imprime la fecha y hora actual."""
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n', gmtime())
    print(time)

root = Tk()

# Crear botón con etiqueta 'Click it' y asociar evento al hacer clic
button1 = Button(root, text='Localtime', command=click_LocalTime)
button1.pack()

button2 = Button(root, text='Greenwichtime', command=click_GreenwichTime)
button2.pack()

root.mainloop()
