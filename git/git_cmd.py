from subprocess import Popen, PIPE
from shlex import split as split_command

class GitCmd:
    def clone(self, repo_url):
        self._run_command(f'git clone "{repo_url}"')
    
    def checkout(self, commit, repo):
        self._run_command(f'git checkout {commit}', repo)
    
    def _run_command(self, command, dir=None):
        print(f'Excuting command: {command}\n')

        process = Popen(split_command(command),
                    cwd=dir,
                    stdout=PIPE,
                    universal_newlines=True)

        stdout, stderr = process.communicate()

        if stdout:
            print(stdout)

        if stderr:
            print(stderr)
    