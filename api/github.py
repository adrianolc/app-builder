from requests import get
import settings

STATUS_OK = 200

class Github:
    def __init__(self):
        self.__base_url = settings.GITHUB_URL
        self.__base_header = {
            'Authorization' : 'token {}'.format(settings.GITHUB_TOKEN),
            'Accept' : 'application/vnd.github.v3+json'
        }

    def list_branches(self):
        url = '{}/repos/chocoapp/choco-droid/branches?per_page=100'.format(self.__base_url)

        self.__print_making_request(url)

        req = get(url, headers=self.__base_header)

        return req.text

    def branch_detail(self, branch):
        url = '{0}/repos/chocoapp/choco-droid/branches/{1}'.format(self.__base_url, branch)

        self.__print_making_request(url)

        req = get(url, headers=self.__base_header)

        return req.text

    def __print_making_request(self, url):
        print('Making request on: {}'.format(url))
