# Implementar los metodos de la capa de datos de socios.


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Practico_05.ejercicio_01 import Base, Socio


class DatosSocio(object):

    def __init__(self):
        engine = create_engine('sqlite:///socios.db')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session(autoflush=False)
        Base.metadata.create_all(engine)

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.session.query(Socio).filter(Socio.id == id_socio).first()

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.session.query(Socio).filter(Socio.dni == dni_socio).first()

    def todos(self):
        """
        Devuelve listado de todos los socios en la base de datos.
        :rtype: list
        """
        return self.session.query(Socio).all()

    def borrar_todos(self):
        """
        Borra todos los socios de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        todos = self.todos()
        for s in todos:
            self.baja(s.id)
        if len(todos):
            return True
        return False

    def alta(self, socio):
        """
        Devuelve el Socio luego de darlo de alta.
        :type socio: Socio
        :rtype: Socio
        """
        self.session.add(socio)
        self.session.commit()
        return socio

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        if self.session.query(Socio).filter(Socio.id == id_socio).delete():
            self.session.commit()
            return True
        return False

    def modificacion(self, socio):
        """
        Guarda un socio con sus datos modificados.
        Devuelve el Socio modificado.
        :type socio: Socio
        :rtype: Socio
        """
        self.session.commit()
        return socio


def pruebas():
    # alta
    datos = DatosSocio()
    socio = datos.alta(Socio(dni=12345678, nombre='Lionel', apellido='Messi'))
    assert socio.id > 0

    # baja
    assert datos.baja(socio.id) is True

    # buscar
    socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Tevez'))
    assert datos.buscar(socio_2.id) == socio_2

    # buscar dni
    socio_2 = datos.alta(Socio(dni=12345681, nombre='Carlos', apellido='Tevez'))
    assert datos.buscar_dni(socio_2.dni) == socio_2

    # modificacion
    socio_3 = datos.alta(Socio(dni=12345680, nombre='China', apellido='Suarez'))
    socio_3.nombre = 'Sol'
    socio_3.apellido = 'Perez'
    socio_3.dni = 13264587
    datos.modificacion(socio_3)
    socio_3_modificado = datos.buscar(socio_3.id)
    assert socio_3_modificado.id == socio_3.id
    assert socio_3_modificado.nombre == 'Sol'
    assert socio_3_modificado.apellido == 'Perez'
    assert socio_3_modificado.dni == 13264587

    # todos
    assert len(datos.todos()) == 3

    # borrar todos
    datos.borrar_todos()
    assert len(datos.todos()) == 0


if __name__ == '__main__':
    pruebas()
