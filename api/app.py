from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'App Builder api version 1.0'

app.run()
