from config import env

import api.git_cmd as git

def make_apk(commit, build_variant):
    git.clone(env['REPO_URL'])
    git.checkout(commit, env['REPO_NAME'])

    git.run_command(f'./gradlew clean assemble{build_variant.capitalize()}' \
                    ' --stacktrace --no-daemon' \
                    ' -x ktlintFormat -x ktlint' \
                    ' -Dorg.gradle.jvmargs=-Xmx2048m\ -XX:MaxPermSize=512m\ -XX:+HeapDumpOnOutOfMemoryError\ -Dfile.encoding=UTF-8' \
                    ' -Dorg.gradle.daemon=false' \
                    ' -Dorg.gradle.caching=true' \
                    ' -Dorg.gradle.configureondemand=true' \
                    ' -Dkotlin.compiler.execution.strategy=in-process' \
                    ' -Dkotlin.incremental=false', 
                    env['REPO_NAME'])
