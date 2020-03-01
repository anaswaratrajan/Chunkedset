'''
Application mimicing actions of chunk1

'''

from flask import Flask, request, jsonify, Response
import requests
import os,inspect
import json

chunk1 = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
chunkedset = os.path.dirname(chunk1)
from chunkedset import Chunk
import sys
sys.path.insert(0, chunkedset)


app = Flask(__name__)
chunk_1 = Chunk()

@app.route("/")
def index():
    return jsonify({'chunk':1})


@app.route("/setdata", methods = ["GET","POST"])
def setdata():
    '''
    Assign data to store on chunks
    '''
    dataset = request.get_json(force=True)
    data = dataset['data']
    foo = chunk_1.set_data(set(data))
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
    r=dict()
    r['data'] = list(chunk_1.get_hash())
    r['chunk'] = 1
    d = json.dumps(r)
    r = requests.post(url = path, data = d)
    return "chunk joined"


@app.route("/leave")
def leave():
    '''
    Pending : Send leave request to master_machine
    '''
    path = "http://127.0.0.1:5000/server/leave"
    data = dataset['data']
    r = requests.post(url = path, data = {'data':data})
    return "chunk left"


@app.route("/update")
def update_data():
    '''
    Pending : Put method - Update data in machine1
    '''
    return "data updating"



if __name__ == "__main__":

    app.run()
