from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from nicegui import ui

#from answers import get_answer_table
from answers import get_answers
from submissions import get_submissions

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


def get_leaderboard_cols():
    return [
        {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True},
        {'name': 'score', 'label': 'Score', 'field': 'score', 'sortable': True},
    ]


def get_leaderboard_rows():
    return [
        {'id': 0, 'name': 'Alice', 'score': 0},
        {'id': 1, 'name': 'Bob', 'score': 3},
        {'id': 2, 'name': 'Lionel', 'score': 6},
        {'id': 3, 'name': 'Michael', 'score': 8},
        {'id': 4, 'name': 'Julie', 'score': 4},
        {'id': 5, 'name': 'Livia', 'score': 1},
        {'id': 6, 'name': 'Carol', 'score': 5},
    ]

# Leaderboard - 38 Total Points
def get_leaderboard():
    with ui.table(title='Leaderboard', columns=get_leaderboard_cols(), rows=get_leaderboard_rows(), selection='multiple', pagination=10).classes('w-half').classes('border-separate border border-amber-500') as table:
        with table.add_slot('top-right'):
            with ui.input(placeholder='Search').props('type=search').bind_value(table, 'filter').add_slot('append'):
                ui.icon('search')


ui.image('/Users/zman/PycharmProjects/superbowl-app/assets/s-l1600.jpeg').classes('object-fill h-32 w-full')
with ui.row(wrap=False):
    get_leaderboard()
    get_answers()

ui.image('/Users/zman/PycharmProjects/superbowl-app/assets/s-l1600.jpeg').classes('object-fill h-32 w-full')
with ui.column():
    get_submissions()
ui.run()
