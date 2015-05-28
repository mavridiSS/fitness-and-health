from models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine('sqlite:///fitness.db')
Base.metadata.create_all(engine)
session = Session(bind=engine)

all_exercises = session.query(Exercises).all()
for x in all_exercises:
    print(x)
