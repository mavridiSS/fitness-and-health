from bottle import route, run, request, template, post
from bottle import template
from bottle import error, BaseRequest
import json


TEST_ARR = [{"user_id": 1, "data": 2}, {"user_id": 3, "data": 4},
            {"user_id": 5, "data": 6}, {"user_id": 7, "data": 8}]


def test_func(index):
    for elem in TEST_ARR:
        if elem["user_id"] == index:
            return elem["data"]
    else:
        return "doesnt exist"


@route('/<current_id:int>')
def callback(current_id):
    res = test_func(current_id)
    return res


@post('/')
def get_parameters():
    cur_id = request.headers.get('id')
    data = request.headers.get('data')
    tmp = {}
    tmp["user_id"] = cur_id
    tmp["data"] = data
   # TEST_ARR.append(tmp)
    return tmp


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
