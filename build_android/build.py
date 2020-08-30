from git.git_cmd import GitCmd

class Build(GitCmd):
    def __init__(self, repo_url, repo):
        self.__repo_url = repo_url
        self.__repo = repo

    def build(self, commit, build_variant):
        self.clone(self.__repo_url)
        self.checkout(commit, self.__repo)

        self._run_command(f'./gradlew assemble{build_variant.capitalize()}', self.__repo)

    