from flask import Flask, Response
from .github import Github

MIME_TYPE = 'application/json'

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    github = Github()

    @app.route('/')
    def index():
        return 'App Builder api version 1.0'

    @app.route('/branches')
    def get_branches():
        return Response(
            github.list_branches(), mimetype=MIME_TYPE
        )

    @app.route('/branches/<path:branch>')
    def get_branch(branch):
        return Response(
            github.branch_detail(branch), mimetype=MIME_TYPE
        )

    return app
