from requests import get

import settings
import json

class GithubApi:
    def __init__(self):
        self.__base_url = settings.GITHUB_URL
        self.__base_header = {
            'Authorization' : f'token {settings.GITHUB_TOKEN}',
            'Accept' : 'application/vnd.github.v3+json'
        }

    def list_branches(self):
        url = f'{self.__base_url}/branches?per_page=100'

        self.__print_making_request(url)

        req = get(url, headers=self.__base_header)

        return req.text

    def branch_detail(self, branch):
        url = f'{self.__base_url}/branches/{branch}'

        self.__print_making_request(url)

        req = get(url, headers=self.__base_header)

        return req.text

    def list_tags(self):
        url = f'{settings.GITHUB_URL}/tags?per_page=100'

        self.__print_making_request(url)

        req = get(url, headers=self.__base_header)

        return req.text

    def __print_making_request(self, url):
        print(f'Making request on: {url}')
