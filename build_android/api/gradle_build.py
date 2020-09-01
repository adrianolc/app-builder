import api.git_cmd as git

class Gradle:
    def __init__(self, repo_name, repo_url):
        self.__repo_name = repo_name
        self.__repo_url = repo_url

    def make_apk(self, commit, build_variant):
        git.clone(self.__repo_url)
        git.checkout(commit, self.__repo_name)

        git.run_command(f'./gradlew clean assemble{build_variant.capitalize()}' \
                        ' --stacktrace --no-daemon' \
                        ' -x ktlintFormat -x ktlint' \
                        ' -Dorg.gradle.jvmargs=-Xmx2048m\ -XX:MaxPermSize=512m\ -XX:+HeapDumpOnOutOfMemoryError\ -Dfile.encoding=UTF-8' \
                        ' -Dorg.gradle.daemon=false' \
                        ' -Dorg.gradle.caching=true' \
                        ' -Dorg.gradle.configureondemand=true' \
                        ' -Dkotlin.compiler.execution.strategy=in-process' \
                        ' -Dkotlin.incremental=false', 
                        self.__repo_name)
