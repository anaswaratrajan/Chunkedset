'''
Application mimicing actions of server.

'''

from flask import Flask, request, jsonify, Response
import requests
import json

import os,inspect
server = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
chunkedset = os.path.dirname(server)
from chunkedset import ChunkedSet
import sys
sys.path.insert(0, chunkedset)


app = Flask(__name__)
Chunkedset = ChunkedSet()

@app.route("/")
def index():
    return "server"


@app.route("/join", methods = ["POST"])
def join_system():
    '''
    Pending : Join the requested machine to system
    '''
    new_data = request.get_json(force=True)
    data = new_data['data']
    duplicates = Chunkedset.join(set(data))
    r = dict()
    r['duplicates']=duplicates
    d = json.dumps(r)
    path = "http://127.0.0.1:5000/chunk{0}/update".format(new_data['chunk'])
    r = requests.post(url = path, data = d)
    return jsonify(r)


@app.route("/leave", methods = ["POST"])
def leave():
    '''
    Pending : Remove the chunk from chunkedset
    '''
    new_data = request.get_json(force=True)
    data = new_data['data']
    message = Chunkedset.leave(set(data))
    return "machine leaving the system"



if __name__ == "__main__":
    hashtable = HashTable()
    app.run()
