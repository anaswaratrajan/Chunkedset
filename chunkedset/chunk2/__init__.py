'''
Application mimicing actions of chunk 2

'''

from flask import Flask, request, jsonify
import requests
import json
import os,inspect

chunk2 = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
chunkedset = os.path.dirname(chunk2)
from chunkedset import Chunk
import sys
sys.path.insert(0, chunkedset)


app = Flask(__name__)
chunk_2 = Chunk()

@app.route("/")
def index():
    '''
    Pending : Get data ids from chunk2
    '''
    return "chunk 2"


@app.route("/setdata", methods = ["GET","POST"])
def setdata():
    '''
    Assign data to store on chunks
    '''
    dataset = request.get_json(force=True)
    data = dataset['data']
    foo = chunk_2.set_data(set(data))
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
    r = {}
    r['data'] = list(chunk_2.get_hash())
    r['chunk'] = 2
    d = json.dumps(r)
    r = requests.post(url = path, data = d)
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
    app.run()
