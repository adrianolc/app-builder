from subprocess import Popen, PIPE
from shlex import split as split_command

class GitCmd:
    def clone(self, repo_url):
        self._run_command(f'git clone {repo_url}')
    
    def checkout(self, commit, repo):
        self._run_command(f'git checkout {commit}', repo)
    
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
    

class Build(GitCmd):
    def __init__(self, repo_url, repo):
        self.__repo_url = repo_url
        self.__repo = repo

    def build(self, commit, build_variant):
        self.clone(self.__repo_url)
        self.checkout(commit, self.__repo)

        self._run_command(f'./gradlew assemble{build_variant.capitalize()}', self.__repo)

    