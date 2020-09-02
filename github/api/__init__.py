from flask import Flask, current_app
from config import env
from api.github_api import GithubApi

def create_app():
    app = Flask(__name__)
    github = GithubApi(env['GITHUB_BASE_URL'], env['GITHUB_TOKEN'])

    @app.route('/branches')
    def get_branches():
        return current_app.make_response(github.list_branches())

    @app.route('/branches/<path:branch>')
    def get_branch(branch):
        return current_app.make_response(github.branch_detail(branch))
    
    @app.route('/tags')
    def get_tags():
        return current_app.make_response(github.list_tags())

    return app
