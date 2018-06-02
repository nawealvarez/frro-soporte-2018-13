from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def Suma():
    n1 = float(caja1.get())
    n2 = float(caja2.get())
    suma = n1+n2
    messagebox.showinfo("Mensaje", "El resultado  de la suma es: %.2f" % suma)
    caja1.delete(0, 20)
    caja2.delete(0, 20)


        # Metodo para calcular la resta
def Resta():
    n1 = float(caja1.get())
    n2 = float(caja2.get())
    resta = n1-n2
    messagebox.showinfo("Mensaje", "El resultado de la resta es: %.2f" % resta)
    caja1.delete(0, 20)
    caja2.delete(0, 20)


# Metodo para calcular la multiplicacion
def Multiplicacion():
    n1 = float(caja1.get())
    n2 = float(caja2.get())
    multi = n1*n2
    messagebox.showinfo("Mensaje", "El resultado de la multiplicacion es: %.2f" % multi)
    caja1.delete(0, 20)
    caja2.delete(0, 20)


# Metodo para calcular la division
def Division():
    n1 = float(caja1.get())
    n2 = float(caja2.get())
    div = n1/n2
    messagebox.showinfo("Mensaje", "El resultado de la divison es: %.2f" % div)
    caja1.delete(0, 20)
    caja2.delete(0, 20)


calc = Tk()
calc.geometry("330x180")

calc.title("Mini-calculadora")

# Creacion primer etiqueta
var1 = StringVar()
var1.set("Primer Operando")
etiq1 = Label(calc, textvariable=var1, height=2, foreground='blue')
etiq1.place(x=10, y=10)


numero1 = StringVar()
caja1 = Entry(calc, bd=4, textvariable=numero1)
caja1.place(x=10, y=40)

# Creacion de otra etiqueta
var2 = StringVar()
var2.set("Segundo Operando")
etiq2 = Label(calc, textvariable=var2, height=1, foreground='blue')

etiq2.place(x=10, y=70)

# Creacion de otra caja de texto para el segundo numero
numero2 = StringVar()
caja2 = Entry(calc, bd=4, textvariable=numero2)
caja2.place(x=10, y=100)

# Boton para la suma
boton1 = Button(calc, text="+", command=Suma, width=5)
boton1.place(x=140, y=70)

# Boton para la resta
boton2 = Button(calc, text="-", command=Resta, width=5)
boton2.place(x=187, y=70)

# Boton para multiplicacion
boton3 = Button(calc, text="x", command=Multiplicacion, width=5)
boton3.place(x=237, y=70)

# Boton para la division
boton4 = Button(calc, text="/", command=Division, width=5)
boton4.place(x=287, y=70)

# Cargar Calculadora
calc.mainloop()

