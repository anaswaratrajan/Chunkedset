'''

Starter app dispatching all applications

'''

from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound

from machine1 import app as machine1
from machine2 import app as machine2
from machine3 import app as machine3
from master_machine import app as master

app = Flask(__name__)

app.wsgi_app = DispatcherMiddleware(NotFound(), {
    "/machine1": machine1,
    '/machine2': machine2,
    '/machine3': machine3,
    '/master':master
})

if __name__ == "__main__":
    app.run()
