'''

Implement function cal() that takes as input a year and a month (a number between 1 and
 12) and starts up a GUI that shows the corresponding calendar. For example, the calendar
 shown is obtained using:

 cal(2012, 2)

 To do this, you will need to compute (1) the day of the week (Monday, Tuesday, . . .) on
 which the first day of the month falls and (2) the number of days in the month (taking into
 account leap years). The function monthrange() defined in the module calendar returns
 exactly those two values:

 from calendar import monthrange
 monthrange(2012, 2) # year 2012, month 2 (February)
 (2, 29)

 The returned value is a tuple. The first value in the tuple, 2, corresponds to Wednesday
 (Monday is 0, Tuesday is 1, etc.). The second value, 29, is the number of days in February
 of year 2012, a leap year.

'''

import tkinter as tk
from calendar import monthrange, month_name


def cal(year, month):
    # Obtener el primer día del mes y el número de días
    first_weekday, num_days = monthrange(year, month)

    # Crear ventana
    root = tk.Tk()
    root.title(f"Calendario - {month_name[month]} {year}")

    # Etiqueta de título
    tk.Label(root, text=f"{month_name[month]} {year}").grid(row=0, column=0, columnspan=7, pady=10)

    # Días de la semana
    days = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
    for i, day in enumerate(days):
        tk.Label(root, text=day,
                       relief="solid",
                       width=6).grid(row=1, column=i)

    # Crear los días del mes
    row = 2
    col = (first_weekday + 1) % 7  # Ajustar porque en calendar, lunes=0
    for day in range(1, num_days + 1):
        tk.Label(root, text=str(day),
                       relief="solid",
                       width=6).grid( row=row,column=col, padx=1, pady=1 )
        col += 1
        if col > 6:
            col = 0
            row += 1

    root.mainloop()
cal(2025, 5)
# Ejemplo:
# cal(2012, 2)
