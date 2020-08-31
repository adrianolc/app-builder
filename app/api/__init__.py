from dotenv import load_dotenv
from flask import Flask, Response, send_from_directory
from api.github_api import GithubApi

import os


load_dotenv()
MIME_TYPE = 'application/json'

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    github = GithubApi(os.getenv('GITHUB_BASE_URL'), os.getenv('GITHUB_TOKEN'))

    @app.route('/')
    def index():
        return 'App Builder api version 1.0'

    @app.route('/branches')
    def get_branches():
        return __make_response(github.list_branches())

    @app.route('/branches/<path:branch>')
    def get_branch(branch):
        return __make_response(github.branch_detail(branch))
    
    @app.route('/tags')
    def get_tags():
        return __make_response(github.list_tags())

    @app.route('/build/<commit>/<build_variant>')
    def get_build(commit, build_variant):
        return __make_response('call build here')

    def __make_response(response):
        return Response(response, mimetype=MIME_TYPE)

    return app
