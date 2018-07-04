import tkinter
from tkinter import ttk


class Formulario(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize_user_interface()

    def initialize_user_interface(self):
        """
        Dibuja una interfaz de usuario, donde este ingresa elementos
        """
        self.parent.title("Formulario Ciudades")
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.config(background="lavender")

        self.dose_label = tkinter.Label(self.parent, text="Nombre:")
        self.dose_entry = tkinter.Entry(self.parent)
        self.dose_label.grid(row=0, column=0, sticky=tkinter.W)
        self.dose_entry.grid(row=0, column=1)

        self.modified_label = tkinter.Label(self.parent, text="Codigo Postal:")
        self.modified_entry = tkinter.Entry(self.parent)
        self.modified_label.grid(row=1, column=0, sticky=tkinter.W)
        self.modified_entry.grid(row=1, column=1)

        self.submit_button = tkinter.Button(self.parent, text="Insert", command=self.insert_data)
        self.submit_button.grid(row=2, column=1, sticky=tkinter.W)
        self.exit_button = tkinter.Button(self.parent, text="Exit", command=self.parent.quit)
        self.exit_button.grid(row=0, column=3)

        self.submit_button = tkinter.Button(self.parent, text="Delete", command=self.delete_data)
        self.submit_button.grid(row=5, column=3, sticky=tkinter.W)

        # Set the treeview
        self.tree = ttk.Treeview(self.parent, columns=('Nombre', 'Codigo Postal'))
        self.tree.heading('#0', text='Numero de Ciudad')
        self.tree.heading('#1', text='Nombre')
        self.tree.heading('#2', text='Codigo Postal')
        self.tree.column('#1', stretch=tkinter.YES)
        self.tree.column('#2', stretch=tkinter.YES)
        self.tree.column('#0', stretch=tkinter.YES)
        self.tree.grid(row=4, columnspan=4, sticky='nsew')
        self.treeview = self.tree
        # inicializar un contador
        self.i = 1

    def insert_data(self):
        self.treeview.insert('', 'end', text="Ciudad_N°_"+str(self.i), values=(self.dose_entry.get(), self.modified_entry.get()))
        self.i = self.i + 1
        self.clear_text()
    
    def delete_data(self):
        focused = self.tree.focus()
        self.treeview.delete(focused)

    def clear_text(self):
        self.dose_entry.delete(0, 'end')
        self.modified_entry.delete(0, 'end')


def main():
    root = tkinter.Tk()
    d = Formulario(root)
    root.mainloop()


if __name__ == "__main__":
    main()
