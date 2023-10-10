import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class planets(Base):
    __tablename__ = "Planets"
    name = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)
    climate = Column(String(250))
    population = Column(Integer)
    orbital_period = Column(String(250)) 
    diameter = Column(Integer)

class people(Base):
    __tablename__ = "People"
    name = Column(String(250), nullable=False) 
    id = Column(Integer, primary_key=True) 
    gender = Column(String(250))
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(Integer)
    height = Column(Integer)
    mass = Column(Integer)
    homeworld_id = Column(String(250),ForeignKey('Planets.id'))
    planets = relationship(planets)

class starships(Base):
    __tablename__ = 'Starships'
    name_model = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)
    passengers = Column(Integer)
    pilots_id = Column(Integer, ForeignKey("People.id"))
    people = relationship(people)
    manufacturer_id = Column(String(250), ForeignKey("Planets.id"))
    planets = relationship(planets)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
