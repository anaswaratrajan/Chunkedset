'''
Application mimicing actions of chunk 2

'''

from flask import Flask, request
import requests
import os,inspect

chunk2 = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
chunkedset = os.path.dirname(chunk2)
from chunkedset import Chunk
import sys
sys.path.insert(0, chunkedset)


app = Flask(__name__)


@app.route("/")
def index():
    '''
    Pending : Get data ids from chunk2
    '''
    return "chunk 2"


@app.route("/join", methods = ["GET"])
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
    Pending : Put method - Update data in chunk2
    '''
    return "data updating"



if __name__ == "__main__":
    chunk2 = Chunk()
    app.run()
