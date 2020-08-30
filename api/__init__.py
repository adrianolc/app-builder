from flask import Flask, Response, send_from_directory
from api.github_api import GithubApi
from build_android.build import Build

import settings

MIME_TYPE = 'application/json'

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    github = GithubApi(settings.GITHUB_URL, settings.GITHUB_TOKEN)
    build = Build(settings.GITHUB_REPO_URL, settings.GITHUB_REPO_NAME)

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
        build.build(commit, build_variant)

        path = f'{settings.APK_PATH}/{build_variant}'
        apk = f'app-{build_variant}.apk'

        return send_from_directory(path, apk, as_attachment=True)

    def __make_response(response):
        return Response(response, mimetype=MIME_TYPE)

    return app
