import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id_user = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    favorites = relationship('Favorites', backref='user', lazy = True)

class Planet(Base):
    __tablename__ = 'planet'
    id_planet = Column(Integer, primary_key=True)
    planet_name = Column(String(50), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id_character = Column(Integer, primary_key=True)
    character_name = Column(String(50), nullable=False)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id_vehicle = Column(Integer, primary_key=True)
    vehicle_name = Column(String(50), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id_favorite = Column(Integer, primary_key=True)
    fk_user = Column(Integer, ForeignKey('user.id_user'), nullable = False)
    fk_character = Column(Integer, ForeignKey('character.id_character'))
    fk_planet = Column(Integer, ForeignKey('planet.id_planet'))
    fk_vehicle = Column(Integer, ForeignKey('vehicle.id_vehicle')) 
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')