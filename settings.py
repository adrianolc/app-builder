import os
import api.app as app
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_URL = os.getenv('GITHUB_BASE_URL')

if __name__ == "__main__":
    app.start_app()
        
