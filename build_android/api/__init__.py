from flask import Flask, send_from_directory
from config import env

import api.gradle_build as gradle

def create_app():
    app = Flask(__name__)

    @app.route('/build/<path:commit>/<build_variant>')
    def build(commit, build_variant):
        gradle.make_apk(commit, build_variant)

        path = f'{env["APK_PATH"]}/{build_variant}'
        apk = f'app-{build_variant}.apk'

        return send_from_directory(path, apk, as_attachment=True)

    return app