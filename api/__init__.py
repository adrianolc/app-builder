from flask import Flask, Response
from .github import Github

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    github = Github()

    @app.route('/')
    def index():
        return 'App Builder api version 1.0'

    @app.route('/branches')
    def get_branches():
        return Response(
            github.list_branches(), mimetype='application/json'
        )

    @app.route('/branches/<branch>')
    def get_branch(branch):
        return Response(
            github.branch_detail(branch), mimetype='application/json'
        )

    return app
