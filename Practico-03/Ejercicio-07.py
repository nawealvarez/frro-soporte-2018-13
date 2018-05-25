from Connection import Connect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey, create_engine

Base = declarative_base()


class Persona(Base):
    __tablename__ = "persona"
    idPersona = Column(Integer, primary_key=True)
    dni = Column(Integer, nullable=True)
    fechaNacimiento = Column(Date, nullable=True)
    nombre = Column(String(30), nullable=True)
    altura = Column(Integer, nullable=True)
    # peso = relationship("PesoCorporal", back_populates="persona")


class PesoCorporal(Base):
    __tablename__ = "personaCorporal"
    idPersona = Column(Integer, ForeignKey('persona.idPersona'))
    fecha = Column(Date, primary_key=True)
    peso = Column(Integer, nullable=True)
    persona = relationship(Persona)


engine = create_engine("mysql+pymysql://root:MySQL@localhost/soporte_tp3")
Base.metadata.create_all(engine)


# TIRA ERROR PERO CREA LA TABLA, NO SE QUE ONDA
