'''
 Write a program peaceandlove.py that creates this GUI:

 The “Peace &Love” text label should be pushed to the left and have a black background
 of size to fit 5 rows of 20 characters. If the user expands the window, the label should remain
 right next to the left border of the window. The peace symbol image label should be pushed
 to the right. However, when the user expands the window, white padding should fill the
 space created. The picture shows the GUI after the user manually expanded it.

'''

from tkinter import Tk, Label, PhotoImage, BOTTOM, LEFT, RIGHT, RIDGE

root = Tk()

        #widget Label can be used to display text inside a window

'''The first argument in this Label constructor,
   named master, specifies that the Label 
   widget will live inside widget root.'''

# transform GIF image to a format tkinter can display


text = Label(master=root,
             font=('Helvetica', 16, 'bold italic'),
             foreground='white',# letter color
             background='black',# background color
             padx=5,  # widen label 25 pixels left and right
             pady=20, # widen label 10 pixels up and down
             text='Peace and love.')
text.pack(side = LEFT) # push label down

peace = PhotoImage(file='peace.png')
peaceLabel = Label(root,
                   borderwidth=3, # label border width
                   background='white',
                   relief=RIDGE, # label border style
                   image=peace)
peaceLabel.pack(expand= True, fill = 'both')  # push label left

root.mainloop()

'''
 The option expand, which can be
 set to True or False, specifies whether the widget should be allowed to expand to fill any
 extra space inside the master. If option expand is set to True, option fill can be used to
 specify whether the expansion should be along the x-axis, the y-axis, or both.'''


'''En Tkinter, los tres métodos principales 
para gestionar la geometría de los widgets son:

pack() → Organiza los widgets en bloques dentro
 de su contenedor, permitiendo alinearlos de forma
vertical u horizontal.

grid() → Coloca los widgets en una estructura 
de filas y columnas, similar a una tabla.

place() → Permite posicionamiento absoluto, 
donde los widgets se ubican en coordenadas 
específicas dentro del contenedor.'''

'''One simple way to specify
 the placement of a widget inside its master is to invoke method pack() on the widget. The
 method pack() can take arguments that specify the desired position of the widget inside its
 master; without any arguments, it will use the default position, which is to place the widget
 centered and against the top boundary of its master'''




