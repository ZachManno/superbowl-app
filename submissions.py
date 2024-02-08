from nicegui import ui


def get_submission_cols():
    return [
        {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True},
        {'name': 'q1', 'label': 'Q1', 'field': 'q1', 'required': False},
        {'name': 'q1', 'label': 'Q2', 'field': 'q2', 'required': False},
        {'name': 'q1', 'label': 'Q3', 'field': 'q3', 'required': False},
        {'name': 'q1', 'label': 'Q4', 'field': 'q4', 'required': False},
        {'name': 'q1', 'label': 'Q5', 'field': 'q5', 'required': False},
        {'name': 'q1', 'label': 'Q6', 'field': 'q6', 'required': False},
        {'name': 'q1', 'label': 'Q7', 'field': 'q7', 'required': False},
        {'name': 'q1', 'label': 'Q8', 'field': 'q8', 'required': False},
        {'name': 'q1', 'label': 'Q9', 'field': 'q9', 'required': False},
        {'name': 'q1', 'label': 'Q10', 'field': 'q10', 'required': False},
        {'name': 'q1', 'label': 'Q11', 'field': 'q11', 'required': False},
        {'name': 'q1', 'label': 'Q12', 'field': 'q12', 'required': False},
        {'name': 'q1', 'label': 'Q13', 'field': 'q13', 'required': False},
        {'name': 'q1', 'label': 'Q14', 'field': 'q14', 'required': False},
        {'name': 'q1', 'label': 'Q15', 'field': 'q15', 'required': False},
        {'name': 'q1', 'label': 'Q16', 'field': 'q16', 'required': False},
        {'name': 'q1', 'label': 'Q17', 'field': 'q17', 'required': False},
        {'name': 'q1', 'label': 'Q18', 'field': 'q18', 'required': False},
        {'name': 'q1', 'label': 'Q19', 'field': 'q19', 'required': False},
        {'name': 'q1', 'label': 'Q20', 'field': 'q20', 'required': False},
        {'name': 'q1', 'label': 'Q21', 'field': 'q21', 'required': False},
        {'name': 'q1', 'label': 'Q22', 'field': 'q22', 'required': False},
        {'name': 'q1', 'label': 'Q23', 'field': 'q23', 'required': False},
        {'name': 'q1', 'label': 'Q24', 'field': 'q24', 'required': False},
        {'name': 'q1', 'label': 'Q25', 'field': 'q25', 'required': False},

    ]


def get_submission_rows():
    return [
        {'id': 0, 'name': 'Carol', 'q1': 'CHIEFS', 'q2': 'OVER', 'q3': '1-5PTS', 'q4': 'OVER', 'q5': 'HEADS', 'q6': 'RED', 'q7': 'UNDER', 'q8': 'UNDER', 'q9': 'YES', 'q10': 'PASS', 'q11': '49ERS', 'q12': 'TOUCHDOWN', },
    ]


def get_submissions():
    with ui.table(title='Submissions', columns=get_submission_cols(), rows=get_submission_rows(), selection='multiple', pagination=10).classes('w-full') as table:
        with table.add_slot('top-right'):
            with ui.input(placeholder='Search').props('type=search').bind_value(table, 'filter').add_slot('append'):
                ui.icon('search')