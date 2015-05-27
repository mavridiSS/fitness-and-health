import crawler as cr
from models import MuscleGroups, DifficultyLevel, Exercises, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine('sqlite:///fitness.db')
Base.metadata.create_all(engine)
session = Session(bind=engine)

user = session.query(Exercises).filter(Exercises.name == "Vdigane ot lejanka").one()
#user.muscle_groups.append(MuscleGroups(name='Arms'))
for name in user.muscle_groups:
    print(name.name)

session.commit()
