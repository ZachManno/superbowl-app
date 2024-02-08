from nicegui import ui


def get_answer_cols():
    return [
        {'name': 'number', 'label': 'Number', 'field': 'number', 'required': True},
        {'name': 'question', 'label': 'Question', 'field': 'question', 'required': True},
        {'name': 'answer', 'label': 'Answer', 'field': 'answer', 'sortable': True},
        {'name': 'option_one', 'label': 'Option 1', 'field': 'option_one', 'sortable': False},
        {'name': 'option_two', 'label': 'Option 2', 'field': 'option_two', 'sortable': False},
        {'name': 'points', 'label': 'Points', 'field': 'points', 'sortable': True},
    ]


def get_answer_rows():
    return [
        {'id': 0, 'number': 1, 'question': 'SUPERBOWL WINNER', 'answer': '?', 'option_one': '49ERS', 'option_two': 'CHIEFS', 'points': 1},
        {'id': 0, 'number': 2, 'question': '47.5 TOTAL POINTS SCORED', 'answer': '?', 'option_one': 'OVER', 'option_two': 'UNDER', 'points': 1},
    ]


def get_answers():
    with ui.table(title='Answers', columns=get_answer_cols(), rows=get_answer_rows(), selection='multiple', pagination=10) as table:
        with table.add_slot('top-right'):
            with ui.input(placeholder='Search').props('type=search').bind_value(table, 'filter').add_slot('append'):
                ui.icon('search')