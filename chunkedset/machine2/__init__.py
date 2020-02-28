'''
Application mimicing actions of machine 2

'''

from flask import Flask, request
import requests

data = {
'machine':2,
'data':[6,7,10,11]
}


app = Flask(__name__)

@app.route("/")
def index():
    '''
    Pending : Get data ids from machine2
    '''
    return "machine 2"

@app.route("/join", methods = ["GET"])
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
    return "machine joined"


@app.route("/update")
def update_data():
    '''
    Pending : Put method - Update data in machine2
    '''
    return "data updating"

if __name__ == "__main__":
    app.run()
