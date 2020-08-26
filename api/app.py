from flask import Flask

__app = Flask(__name__)

@__app.route('/')
def index():
    return 'App Builder api version 1.0'


def start_app():
    __app.run()