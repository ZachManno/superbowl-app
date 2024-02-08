from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from nicegui import ui
from nicegui.events import ValueChangeEventArguments
import pandas as pd
from pandas.api.types import is_bool_dtype, is_numeric_dtype

#from answers import get_answer_table
from answers import get_answers

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


columns = [
    {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True},
    {'name': 'age', 'label': 'Age', 'field': 'age', 'sortable': True},
]
rows = [
    {'id': 0, 'name': 'Alice', 'age': 18},
    {'id': 1, 'name': 'Bob', 'age': 21},
    {'id': 2, 'name': 'Lionel', 'age': 19},
    {'id': 3, 'name': 'Michael', 'age': 32},
    {'id': 4, 'name': 'Julie', 'age': 12},
    {'id': 5, 'name': 'Livia', 'age': 25},
    {'id': 6, 'name': 'Carol'},
]

def get_leaderboard():
    with ui.table(title='My Team', columns=columns, rows=rows, selection='multiple', pagination=10).classes('w-96') as table:
        with table.add_slot('top-right'):
            with ui.input(placeholder='Search').props('type=search').bind_value(table, 'filter').add_slot('append'):
                ui.icon('search')

with ui.row():
    get_leaderboard()
    get_answers()
ui.run()
