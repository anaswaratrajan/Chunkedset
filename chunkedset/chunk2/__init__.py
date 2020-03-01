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
    return jsonify({'chunk':2})


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
    Send join request to server
    server returns duplicates to delete
    '''
    path = "http://127.0.0.1:5000/server/join"
    r=dict()
    r['data'] = list(chunk_2.get_data())
    r['chunk'] = 2
    d = json.dumps(r)
    r = requests.post(url = path, data = d)
    json_data = json.loads(r.text)
    return jsonify(json_data)


@app.route("/leave")
def leave():
    '''
    Send leave request to master_chunk
    '''
    path = "http://127.0.0.1:5000/server/leave"
    data = dataset['data']
    r = requests.post(url = path, data = {'data':data})
    return "chunk left"


@app.route("/update", methods=["POST"])
def update_data():
    '''
    Update data in chunk2
    '''
    dataset = request.get_json(force=True)
    duplicates = dataset['duplicates']
    chunk_2.remove_data(duplicates)
    return "data updating"



if __name__ == "__main__":
    app.run()
