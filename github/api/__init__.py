from flask import Flask, request, json, make_response
from config import env
from api.github_api import GithubApi

def json_response(data):
    js = json.dumps(data)

    response = make_response(js)
    response.mimetype = "application/json"

    return response 

def create_app():
    app = Flask(__name__)
    github = GithubApi(env['GITHUB_BASE_URL'], env['GITHUB_TOKEN'])

    @app.route('/branches')
    def get_branches():
        page = request.args.get("page")

        return json_response(github.list_branches(page))

    @app.route('/branches/<path:branch>')
    def get_branch(branch):
        return json_response(github.branch_detail(branch))
    
    @app.route('/tags')
    def get_tags():
        page = request.args.get("page")

        return json_response(github.list_tags(page))

    return app
