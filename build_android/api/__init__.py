from flask import Flask, send_file
from api.gradle_build import Build
from config import env
from datetime import datetime
from os import path

def create_app():
    app = Flask(__name__)
    build = Build(env['REPO_NAME'], env['REPO_URL'])

    @app.route('/start/<path:commit>/<build_variant>')
    def start_build(commit, build_variant):
        apk_id = datetime.today().strftime('%Y%m%d_%H%M%S')
        build.make_apk(commit, build_variant, apk_id)

        return { 
            'message'   : 'Build started',
            'url'       : f'/build/download/{apk_id}'
        }, 202

    @app.route('/download/<apk_id>')
    def get_apk(apk_id):
        apk_path = build.make_apk_path(apk_id)

        if path.isfile(apk_path):
            return send_file(apk_path, as_attachment=True)

        return { 'message' : 'Build still running' }, 202

    return app