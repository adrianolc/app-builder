from flask import Flask, Response
from .github import GithubApi, GitCmd

MIME_TYPE = 'application/json'

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    github = GithubApi()
    git_cmd = GitCmd()

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

    @app.route('/clone')
    def get_clone():
        git_cmd.clone()

        return __make_response('Clone success!!')

    @app.route('/clone/checkout/<commit>')
    def get_checkout(commit):
        git_cmd.checkout(commit)

        return __make_response('Checkout success!!!')

    def __make_response(response):
        return Response(response, mimetype=MIME_TYPE)

    return app
