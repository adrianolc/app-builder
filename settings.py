from dotenv import load_dotenv

import os

load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_URL = os.getenv('GITHUB_BASE_URL')
