import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from data_training import AtmCardFraud
import numpy as np
import pickle
import pandas as pd
from dateutil import parser


class Date(BaseModel):
    date: str


app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post('/format')
def format_date(date: Date):
    date = date.date
    formatted = parser.parse(date)

    return {
        'format': formatted
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.2', port=8000)
