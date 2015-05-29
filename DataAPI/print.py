from models import MuscleGroups, DifficultyLevel, Exercises, Priority, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine('sqlite:///fitness.db')
Base.metadata.create_all(engine)
session = Session(bind=engine)

all_back = session.query(Exercises).join(Exercises.muscle_groups).filter(Exercises.muscle_groups.any(MuscleGroups.name.in_(["Гърди"]))).filter(Exercises.priority_groups.any(Priority.priority.in_([2]))).all()
for x in all_back:
    print(x.name)
