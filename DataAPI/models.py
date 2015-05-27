from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Exercises(Base):
    __tablename__ = "Exercises"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    priority = Column(Integer)


class MuscleGroups(Base):
    __tablename__ = "MuscleGroups"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    exercise_id = Column(Integer, ForeignKey(Exercises.id))
    muscle_groups = relationship(Exercises, backref="muscle_groups")


class DifficultyLevel(Base):
    __tablename__ = "DifficultyLevel"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    exercise_id = Column(Integer, ForeignKey(Exercises.id))
    levels = relationship(Exercises, backref="levels")


