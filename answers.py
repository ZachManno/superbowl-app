from nicegui import ui


def get_answer_cols():
    return [
        {'name': 'number', 'label': 'Number', 'field': 'number', 'required': True},
        {'name': 'question', 'label': 'Question', 'field': 'question', 'required': True},
        {'name': 'answer', 'label': 'Answer', 'field': 'answer', 'sortable': True},
        {'name': 'O1', 'label': 'Option 1', 'field': 'O1', 'sortable': False},
        {'name': 'O2', 'label': 'Option 2', 'field': 'O2', 'sortable': False},
        {'name': 'O3', 'label': 'Option 3', 'field': 'O3', 'sortable': False},
        {'name': 'O4', 'label': 'Option 4', 'field': 'O4', 'sortable': False},
        {'name': 'O5', 'label': 'Option 5', 'field': 'O5', 'sortable': False},
        {'name': 'O6', 'label': 'Option 6', 'field': 'O6', 'sortable': False},
        {'name': 'O7', 'label': 'Option 7', 'field': 'O7', 'sortable': False},
        {'name': 'points', 'label': 'Points', 'field': 'points', 'sortable': True},
    ]


def get_answer_rows():
    return [
        {'id': 1, 'number': 1, 'question': 'Time for Reba McEntire’s National Anthem: 90.5 seconds', 'answer': '?', 'O1': 'OVER', 'O2': 'UNDER', 'points': 1},
        {'id': 2, 'number': 2, 'question': 'What will be the primary color of Reba McEntire’s boots?', 'answer': '?', 'O1': 'BLACK', 'O2': 'BROWN', 'O3': 'RED', 'O4': 'OTHER', 'points': 2},
        {'id': 3, 'number': 3, 'question': 'Will any scoring drive take less time than the anthem?', 'answer': '?','O1': 'YES', 'O2': 'NO', 'points': 1},
        {'id': 4, 'number': 4, 'question': 'Which quarterback will be shown first during the National Anthem?', 'answer': '?','O1': 'PURDY', 'O2': 'MAHOMES', 'points': 1},
        {'id': 5, 'number': 5, 'question': 'Who will be shown first with/closest to Taylor Swift during the broadcast (not counting commercials)?', 'answer': '?', 'O1': 'DONNA KELCE', 'O2': 'BRITTANY MAHOMES', 'O3': 'JASON KELCE', 'O4': 'OTHER', 'points': 2},
        {'id': 6, 'number': 6, 'question': 'Outcome of the coin toss:', 'answer': '?', 'O1': 'HEADS', 'O2': 'TAILS', 'points': 1},
        {'id': 7, 'number': 7, 'question': 'Taylor Swift to be shown within first 5 mins of game (game clock)?', 'answer': '?', 'O1': 'YES', 'O2': 'NO', 'points': 1},
        {'id': 8, 'number': 8, 'question': 'Primary color of Taylor Swift’s top at the Super Bowl?', 'answer': '?', 'O1': 'RED', 'O2': 'WHITE', 'O3': 'YELLOW', 'O4': 'OTHER', 'points': 2},
        {'id': 9, 'number': 9, 'question': 'Which team will score first?', 'answer': '?', 'O1': 'SAN FRANCISCO', 'O2': 'KANSAS CITY', 'points': 1},
        {'id': 10, 'number': 10, 'question': 'What will the first score of the game be?', 'answer': '?', 'O1': 'TOUCHDOWN', 'O2': 'FIELD GOAL', 'O3': 'SAFETY', 'points': 1},
        {'id': 11, 'number': 11, 'question': 'Will the game be tied again after 0-0?', 'answer': '?', 'O1': 'YES', 'O2': 'NO', 'points': 1},
        {'id': 12, 'number': 12, 'question': 'Will there be a penalty called in the first quarter?', 'answer': '?', 'O1': 'YES','O2': 'NO', 'points': 1},
        {'id': 13, 'number': 13, 'question': 'Over/Under 2.5 players to attempt a pass?', 'answer': '?', 'O1': 'OVER', 'O2': 'UNDER', 'points': 1},
        {'id': 14, 'number': 14, 'question': 'Who will be leading at halftime?', 'answer': '?', 'O1': 'SAN FRANCISCO', 'O2': 'KANSAS CITY', 'points': 1},
        {'id': 15, 'number': 15, 'question': 'Which quarter will be the higest scoring?', 'answer': '?', 'O1': '1ST', 'O2': '2ND', 'O3': '3RD', 'O4': '4TH', 'points': 2},
        {'id': 16, 'number': 16, 'question': 'What will be the primary color of Usher’s shirt during his first appearance?', 'answer': '?', 'O1': 'BLACK', 'O2': 'WHITE', 'O3': 'RED', 'O4': 'BLUE', 'O5': 'OTHER', 'points': 2},
        {'id': 17, 'number': 17, 'question': 'Will Usher be wearing sunglasses when first seen?', 'answer': '?', 'O1': 'YES', 'O2': 'NO', 'points': 1},
        {'id': 18, 'number': 18, 'question': 'Will Ludacris perform with Usher during the Halftime Show?', 'answer': '?', 'O1': 'YES', 'O2': 'NO', 'points': 1},
        {'id': 19, 'number': 19, 'question': 'Will Lil Jon perform with Usher during the Halftime Show?', 'answer': '?', 'O1': 'YES', 'O2': 'NO', 'points': 1},
        {'id': 20, 'number': 20, 'question': 'What will the first song of the Halftime Show be?', 'answer': '?','O1': 'MY WAY', 'O2': 'YEAH!', 'O3': 'DJ GOT US FALLIN IN LOVE', 'O4': 'LOVE IN THIS CLUB', 'O5': 'OTHER', 'points': 2},
        {'id': 21, 'number': 21, 'question': 'What will the LAST song of the Halftime Show be?', 'answer': '?', 'O1': 'YEAH!', 'O2': 'MY BOO', 'O3': 'CONFESSIONS PART II', 'O4': 'U DONT HAVE TO CALL', 'O5': 'OTHER', 'points': 2},
        {'id': 22, 'number': 22, 'question': 'Who will win Super Bowl 58?', 'answer': '?', 'O1': 'SAN FRANCISCO','O2': 'KANSAS CITY', 'points': 1},
        {'id': 23, 'number': 23, 'question': 'Which color Gatorade will be dumped on the winning coach?', 'answer': '?', 'O1': 'CLEAR/WATER', 'O2': 'RED/PINK', 'O3': 'BLUE', 'O4': 'YELLOW/LIME/GREEN', 'O5': 'ORANGE', 'O6': 'OTHER', 'O7': 'NONE', 'points': 3},
        {'id': 24, 'number': 24, 'question': 'Who will win Super Bowl MVP?', 'answer': '?', 'O1': 'PURDY', 'O2': 'MAHOMES', 'O3': 'OTHER', 'points': 1},
        {'id': 25, 'number': 25, 'question': 'Who will the Super Bowl MVP thank first?', 'answer': '?', 'O1': 'GOD', 'O2': 'TEAMMATES', 'O3': 'FAMILY', 'O4': 'COACHES', 'O5': 'OTHER', 'O6': 'NONE', 'points': 3}
    ]


def get_answers():
    with ui.table(title='Answers', columns=get_answer_cols(), rows=get_answer_rows(), selection='multiple', pagination=25).classes('grid-flow-col') as table:
        with table.add_slot('top-right'):
            with ui.input(placeholder='Search').props('type=search').bind_value(table, 'filter').add_slot('append'):
                ui.icon('search')