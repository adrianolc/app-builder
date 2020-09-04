from subprocess import Popen, PIPE
from shlex import split as split_command

def clone(repo_url):
    run_command(f'git clone "{repo_url}"', wait=True)

def checkout(commit, repo):
    run_command(f'git checkout {commit}', dir=repo, wait=True)
    run_command(f'git pull origin {commit}', dir=repo, wait=True)

def run_command(command, dir=None, wait=False):
    print(f'Excuting command: {command}\n')

    process = Popen(split_command(command),
                cwd=dir,
                bufsize=-1)

    if wait:
        process.wait()
