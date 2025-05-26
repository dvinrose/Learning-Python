import tkinter as tk

root = tk.Tk()
root.title("Cohete apuntando a la derecha")

canvas = tk.Canvas(root, width=400, height=200, bg="skyblue")
canvas.pack()

# Cuerpo del cohete (rectángulo horizontal)
canvas.create_rectangle(50, 80, 200, 120, fill="gray", outline="black")

# Punta del cohete (triángulo apuntando a la derecha)
canvas.create_polygon(200, 80, 240, 100, 200, 120, fill="red", outline="black")

# Aletas traseras (triángulos pequeños hacia abajo y arriba)
canvas.create_polygon(50, 80, 30, 70, 50, 100, fill="blue", outline="black")
canvas.create_polygon(50, 120, 30, 130, 50, 100, fill="blue", outline="black")

# Ventana del cohete
canvas.create_oval(120, 90, 140, 110, fill="white", outline="black")

root.mainloop()
