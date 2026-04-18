from flask import *
from Logger import Logger
from werkzeug.serving import make_server
import threading
app = Flask(__name__, static_folder='templates')


import logging
logging.getLogger('werkzeug').disabled = True

from Config_interface import Config_interface
config = Config_interface()

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/style.css')
def style():
    return send_file('templates/style.css', mimetype='text/css')


@app.route('/script.js')
def script():
    return send_file('templates/script.js', mimetype='text/javascript')

@app.route('/scores.json')
def scores():
    return send_file('scores.json')

@app.route('/fonts/Cirno.ttf')
def font():
    return send_file("templates/fonts/Cirno.ttf")

class Server_runner:
    def __init__(self):
        self.server = None
        self.thread = None

    def run(self):
        self.server = make_server(config.get_property("BINDING"), config.get_property("PORT"), app)
        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.start()

    def stop(self):
        if self.server:
            self.server.shutdown()
        if self.thread:
            self.thread.join()
        Logger.info("HTTP server stopped")