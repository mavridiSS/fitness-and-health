from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Exercises(Base):
    __tablename__ = "Exercises"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class MuscleGroups(Base):
    __tablename__ = "MuscleGroups"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    exercise_id = Column(Integer, ForeignKey(Exercises.id))
    muscle_groups = relationship(Exercises, backref="muscle_groups")


class DifficultyLevel(Base):
    __tablename__ = "DifficultyLevel"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    exercise_id = Column(Integer, ForeignKey(Exercises.id))
    levels = relationship(Exercises, backref="levels")


class Priority(Base):
    __tablename__ = "Priority"
    id = Column(Integer, primary_key=True)
    priority = Column(Integer)
    exercise_id = Column(Integer, ForeignKey(Exercises.id))
    priority_groups = relationship(Exercises, backref="priority_groups")
