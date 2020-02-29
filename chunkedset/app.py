'''

Starter app dispatching all applications

'''

from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound

import sys
sys.path.insert(0, chunkedset)

from chunk1 import app as chunk1
from chunk2 import app as chunk2
from chunk3 import app as chunk3
from server import app as server

app = Flask(__name__)

app.wsgi_app = DispatcherMiddleware(NotFound(), {
    "/chunk1": chunk1,
    '/chunk2': chunk2,
    '/chunk3': chunk3,
    '/server':server
})

if __name__ == "__main__":
    app.run()
