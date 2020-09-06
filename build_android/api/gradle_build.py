from threading import Thread
from pathlib import Path
from os import path, makedirs
from config import env
from shutil import move

import api.git_cmd as git

ROOT_DIR = path.dirname(path.realpath(__file__))

def get_apk_path(build_variant):
    apk_path = f'{env["APK_PATH"]}/{build_variant}'
    apk = f'app-{build_variant}.apk'

    return f'{ROOT_DIR}/{apk_path}/{apk}'

class Build:
    def __init__(self, repo_name, repo_url):
        self.__repo_name = repo_name
        self.__repo_url = repo_url

    def __run_gradle_background(self, build_variant, apk_id):
        git.run_command(f'./gradlew clean assemble{build_variant.capitalize()}' \
                        ' --stacktrace --no-daemon' \
                        ' -x ktlintFormat -x ktlint' \
                        ' -Dorg.gradle.jvmargs=-Xmx1024m' \
                        ' -Dorg.gradle.daemon=false' \
                        ' -Dkotlin.compiler.execution.strategy=in-process' \
                        ' -Dkotlin.incremental=false', 
                        self.__repo_name)

        new_file = self.make_apk_path(apk_id)
        makedirs(path.dirname(new_file), exist_ok=True)
        move(get_apk_path(build_variant), new_file)

    def make_apk(self, commit, build_variant, apk_id):
        git.clone(self.__repo_url)
        git.checkout(commit, self.__repo_name)

        Thread(
            target=self.__run_gradle_background,
            args=(build_variant, apk_id, )
        ).start()
    
    def make_apk_path(self, apk_id):
        return f'{ROOT_DIR}/{apk_id}/app.apk'

