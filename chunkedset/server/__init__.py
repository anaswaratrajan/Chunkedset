'''
Application mimicing actions of server. The hashes of each datapoint
in every chunk is stored in the server.

'''

from flask import Flask, request
import requests

import os,inspect
server = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
chunkedset = os.path.dirname(server)
from chunkedset import ChunkedSet
import sys
sys.path.insert(0, chunkedset)


app = Flask(__name__)


@app.route("/")
def index():

    return "master machine"


@app.route("/join", methods = ["GET","POST"])
def join_system():
    '''
    Pending : Join the requested machine to system
    '''
    new_data = request.get_json(force=True)
    data = new_data['data']
    print(data)
    chunk = new_data['chunk']
    return "new machine joining the system"


@app.route("/leave")
def leave():
    '''
    Pending : Remove the requested machine from system
    '''
    return "machine leaving the system"



if __name__ == "__main__":
    hashtable = HashTable()
    app.run()
