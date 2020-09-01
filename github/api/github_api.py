from dotenv import load_dotenv
from requests import get

import json
import os

load_dotenv()

BASE_URL = os.getenv('GITHUB_BASE_URL')
BASE_HEADER = { 
    'Authorization' : f'token {os.getenv("GITHUB_TOKEN")}', 
    'Accept' : 'application/vnd.github.v3+json' 
}    

def list_branches():
    url = f'{BASE_URL}/branches?per_page=100'

    __print_making_request(url)

    req = get(url, headers=BASE_HEADER)

    return req.text

def branch_detail(branch):
    url = f'{BASE_URL}/branches/{branch}'

    __print_making_request(url)

    req = get(url, headers=BASE_HEADER)

    return req.text

def list_tags():
    url = f'{BASE_URL}/tags?per_page=100'

    __print_making_request(url)

    req = get(url, headers=BASE_HEADER)

    return req.text

def __print_making_request(url):
    print(f'Making request on: {url}')
    
