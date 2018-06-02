from tkinter import *


class Calculator:
    def clearall(self):
        self.e.delete(0, END)

    def action(self, num):
        self.e.insert(END, num)

    def equal(self):
        try:
            self.igual = self.e.get()
            self.equialidad=eval(self.igual)
            self.e.delete(0, END)
            self.e.insert(END, self.equialidad)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(END, 'DATA ERRROR')

    def __init__(self, ventana):
        ventana.title("Calculadora")
        ventana.geometry("300x190")
        # Entrada de texto
        self.e = Entry(ventana, width=40)
        self.e.grid(row=0, column=0, columnspan=4, pady=3)
        self.e.focus_set()


ventana = Tk()
objeto = Calculator(ventana)

# Botones numeros
Button(ventana, text="0", width=8, height=2, command=lambda: objeto.action(0)).grid(column=1, row=4)
botUno = Button(ventana, text="1", width=8, height=2, command=lambda: objeto.action(1))
botDos = Button(ventana, text="2", width=8, height=2, command=lambda: objeto.action(2))
botTres = Button(ventana, text="3", width=8, height=2, command=lambda: objeto.action(3))
botCuatro = Button(ventana, text="4", width=8, height=2, command=lambda: objeto.action(4))
botCinco = Button(ventana, text="5", width=8, height=2, command=lambda: objeto.action(5))
botSeis = Button(ventana, text="6", width=8, height=2, command=lambda: objeto.action(6))
botSiete = Button(ventana, text="7", width=8, height=2, command=lambda: objeto.action(7))
botOcho = Button(ventana, text="8", width=8, height=2, command=lambda: objeto.action(8))
botNueve = Button(ventana, text="9", width=8, height=2, command=lambda: objeto.action(9))

# Botones operadores
botSuma = Button(ventana, text="+", width=8, height=2, command=lambda: objeto.action('+'))
botResta = Button(ventana, text="-", width=8, height=2, command=lambda: objeto.action('-'))
botMultiplicacion = Button(ventana, text="x", width=8, height=2, command=lambda: objeto.action('*'))
botDivision = Button(ventana, text="/", width=8, height=2, command=lambda: objeto.action('/'))
botIgual = Button(ventana, text="=", width=8, height=2, command=objeto.equal)
Button(ventana, text="AC", width=8, height=2, command=objeto.clearall).grid(column=0, row=4)

# Aparicion de botones
botSiete.grid(column=0, row=1)
botOcho.grid(column=1, row=1)
botNueve.grid(column=2, row=1)
botSuma.grid(column=3, row=1)

botCuatro.grid(column=0, row=2)
botCinco.grid(column=1, row=2)
botSeis.grid(column=2, row=2)
botResta.grid(column=3, row=2)

botUno.grid(column=0, row=3)
botDos.grid(column=1, row=3)
botTres.grid(column=2, row=3)
botMultiplicacion.grid(column=3, row=3)

botDivision.grid(column=2, row=4)
botIgual.grid(column=3, row=4)


ventana.mainloop()
