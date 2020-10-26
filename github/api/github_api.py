from requests import get

class GithubApi:
    def __init__(self, base_url, token):
        self.__base_url = base_url
        self.__base_header = { 
            'Authorization' : f'token {token}', 
            'Accept' : 'application/vnd.github.v3+json' 
        }    

    def list_branches(self, page):
        url = f'{self.__base_url}/branches?per_page=10&page={page}'
        req = get(url, headers=self.__base_header)

        return req.json()

    def branch_detail(self, branch):
        url = f'{self.__base_url}/branches/{branch}'
        req = get(url, headers=self.__base_header)

        return req.text

    def list_tags(self, page):
        url = f'{self.__base_url}/tags?per_page=10&page={page}'
        req = get(url, headers=self.__base_header)

        return req.text
