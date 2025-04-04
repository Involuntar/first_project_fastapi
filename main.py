import random as r
from fastapi import FastAPI, Query
import math

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/about_me")
def show_about_me():
    return {
        "name": "Ilya",
        "birth_date": {
            "day": 7,
            "month": "august",
            "year": 2004
        },
        "email": "ilya.nevolin.2004@mail.ru",
    }

@app.get("/rnd")
def get_random(start: int = 1, end: int = 10):
    return {
        "random integer": r.randint(start, end)
    }

@app.get("/t_square")
def get_random(a: int=Query(gt=0), b: int=Query(gt=0), c: int=Query(gt=0)):
    P = a + b + c
    p = P/2
    return {
        "perimeter": P,
        "square": math.sqrt(p*(p-a)*(p-b)*(p-c))
    }