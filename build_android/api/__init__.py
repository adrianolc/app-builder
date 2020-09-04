from flask import Flask, send_from_directory
from api.gradle_build import Gradle
from config import env
from os import path

BASE_DIR = path.dirname(path.realpath(__file__))

def create_app():
    app = Flask(__name__)
    gradle = Gradle(env['REPO_NAME'], env['REPO_URL'])

    @app.route('/start/<path:commit>/<build_variant>')
    def build(commit, build_variant):
        gradle.make_apk(commit, build_variant)

        return { 
            'message'   : 'Build started',
            'url'       : f'/build/download/{build_variant}'
        }, 202

    @app.route('/download/<build_variant>')
    def get_apk(build_variant):
        apk_path = f'{env["APK_PATH"]}/{build_variant}'
        apk = f'app-{build_variant}.apk'

        if path.isfile(f'{BASE_DIR}/{apk_path}/{apk}'):
            return send_from_directory(apk_path, apk, as_attachment=True)

        return { 'message' : 'Build still running' }, 202

    return app