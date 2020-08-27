from flask import Flask, Response
from .github import GithubApi
from .build import Build

MIME_TYPE = 'application/json'

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    github = GithubApi()
    build = Build()

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

    @app.route('/build/<commit>')
    def get_build(commit):
        build.build(commit)

        return __make_response('Success!!!')

    def __make_response(response):
        return Response(response, mimetype=MIME_TYPE)

    return app
