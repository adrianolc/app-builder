from dotenv import load_dotenv

import api.git_cmd as git
import os

load_dotenv()

__REPO_URL = os.getenv('REPO_URL')
__REPO_NAME = os.getenv('REPO_NAME')

def make_apk(commit, build_variant):
    git.clone(__REPO_URL)
    git.checkout(commit, __REPO_NAME)

    git.run_command(f'./gradlew assemble{build_variant.capitalize()} --no-daemon --debug', __REPO_NAME)
