from bottle import route, run, request, template, post
from bottle import template
from bottle import error, BaseRequest
import json



TEST_ARR = [{"id": '1', "data": '2'}, {"id": '3', "data": "4"},
            {"id": '5', "data": '5'}, {"id": "7", "data": "8"}]


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
    """cur_id = request.body.get('id')
    data = request.body.get('data')"""
    tmp = request.json
    TEST_ARR[0] = tmp

    # return "dsdasdsads"


"""
@error(404)
def error404(error):
    return 'Nothing here, sorry'
"""


@route('/hello')
def hello():
    name = request.cookies.username or 'Guest'
    return template('Hello {{name}}', name=name)



run(host='localhost', port=8080, debug=True)
