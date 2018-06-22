from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column

Base = declarative_base()


class Socio(Base):
    __tablename__ = 'socios'

    id = Column(Integer, autoincrement=True, primary_key=True)
    dni = Column(Integer, unique=True)
    nombre = Column(String(250))
    apellido = Column(String(250))
