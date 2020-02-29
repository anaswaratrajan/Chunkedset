'''
Application mimicing actions of chunk1

'''

from flask import Flask, request
from chunkedset import Chunk

import os,sys,inspect
chunk1 = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

import requests

app = Flask(__name__)

@app.route("/")
def index():
    '''
    Pending : Get data ids from machine1
    '''

    return "chunk 1"


@app.route("/join", methods = ["GET","POST"])
def join():
    '''
    Pending : Send join request to master_machine
    master_machine returns datavalues to store
    '''
    dataset = request.get_json(force=True)
    data = dataset['data']
    path = "http://127.0.0.1:5000/server/join"
    r = requests.post(url = path, data = {'data':dataset["data"], 'chunk':1})
    print(r)
    return "chunk joined"


@app.route("/leave")
def leave():
    '''
    Pending : Send leave request to master_machine
    '''
    path = "http://127.0.0.1:5000/master/leave"
    r = requests.post(url = path, data = data)
    return "chunk left"


@app.route("/update")
def update_data():
    '''
    Pending : Put method - Update data in machine1
    '''
    return "data updating"

if __name__ == "__main__":
    chunk1 = Chunk()
    app.run()
