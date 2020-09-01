from subprocess import Popen, PIPE
from shlex import split as split_command

def clone(repo_url):
    run_command(f'git clone "{repo_url}"')

def checkout(commit, repo):
    run_command(f'git checkout {commit}', repo)
    run_command(f'git pull origin {commit}', repo)

def run_command(command, dir=None):
    print(f'Excuting command: {command}\n')

    process = Popen(split_command(command),
                cwd=dir,
                bufsize=-1)

    process.wait()
