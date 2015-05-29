from bottle import route, run, request, template, post
from bottle import template
from bottle import error, BaseRequest
import json



TEST_ARR = []
def try1(data):
    TRY = { 'П': [{'МГ1': ['У1', 'У2'], 'МГ2': ['У3', 'Ъ4']}],
            'В': [{'МГ1': ['У1', 'У2'], 'МГ2': ['У3', 'Ъ4']}],
            'Дата': data
            }
    return(TRY)

def test_func(index):
    for elem in TEST_ARR:
        if elem["id"] == index:
            data = elem["data"]
            return data
    else:
        return "doesnt exist"


@route('/<current_id:int>')
def callback(current_id):
    res = test_func(current_id)
    return res

@post('/')
def get_parameters():
    tmp = request.json
    TEST_ARR[0] = try1(tmp)

    # return "dsdasdsads"


@error(500)
def error404(error):
    return 'error'



@route('/hello')
def hello():
    name = request.cookies.username or 'Guest'
    return template('Hello {{name}}', name=name)



run(host='localhost', port=8080, debug=True)
