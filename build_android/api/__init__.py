from flask import Flask, send_from_directory
from api.gradle_build import Gradle
from config import env


def create_app():
    app = Flask(__name__)
    gradle = Gradle(env['REPO_NAME'], env['REPO_URL'])

    @app.route('/build/<path:commit>/<build_variant>')
    def build(commit, build_variant):
        gradle.make_apk(commit, build_variant)

        path = f'{env["APK_PATH"]}/{build_variant}'
        apk = f'app-{build_variant}.apk'

        return send_from_directory(path, apk, as_attachment=True)

    return app