from nicegui import ui


def get_answer_cols():
    return [
        {'name': 'question', 'label': 'Question', 'field': 'question', 'required': True},
        {'name': 'correct', 'label': 'Correct', 'field': 'correct', 'sortable': True},
    ]


def get_answer_rows():
    return [
        {'id': 0, 'question': 'SUPERBOWL WINNER', 'correct': False},
        {'id': 1, 'question': '47.5 TOTAL POINTS SCORED', 'correct': False},
    ]


def get_answers():
    with ui.table(title='My Team', columns=get_answer_cols(), rows=get_answer_rows(), selection='multiple', pagination=10).classes('w-96') as table:
        with table.add_slot('top-right'):
            with ui.input(placeholder='Search').props('type=search').bind_value(table, 'filter').add_slot('append'):
                ui.icon('search')