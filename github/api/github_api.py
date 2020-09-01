from requests import get

class GithubApi:
    def __init__(self, base_url, token):
        self.__base_url = base_url
        self.__base_header = { 
            'Authorization' : f'token {token}', 
            'Accept' : 'application/vnd.github.v3+json' 
        }    

    def list_branches(self):
        url = f'{self.__base_url}/branches?per_page=100'

        __print_making_request(url)

        req = get(url, headers=self.__base_header)

        return req.text

    def branch_detail(self, branch):
        url = f'{self.__base_url}/branches/{branch}'

        __print_making_request(url)

        req = get(url, headers=self.__base_header)

        return req.text

    def list_tags(self):
        url = f'{self.__base_url}/tags?per_page=100'

        __print_making_request(url)

        req = get(url, headers=self.__base_header)

        return req.text

def __print_making_request(url):
    print(f'Making request on: {url}')