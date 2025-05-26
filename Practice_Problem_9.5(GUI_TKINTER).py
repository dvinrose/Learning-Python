'''

 In the original day.py program, the user has to click button “Enter” after typing a date in
 the entry box. Requiring the user to use the mouse right after typing his name using the
 keyboard is an inconvenience. Modify the program day.py to allow the user just to press
 the Enter/Return keyboard key instead of clicking the button “Enter”

'''
from tkinter import Tk, Button, Entry, Label, END
from tkinter.messagebox import showinfo
from tkinter import font
from time import strptime, strftime

def compute():
    date = dateEnt.get()
    if not date.strip():
        showinfo(message="Please enter a date.")
        return

    try:
        weekday = strftime('%A', strptime(date, '%b %d, %Y'))
        dateEnt.insert(0, weekday + ' ')
    except ValueError:
        showinfo(message="Incorrect format. Please use 'Jan 21, 1967'.")

def dlt():
    dateEnt.delete(0, END)

def rturn(event):
    compute()

root = Tk()
label = Label(root, text='Enter date')
label.grid(row=0, column=0)

# Fuente en negrita
bold_font = font.Font(weight="bold", size=10)

dateEnt = Entry(root, width=30, font=bold_font)
dateEnt.bind('<Return>', rturn)
dateEnt.grid(row=0, column=1, ipady=7)  # ipady ajusta la altura visual

button1 = Button(root, text='Enter', command=compute, font=bold_font)
button1.grid(row=1, column=0)

button2 = Button(root, text='Clear', command=dlt, font=bold_font)
button2.grid(row=1, column=1)

root.mainloop()
