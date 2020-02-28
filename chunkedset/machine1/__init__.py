'''
Application mimicing actions of machine 1

'''

from flask import Flask, request
import requests

app = Flask(__name__)

data = {
'machine':1,
'data':[1,2,3,4,5]
}

@app.route("/")
def index():
    '''
    Pending : Get data ids from machine1
    '''
    return "machine 1"


@app.route("/join")
def join():
    '''
    Pending : Send join request to master_machine
    '''
    path = "http://127.0.0.1:5000/master/join"
    print("\n\n")
    r = requests.post(url = path, data = data)
    print("Haha\n\n")
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
    Pending : Put method - Update data in machine1
    '''
    return "data updating"

if __name__ == "__main__":
    app.run()
