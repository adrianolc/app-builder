from dotenv import load_dotenv
from git.git_cmd import GitCmd

import os

load_dotenv()

class Build(GitCmd):
    def __init__(self):
        self.__repo_url = os.getenv('REPO_URL')
        self.__repo = os.getenv('REPO_NAME')
        self.__apk_path = os.getenv('APK_PATH')

    def build(self, commit, build_variant):
        self.clone(self.__repo_url)
        self.checkout(commit, self.__repo)

        self._run_command(f'./gradlew assemble{build_variant.capitalize()}', self.__repo)

    