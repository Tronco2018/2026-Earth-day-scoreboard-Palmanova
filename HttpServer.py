from flask import Flask, render_template
from Logger import Logger
from werkzeug.serving import make_server
import threading
app = Flask(__name__)


import logging
logging.getLogger('werkzeug').disabled = True

@app.route("/")
def home():
    return render_template("index.html")


class Server_runner:
    def __init__(self):
        self.server = None
        self.thread = None

    def run(self, port):
        self.server = make_server("0.0.0.0", port, app)
        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.start()

    def stop(self):
        if self.server:
            self.server.shutdown()
        if self.thread:
            self.thread.join()
        Logger.info("HTTP server stopped")