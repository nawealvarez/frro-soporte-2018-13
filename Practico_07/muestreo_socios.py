from operator import attrgetter

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mbox

from Practico_06.capa_negocio import Socio, NegocioSocio, DniRepetido, LongitudInvalida, MaximoAlcanzado


class PresentacionSocios:
    def __init__(self):
        self.negocio_socio = NegocioSocio()
        self.root = tk.Tk()
        self.configure_gui()
        self.create_widgets()
        self.populate_treeview()
        self.root.mainloop()

    def configure_gui(self):
        self.root.title('ABM de Socios')
        self.root.geometry('1000x600')

    def create_widgets(self):
        self.frame = ttk.Frame(self.root, padding=10)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.frame.grid(sticky=tk.W + tk.E + tk.N + tk.S)
        self.tree = ttk.Treeview(self.frame, columns=('id', 'nombre', 'apellido', 'dni'))
        self.tree['show'] = 'headings'  # no mostrar columna vacía
        self.tree.heading('id', text='Id')
        self.tree.heading('nombre', text='Nombre')
        self.tree.heading('apellido', text='Apellido')
        self.tree.heading('dni', text='DNI')
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.tree.grid(sticky=tk.W + tk.E + tk.N + tk.S)
        self.frame_acciones = ttk.Frame(self.root, padding=(10, 0, 0, 10))
        self.frame_acciones.grid(row=1, column=0, sticky=tk.W + tk.E)
        self.btn_alta = ttk.Button(self.frame_acciones, text='Alta', command=self.alta_socio)
        self.btn_modificacion = ttk.Button(self.frame_acciones, text='Modificación', command=self.modifica_socio)
        self.btn_baja = ttk.Button(self.frame_acciones, text='Baja', command=self.baja_socio)
        self.btn_alta.pack(side=tk.LEFT, padx=(0, 5))
        self.btn_baja.pack(side=tk.LEFT, padx=(0, 5))
        self.btn_modificacion.pack(side=tk.LEFT)

    def populate_treeview(self):
        self.tree.delete(*self.tree.get_children())
        lista_socios = self.negocio_socio.todos()
        lista_socios.sort(key=attrgetter('nombre', 'apellido'))  # ordena por nombre y apellido
        for s in lista_socios:
            self.tree.insert('', 'end', values=(s.id, s.nombre, s.apellido, s.dni))

    def alta_socio(self):
        ed = EditaSocio(self.root, self.negocio_socio)
        socio = ed.resultado
        if socio:
            try:
                self.negocio_socio.alta(socio)
                self.populate_treeview()
            except Exception as err:
                mbox.showerror('Error', str(err), parent=self.root)

    def modifica_socio(self):
        item_id = self.tree.focus()
        if item_id:
            id_socio = self.tree.item(item_id, 'values')[0]
            socio = self.negocio_socio.buscar(id_socio)
            ed = EditaSocio(self.root, self.negocio_socio, socio=socio)
            s = ed.resultado
            if s:
                try:
                    self.negocio_socio.modificacion(socio)
                    self.populate_treeview()
                except Exception as err:
                    mbox.showerror('Error', str(err), parent=self.root)

    def baja_socio(self):
        item_id = self.tree.focus()
        if item_id:
            baja = mbox.askyesno('Confirme baja de socio', '¿Realmente desea dar de baja?', default='no',
                                 parent=self.root)
            if baja:
                id_socio = self.tree.item(item_id, 'values')[0]
                self.negocio_socio.baja(id_socio)
                self.populate_treeview()


class EditaSocio:
    def __init__(self, parent, negocio_socio, socio=None):
        self.parent = parent
        self.top = tk.Toplevel(self.parent)
        self.top.transient(self.parent)

        self.negocio_socio = negocio_socio
        if socio:
            self.top.title('Editando socio')
            self.resultado = socio
        else:
            self.top.title('Alta socio')
            self.resultado = Socio(nombre='', apellido='', dni=0)
        id_socio = self.resultado.id
        if id_socio is None:
            id_socio = 0
        self.top.resizable(1, 0)

        self.frame = ttk.Frame(self.top, padding=10)
        self.top.columnconfigure(0, weight=1)
        self.frame.grid(sticky=tk.W + tk.E)
        self.lbl_id = ttk.Label(self.frame, text='Id')
        self.txt_id = ttk.Label(self.frame, text=str(id_socio))
        self.lbl_nombre = ttk.Label(self.frame, text='Nombre')
        self.nombre_var = tk.StringVar()
        self.nombre_var.set(self.resultado.nombre)
        self.txt_nombre = ttk.Entry(self.frame, textvariable=self.nombre_var)
        self.lbl_apellido = ttk.Label(self.frame, text='Apellido')
        self.apellido_var = tk.StringVar()
        self.apellido_var.set(self.resultado.apellido)
        self.txt_apellido = ttk.Entry(self.frame, textvariable=self.apellido_var)
        self.lbl_dni = ttk.Label(self.frame, text='DNI')
        self.dni_var = tk.IntVar()
        self.dni_var.set(self.resultado.dni)
        self.txt_dni = ttk.Entry(self.frame, textvariable=self.dni_var)
        self.frame.columnconfigure(1, weight=1)
        self.lbl_id.grid(row=0, column=0, padx=(0, 10), pady=(0, 10), sticky=tk.W)
        self.txt_id.grid(row=0, column=1, pady=(0, 10), sticky=tk.W + tk.E)
        self.lbl_nombre.grid(row=1, column=0, padx=(0, 10), pady=(0, 10), sticky=tk.W)
        self.txt_nombre.grid(row=1, column=1, pady=(0, 10), sticky=tk.W + tk.E)
        self.lbl_apellido.grid(row=2, column=0, padx=(0, 10), pady=(0, 10), sticky=tk.W)
        self.txt_apellido.grid(row=2, column=1, pady=(0, 10), sticky=tk.W + tk.E)
        self.lbl_dni.grid(row=3, column=0, padx=(0, 10), sticky=tk.W)
        self.txt_dni.grid(row=3, column=1, sticky=tk.W + tk.E)

        self.btn_frame = ttk.Frame(self.top, padding=(0, 0, 10, 10))
        self.btn_frame.grid(sticky=tk.W + tk.E)
        self.btn_aceptar = ttk.Button(self.btn_frame, text='Aceptar', command=self.ok)
        self.btn_cancelar = ttk.Button(self.btn_frame, text='Cancelar', command=self.cancel)
        self.btn_cancelar.pack(side=tk.RIGHT)
        self.btn_aceptar.pack(side=tk.RIGHT, padx=(0, 5))

        self.top.grab_set()
        self.top.protocol("WM_DELETE_WINDOW", self.cancel)
        self.txt_nombre.focus_set()
        self.top.wait_window(self.top)

    def ok(self):
        try:
            self.resultado.dni = self.dni_var.get()
            self.resultado.nombre = self.nombre_var.get()
            self.resultado.apellido = self.apellido_var.get()
            if self.resultado.nombre and self.resultado.apellido and self.resultado.dni:
                if self.negocio_socio.validar_todo(self.resultado):
                    self.finish()
            else:
                mbox.showinfo('Campos incompletos', 'Complete todos los campos', parent=self.top)
        except tk.TclError:
            mbox.showinfo('Error', 'El DNI debe ser un número entero', parent=self.top)
        except Exception as ex:
            if len(ex.args) <= 1:  # excepcion simple
                mbox.showinfo('Error', str(ex), parent=self.top)
            else:
                errors = ''
                for err in ex.args:  # excepcion con multiples excepciones
                    errors += str(err) + '\n'
                mbox.showinfo('Errores de validación', errors, parent=self.top)

    def cancel(self):
        self.resultado = None
        self.finish()

    def finish(self):
        self.parent.focus_set()
        self.top.destroy()


if __name__ == '__main__':
    p = PresentacionSocios()
