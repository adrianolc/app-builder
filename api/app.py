from flask import Flask
from .github import Github

def start_app():
    app = Flask('app-builder')
    github = Github()

    @app.route('/')
    def index():
        return 'App Builder api version 1.0'

    @app.route('/branches')
    def get_branches():
        return github.list_branches()

    @app.route('/branches/<branch>')
    def get_branch(branch):
        return github.branch_detail(branch)

    app.run()
