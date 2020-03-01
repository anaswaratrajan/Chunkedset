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
sys.path.insert(0, chunkedset)'''Adding the module in parent class containing the
chunkset classes into sys.path'''


app = Flask(__name__)
Chunkedset = ChunkedSet()

@app.route("/")
def index():
    '''Shows the chunkedlist'''
    chunked_set = dict()
    cset = Chunkedset.get_node()
    chunked_set['cset']=cset
    js_dump = json.dumps(chunked_set)
    return js_dump


@app.route("/join", methods = ["POST"])
def join_system():
    '''
    Join the requested chunk to chunkedset
    '''
    new_data = request.get_json(force=True)
    data = new_data['data']
    duplicates = Chunkedset.join(set(data))
    r = dict()
    r['duplicates']=list(duplicates)
    r['chunk']=new_data['chunk']
    d = json.dumps(r)
    path = "http://127.0.0.1:5000/chunk{0}/update".format(new_data['chunk'])
    r = requests.post(url = path, data = d)
    json_data = json.loads(r.text)
    return jsonify(json_data)


@app.route("/leave", methods = ["POST"])
def leave():
    '''
    Pending : Remove the chunk from chunkedset
    '''
    new_data = request.get_json(force=True)
    data = new_data['data']
    message = Chunkedset.leave(set(data))
    return jsonify({'message':'Success'})


if __name__ == "__main__":
    app.run()
