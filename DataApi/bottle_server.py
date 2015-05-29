from bottle import route, run, request, post
from generator import beginner, intermediate_3days, intermediate_4days
from generator import advanced_5days, advanced_6days


USERS_INFO = []


def test_func(level, period):
    if level == 1:
        return beginner()
    elif level == 2 and period == 3:
        return intermediate_3days()
    elif level == 2 and period == 4:
        return intermediate_4days()
    elif level == 3 and period == 5:
        return advanced_5days()
    elif level == 3 and period == 6:
        return advanced_6days()
    else:
        pass


@route('/<current_id:int>')
def callback(current_id):
    for user in USERS_INFO:
        if user['id'] == current_id:
            current_lvl = user['diffuculty']
            current_period = user['workouts_count']
            break
    res = test_func(current_lvl, current_period)
    return res


@post('/')
def get_parameters():
    """cur_id = request.body.get('id')
    data = request.body.get('data')"""
    cur_id = request.forms.get('id')
    cur_dif = request.forms.get('diffuculty')
    cur_days = request.forms.get('workouts_count')
    d = {}
    d['id'] = cur_id
    d['diffuculty'] = cur_dif
    d['days'] = cur_days

    USERS_INFO.append(d)
    return d


run(host='localhost', port=8080, debug=True)
