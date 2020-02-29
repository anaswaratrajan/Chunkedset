'''
Application mimicing actions of chunk 3

'''

from flask import Flask, request
import requests
import os,sys,inspect
chunk3 = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

from chunks import Chunk


app = Flask(__name__)

@app.route("/")
def index():
    '''
    Pending : Get data ids from chunk3
    '''

    return "chunk 3"


@app.route("/join", methods = ["POST"])
def join():
    '''
    Pending : Send join request to master_chunk
    '''
    path = "http://127.0.0.1:5000/master/join"
    r = requests.post(url = path, data = data)
    return "chunk joined"

@app.route("/leave")
def leave():
    '''
    Pending : Send leave request to master_chunk
    '''
    path = "http://127.0.0.1:5000/master/leave"
    r = requests.post(url = path, data = data)
    return "chunk left"

@app.route("/update")
def update_data():
    '''
    Pending
    '''
    return "data updating"


if __name__ == "__main__":
    chunk3 = Chunk()
    app.run()
