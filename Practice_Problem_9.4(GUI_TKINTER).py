'''
 Implement a variation of GUI program day.py called day2.py. Instead of displaying the
 weekday message in a separate pop-up window, insert it in front of the date in the entry box,
 as shown. Also add a button labeled “Clear” that erases the entry box.
'''

from tkinter import Tk, Button, Entry, Label, END
from time import strptime, strftime
from tkinter.messagebox import showinfo


def compute():
    '''display day of the week corresponding to date in dateEnt;
    date must have format MMM DD, YYYY (e.g., Jan 21, 1967)'''

    date = dateEnt.get() #  Returns the string inside the entry

    # Comprobar si el campo está vacío (incluso con espacios)
    if not date.strip():
        showinfo(message="Please enter a date.")
        return

    try:
        # Intentar convertir la fecha
        weekday = strftime('%A', strptime(date, '%b %d, %Y'))
        dateEnt.insert(0, weekday + ' ')
    except ValueError:
        # Si el formato es incorrecto, avisar al usuario
        showinfo(message="Incorrect format. Please use 'Jan 21, 1967'.")

def dlt():
    dateEnt.delete(0, END)

root = Tk()
label = Label(root, text='Enter date')
label.grid(row=0, column=0)

dateEnt = Entry(root)
dateEnt.grid(row=0, column=1)

button1 = Button(root, text='Enter', command=compute)
button1.grid(row=1, column=0)

button2 = Button(root, text='Clear', command=dlt)
button2.grid(row=1, column=1)

root.mainloop()
