from .github import GitCmd

import settings

class Build(GitCmd):
    def build(self, commit):
        self.clone()
        self.checkout(commit)

        self._run_command('./gradlew assembleDebug', settings.GITHUB_REPO_NAME)
    