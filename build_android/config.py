from dotenv import load_dotenv

import os

load_dotenv()

env = {
    'REPO_URL' : os.getenv('REPO_URL'),
    'REPO_NAME' : os.getenv('REPO_NAME'),
    'APK_PATH' : os.getenv('APK_PATH')
}