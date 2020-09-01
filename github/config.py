from dotenv import load_dotenv

import os

load_dotenv()

env = {
    'GITHUB_TOKEN' : os.getenv('GITHUB_TOKEN'),
    'GITHUB_BASE_URL' : os.getenv('GITHUB_BASE_URL')
}