'''
Application mimicing actions of machine 3

'''

from flask import Flask, request
import requests

data = {
        'machine':3,
        'data':[6,7]

app = Flask(__name__)

@app.route("/")
def index():
    '''
    Pending : Get data ids from machine3
    '''
    return "machine 3"


@app.route("/join")
def join():
    '''
    Pending : Send join request to master_machine
    '''
    path = "http://127.0.0.1:5000/master/join"
    r = requests.post(url = path, data = data)
    return "machine joined"

@app.route("/leave")
def leave():
    '''
    Pending : Send leave request to master_machine
    '''
    path = "http://127.0.0.1:5000/master/leave"
    r = requests.post(url = path, data = data)
    return "machine left"

@app.route("/update")
def update_data():
    '''
    Pending
    '''
    return "data updating"


if __name__ == "__main__":
    app.run()
