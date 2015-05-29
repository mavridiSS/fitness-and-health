from models import MuscleGroups, DifficultyLevel, Exercises, Priority, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import random
import collections
import json


BEGINNER = "beginner"
INTERMEDIATE = "intermediate"
ADVANCED = "advanced"


engine = create_engine('sqlite:///fitness.db')
Base.metadata.create_all(engine)
session = Session(bind=engine)


def get_exercises_for(muscle_group, number, level):
    result = []
    for exerc_number in range(1, number + 1):
            exercises = session.query(Exercises).join(Exercises.muscle_groups).filter(Exercises.muscle_groups.any(MuscleGroups.name.in_([muscle_group]))).filter(Exercises.priority_groups.any(Priority.priority.in_([2*exerc_number - 1, 2*exerc_number]))).filter(Exercises.levels.any(DifficultyLevel.name.in_([level]))).all()
            rand_exercise = random.choice(exercises).name
            result.append(rand_exercise)

    return result


def save_to_json(program):
    with open('program.json', 'w') as f:
        data = json.dumps(program, indent=4, ensure_ascii=False)
        f.write(data)


def beginner():
    program = collections.OrderedDict()
    program["Понеделник"] = [{"Гърди": get_exercises_for("Гърди", 1, BEGINNER),
                              "Гръб": get_exercises_for("Гръб", 1, BEGINNER),
                              "Бицепс": get_exercises_for("Бицепс", 1, BEGINNER),
                              "Трицепс": get_exercises_for("Трицепс", 1, BEGINNER),
                              "Предмишници": get_exercises_for("Предмишници", 1, BEGINNER),
                              "Рамо": get_exercises_for("Рамо", 1, BEGINNER),
                              "Бедра": get_exercises_for("Бедра", 1, BEGINNER),
                              "Прасец": get_exercises_for("Прасец", 1, BEGINNER)}]
    program["Вторник"] = [{}]
    program["Сряда"] = [{"Гърди": get_exercises_for("Гърди", 1, BEGINNER),
                         "Гръб": get_exercises_for("Гръб", 1, BEGINNER),
                         "Бицепс": get_exercises_for("Бицепс", 1, BEGINNER),
                         "Трицепс": get_exercises_for("Трицепс", 1, BEGINNER),
                         "Предмишници": get_exercises_for("Предмишници", 1, BEGINNER),
                         "Рамо": get_exercises_for("Рамо", 1, BEGINNER),
                         "Бедра": get_exercises_for("Бедра", 1, BEGINNER),
                         "Прасец": get_exercises_for("Прасец", 1, BEGINNER)}]
    program["Четвъртък"] = [{}]
    program["Петък"] = [{"Гърди": get_exercises_for("Гърди", 1, BEGINNER),
                         "Гръб": get_exercises_for("Гръб", 1, BEGINNER),
                         "Бицепс": get_exercises_for("Бицепс", 1, BEGINNER),
                         "Трицепс": get_exercises_for("Трицепс", 1, BEGINNER),
                         "Предмишници": get_exercises_for("Предмишници", 1, BEGINNER),
                         "Рамо": get_exercises_for("Рамо", 1, BEGINNER),
                         "Бедра": get_exercises_for("Бедра", 1, BEGINNER),
                         "Прасец": get_exercises_for("Прасец", 1, BEGINNER)}]
    program["Събота"] = [{}]
    program["Неделя"] = [{}]

    return program


def intermediate_3days():
    program = collections.OrderedDict()
    program["Понеделник"] = [{"Гърди": get_exercises_for("Гърди", 4, INTERMEDIATE),
                              "Трицепс": get_exercises_for("Трицепс", 3, INTERMEDIATE)}]
    program["Вторник"] = [{}]
    program["Сряда"] = [{"Гръб": get_exercises_for("Гръб", 4, INTERMEDIATE),
                         "Трицепс": get_exercises_for("Трицепс", 3, INTERMEDIATE)}]
    program["Четвъртък"] = [{}]
    program["Петък"] = [{"Бедра": get_exercises_for("Бедра", 4, INTERMEDIATE),
                         "Прасец": get_exercises_for("Прасец", 2, INTERMEDIATE),
                         "Рамо": get_exercises_for("Рамо", 3, INTERMEDIATE)}]
    program["Събота"] = [{}]
    program["Неделя"] = [{}]

    return program


def intermediate_4days():
    program = collections.OrderedDict()
    program["Понеделник"] = [{"Гърди": get_exercises_for("Гърди", 4, INTERMEDIATE)}]
    program["Вторник"] = [{"Гръб": get_exercises_for("Гръб", 4, INTERMEDIATE)}]
    program["Сряда"] = [{}]
    program["Четвъртък"] = [{"Бицепс": get_exercises_for("Бицепс", 3, INTERMEDIATE),
                             "Трицепс": get_exercises_for("Трицепс", 3, INTERMEDIATE),
                             "Предмишници": get_exercises_for("Предмишници", 1, INTERMEDIATE)}]
    program["Петък"] = [{"Бедра": get_exercises_for("Бедра", 4, INTERMEDIATE),
                         "Прасец": get_exercises_for("Прасец", 2, INTERMEDIATE),
                         "Рамо": get_exercises_for("Рамо", 3, INTERMEDIATE)}]
    program["Събота"] = [{}]
    program["Неделя"] = [{}]

    return program


def advanced_5days():
    program = collections.OrderedDict()
    program["Понеделник"] = [{"Гърди": get_exercises_for("Гърди", 4, ADVANCED)}]
    program["Вторник"] = [{"Гръб": get_exercises_for("Гръб", 4, ADVANCED)}]
    program["Сряда"] = [{}]
    program["Четвъртък"] = [{"Бицепс": get_exercises_for("Бицепс", 3, ADVANCED),
                             "Трицепс": get_exercises_for("Трицепс", 3, ADVANCED),
                             "Предмишници": get_exercises_for("Предмишници", 1, ADVANCED)}]
    program["Петък"] = [{"Бедра": get_exercises_for("Бедра", 4, ADVANCED),
                         "Прасец": get_exercises_for("Прасец", 2, ADVANCED)}]
    program["Събота"] = [{"Рамо": get_exercises_for("Рамо", 3, ADVANCED)}]
    program["Неделя"] = [{}]

    return program


def advanced_6days():
    program = collections.OrderedDict()
    program["Понеделник"] = [{"Гърди": get_exercises_for("Гърди", 4, ADVANCED)}]
    program["Вторник"] = [{"Гръб": get_exercises_for("Гръб", 4, ADVANCED)}]
    program["Сряда"] = [{}]
    program["Четвъртък"] = [{"Бицепс": get_exercises_for("Бицепс", 3, ADVANCED),
                             "Трицепс": get_exercises_for("Трицепс", 3, ADVANCED),
                             "Предмишници": get_exercises_for("Предмишници", 1, ADVANCED)}]
    program["Петък"] = [{"Бедра": get_exercises_for("Бедра", 4, ADVANCED),
                         "Прасец": get_exercises_for("Прасец", 2, ADVANCED)}]
    program["Събота"] = [{"Рамо": get_exercises_for("Рамо", 3, ADVANCED)}]
    program["Неделя"] = [{"Корем": get_exercises_for("Корем", 4, ADVANCED)}]

    return program
