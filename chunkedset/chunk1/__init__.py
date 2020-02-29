'''
Application mimicing actions of chunk1

'''

from flask import Flask, request, jsonify
import requests
import os,inspect

chunk1 = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
chunkedset = os.path.dirname(chunk1)
from chunkedset import Chunk
import sys
sys.path.insert(0, chunkedset)


app = Flask(__name__)
chunk = Chunk()

@app.route("/")
def index():
    '''
    Pending : Get data ids from chunk1
    '''

    return "chunk 1"


@app.route("/setdata", methods = ["GET","POST"])
def setdata():
    '''
    Assign data to store on chunks
    '''
    dataset = request.get_json(force=True)
    data = dataset['data']
    foo = chunk.set_data(set(data))
    if foo:
        return jsonify(dataset)
    else:
        return jsonify({'message':"Data already assigned"})


@app.route("/join", methods = ["GET"])
def join():
    '''
    Pending : Send join request to server
    server returns duplicates to delete
    '''
    path = "http://127.0.0.1:5000/server/join"
    r = requests.post(url = path, data = {'data':chunk.get_hash(), 'chunk':1})
    print(r)
    return "chunk joined"


@app.route("/leave")
def leave():
    '''
    Pending : Send leave request to master_machine
    '''
    path = "http://127.0.0.1:5000/server/leave"
    data = dataset['data']
    r = requests.post(url = path, data = {'data':dataset["data"], 'chunk':1})
    return "chunk left"


@app.route("/update")
def update_data():
    '''
    Pending : Put method - Update data in machine1
    '''
    return "data updating"



if __name__ == "__main__":

    app.run()
