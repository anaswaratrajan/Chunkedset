'''
Application mimicing actions of chunk 3

'''

from flask import Flask, request, jsonify
import requests
import os,inspect
import json

chunk3 = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
chunkedset = os.path.dirname(chunk3)
from chunkedset import Chunk
import sys
sys.path.insert(0, chunkedset)


app = Flask(__name__)
chunk_3 = Chunk()


@app.route("/")
def index():
    '''
    Pending : Get data ids from chunk3
    '''

    return "chunk 3"


@app.route("/setdata", methods = ["GET","POST"])
def setdata():
    '''
    Assign data to store on chunks
    '''
    dataset = request.get_json(force=True)
    data = dataset['data']
    foo = chunk_3.set_data(set(data))
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
    r['data'] = list(chunk_3.get_hash())
    r['chunk'] = 3
    d = json.dumps(r)
    r = requests.post(url = path, data = d)
    print(r.text)
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
    app.run()
