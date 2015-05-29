import crawler as cr
from models import MuscleGroups, DifficultyLevel, Exercises, Priority, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from random import randint

engine = create_engine('sqlite:///fitness.db')
Base.metadata.create_all(engine)
session = Session(bind=engine)


BEGINNER = "beginner"
INTERMEDIATE = "intermediate"
ADVANCED = "advanced"

beg_exerc = cr.get_beginners_exercises()
intm_exerc = cr.get_intermediate_exercises()
adv_exerc = cr.get_advanced_exercises()


def update_exerc(exerc_name, priority, difficulty, muscle_group):
    db_exerc = session.query(Exercises).filter(
        Exercises.name == exerc_name).one()
    db_exerc.priority_groups.append(Priority(priority=int(priority)))
    db_exerc.levels.append(DifficultyLevel(name=difficulty))
    db_exerc.muscle_groups.append(MuscleGroups(name=muscle_group))

# beginners
for muscle_group, exercises in beg_exerc.items():
    for exerc in exercises:
        print(exerc, "  --  ", muscle_group)
        # priority = input("Enter priority for this exercise:")
        priority = randint(1, 8)
        db_exerc = session.query(Exercises).filter(
            Exercises.name == exerc).all()
        if len(db_exerc) == 0:
            session.add(Exercises(name=exerc))
            session.commit()
        update_exerc(exerc, priority, BEGINNER, muscle_group)
        session.commit()

for muscle_group, exercises in intm_exerc.items():
    for exerc in exercises:
        print(exerc, "  --  ", muscle_group)
        # priority = input("Enter priority for this exercise:")
        priority = randint(1, 8)
        db_exerc = session.query(Exercises).filter(
            Exercises.name == exerc).all()
        if len(db_exerc) == 0:
            session.add(Exercises(name=exerc))
            session.commit()
        update_exerc(exerc, priority, INTERMEDIATE, muscle_group)
        session.commit()

for muscle_group, exercises in adv_exerc.items():
    for exerc in exercises:
        print(exerc, "  --  ", muscle_group)
        # priority = input("Enter priority for this exercise:")
        priority = randint(1, 8)
        db_exerc = session.query(Exercises).filter(
            Exercises.name == exerc).all()
        if len(db_exerc) == 0:
            session.add(Exercises(name=exerc))
            session.commit()
        update_exerc(exerc, priority, ADVANCED, muscle_group)
        session.commit()
