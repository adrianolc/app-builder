from requests import get
from subprocess import Popen, PIPE
from shlex import split as split_command

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

class GitCmd:
    def clone(self):
        self._run_command(f'git clone {settings.GITHUB_REPO_URL}')
    
    def checkout(self, commit):
        self._run_command(f'git checkout {commit}', settings.GITHUB_REPO_NAME)
    
    def _run_command(self, command, dir=None):
        print(f'Excuting command: {command}\n')

        process = Popen(split_command(command),
                    cwd=dir,
                    stdout=PIPE,
                    universal_newlines=True)

        while True:
            output = process.stdout.readline()
            print(output.strip())

            if process.poll() is not None:
                break
    
