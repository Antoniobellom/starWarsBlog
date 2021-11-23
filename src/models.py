import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    userId = Column(Integer,ForeignKey('pelicula.id'))
    password = Column(String(12), primary_key=True, nullable=False)
    peronajesID = Column(Integer,ForeignKey('Personajes.id'))

class Comentario(Base):
    __tablename__ = 'Comentario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    userId = Column(String(250), nullable=False)
    post_Id = Column(Integer,ForeignKey('Usuario.id'))

    

class Personajes(Base):
    __tablename__ ='Personajes'
    id = Column(Integer,primary_key=True)
    Alineacion = Column(String(250))
    Nombre = Column(String(250))
    Raza = Column(String(250))    


class Planetas(Base):
    __tablename__ = 'Planetas'
    id = Column(Integer,primary_key=True) 
    Poblacion = Column(Integer)
    Ubicacion = Column(Integer)

class Peliculas(Base):
    __tablename__ = 'Peliculas'
    id = Column(Integer,primary_key=True) 
    Fecha_de_estreno = Column(Integer)
    Director = Column(String(250))
    Recaudacion = Column(Integer)

class Libros(Base):
    __tablename__ = 'Libros'
    id = Column(Integer,primary_key=True) 
    Fecha_de_estreno = Column(Integer)
    Escritor = Column(String(250))
    Genero = Column(Integer) 



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')