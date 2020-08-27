from .github import GitCmd

import settings

class Build(GitCmd):
    def build(self, commit, build_variant):
        self.clone()
        self.checkout(commit)

        self._run_command(f'./gradlew assemble{build_variant.capitalize()}', settings.GITHUB_REPO_NAME)
    