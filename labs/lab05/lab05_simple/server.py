from json import dumps
from flask import Flask, request

APP = Flask(__name__)

# GLOBAL VARIABLE BELOW
names = []
# GLOBAL VARIABLE ABOVE

def get_names():
    global names
    return names

@APP.route('/names', methods=['GET'])
def get():
    data = get_names()
    return dumps({
        'names' : data,
    })

@APP.route('/names/add', methods=['POST'])
def create():
    data = get_names()
    data.append(request.get_json()['names'])
    return dumps({})

@APP.route('/names/remove', methods=['DELETE'])
def update():
    data = get_names()
    data.remove(request.get_json()['names'])
    return dumps({})

if __name__ == '__main__':
    APP.run(port=7777)
