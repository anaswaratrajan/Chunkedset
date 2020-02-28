'''
Application mimicing actions of master machine. Master machine is responsible
for carrying out all operations corresponding to actions from the machine applications

'''

from flask import Flask
import requests

app = Flask(__name__)

data = {
'machine':1,
'data':[1,2,3,4,5]
}

@app.route("/")
def index():

    return "master machine"


@app.route("/join", methods = ["GET","POST"])
def join_system():
    '''
    Pending : Join the requested machine to system
    '''

    request = request.get_json(force=True)
    machine = request["machine"]

    return "new machine joining the system"


@app.route("/leave")
def leave():
    '''
    Pending : Remove the requested machine from system
    '''
    return "machine leaving the system"


if __name__ == "__main__":
    app.run()
