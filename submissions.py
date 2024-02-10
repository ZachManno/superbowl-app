from nicegui import ui

from answers import get_question_answer_template
from csv_reader import read_csv_to_dict


def get_submission_cols():
    return [
        {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True},
        {'name': 'score', 'label': 'Score', 'field': 'score', 'required': True},
        {'name': '1', 'label': 'Q1', 'field': '1', 'required': False},
        {'name': '2', 'label': 'Q2', 'field': '2', 'required': False},
        {'name': '3', 'label': 'Q3', 'field': '3', 'required': False},
        {'name': '4', 'label': 'Q4', 'field': '4', 'required': False},
        {'name': '5', 'label': 'Q5', 'field': '5', 'required': False},
        {'name': '6', 'label': 'Q6', 'field': '6', 'required': False},
        {'name': '7', 'label': 'Q7', 'field': '7', 'required': False},
        {'name': '8', 'label': 'Q8', 'field': '8', 'required': False},
        {'name': '9', 'label': 'Q9', 'field': '9', 'required': False},
        {'name': '10', 'label': 'Q10', 'field': '10', 'required': False},
        {'name': '11', 'label': 'Q11', 'field': '11', 'required': False},
        {'name': '12', 'label': 'Q12', 'field': '12', 'required': False},
        {'name': '13', 'label': 'Q13', 'field': '13', 'required': False},
        {'name': '14', 'label': 'Q14', 'field': '14', 'required': False},
        {'name': '15', 'label': 'Q15', 'field': '15', 'required': False},
        {'name': '16', 'label': 'Q16', 'field': '16', 'required': False},
        {'name': '17', 'label': 'Q17', 'field': '17', 'required': False},
        {'name': '18', 'label': 'Q18', 'field': '18', 'required': False},
        {'name': '19', 'label': 'Q19', 'field': '19', 'required': False},
        {'name': '20', 'label': 'Q20', 'field': '20', 'required': False},
        {'name': '21', 'label': 'Q21', 'field': '21', 'required': False},
        {'name': '22', 'label': 'Q22', 'field': '22', 'required': False},
        {'name': '23', 'label': 'Q23', 'field': '23', 'required': False},
        {'name': '24', 'label': 'Q24', 'field': '24', 'required': False},
        {'name': '25', 'label': 'Q25', 'field': '25', 'required': False},

    ]


def get_submission_rows():
    dict_from_csv = read_csv_to_dict("/Users/zman/Downloads/Superbowl-Prop-Submissions.csv")
    for name, answers in dict_from_csv.items():
        answers_converted = {str(k): v for k, v in answers.items()}
        dict_from_csv[name] = answers_converted
    list_of_dicts = []

    for idx, (name, data) in enumerate(dict_from_csv.items()):
        new_dict = {'id': idx, 'name': name}
        new_dict.update(data)
        list_of_dicts.append(new_dict)
    #print(list_of_dicts)
    return list_of_dicts
    #return [
        # {'id': 1, 'name': 'Zach', '1': 'CHIEFS', '2': 'OVER', '1': '1-5PTS', 'q4': 'OVER', 'q5': 'HEADS', 'q6': 'RED', 'q7': 'UNDER', 'q8': 'UNDER', 'q9': 'YES', 'q10': 'PASS', 'q11': '49ERS', 'q12': 'TOUCHDOWN', },
    #]

def score_submissions_with_answers(answer_rows):
    submission_rows = get_submission_rows()
    print("submission_rows: " + str(submission_rows))
    for submission_dict in submission_rows:
        score = 0
        for key, value in submission_dict.items():
            if key != 'id' and key != 'name':
                the_answer_row = {}
                for ans in answer_rows:
                    if ans['number'] == int(key):
                        the_answer_row = ans
                if value == the_answer_row['answer']:
                    score = score + the_answer_row['points']
        submission_dict['score'] = score
    for submission_dict in submission_rows:
        if 'score' not in submission_dict.keys():
            submission_dict['score'] = 0
    return submission_rows



def get_submissions(submission_rows_with_score):
    with ui.table(title='Submissions', columns=get_submission_cols(), rows=submission_rows_with_score, selection='multiple', pagination=10).classes('w-full') as table:
        with table.add_slot('top-right'):
            with ui.input(placeholder='Search').props('type=search').bind_value(table, 'filter').add_slot('append'):
                ui.icon('search')