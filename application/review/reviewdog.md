---
title: Reviewdog
---

## Reviewdog

## Install
```
$ brew install reviewdog/tap/reviewdog
$ brew upgrade reviewdog/tap/reviewdog
```

## CLI
reviewdog accepts any compiler or linter results from stdin and filters them by diff for review. reviewdog also can posts the results as a comment to GitHub if you use reviewdog in CI service.

- `-conf string`
    - config file path
- `-diff string`
    - diff command (e.g. "git diff") for local reporters. Do not use --relative flag for git command.
- `-efm value`
    - list of supported machine-readable format and errorformat (https://github.com/reviewdog/errorformat)
- `-f string`
    - format name (run -list to see supported format name) for input. It's also used as tool name in review comment if -name is empty
- `-f.diff.strip int`
    - option for -f=diff: strip NUM leading components from diff file names (equivalent to 'patch -p') (default is 1 for git diff) (default 1)
- `-fail-level value`
    - reviewdog will exit with code 1 if it finds at least 1 issue with severity greater than or equal to the given level. [none(default),any,info,warning,error]
- `-filter-mode value`
    - how to filter checks results. [added, diff_context, file, nofilter].
        - "added" (default)
            - Filter by added/modified diff lines.
        - "diff_context"
            - Filter by diff context, which can include unchanged lines.
            - i.e. changed lines +-N lines (e.g. N=3 for default git diff).
        - "file"
            - Filter by added/modified file.
        - "nofilter"
            - Do not filter any results.
- `-guess`
    - guess Pull Request ID by branch name and commit SHA
- `-level string`
    - default report level for supported reporters ("info","warning","error").
- `-list`
    - list supported pre-defined format names which can be used as -f arg
- `-log-level string`
    - log level for reviewdog itself. (debug, info, warning, error) (default "info")
- `-name string`
    - tool name in review comment. -f is used as tool name if -name is empty
- `-reporter string`
    - reporter of reviewdog results.
        - "local" (default)
            - Report results to stdout.
        - "rdjson"
            - Report results to stdout in rdjson format.
        - "rdjsonl"
            - Report results to stdout in rdjsonl format.
        - "sarif"
            - Report results to stdout in SARIF format.
        - "github-check"
            - Report results to GitHub Check. It works both for Pull Requests and commits. For Pull Request, you can see report results in GitHub PullRequest Check tab and can control filtering mode by -filter-mode flag. There are two options to use this reporter.
            - Option 1) Run reviewdog from GitHub Actions w/ secrets.GITHUB_TOKEN Note that it reports result to GitHub Actions log console for Pull Requests from fork repository due to GitHub Actions restriction. https://help.github.com/en/articles/virtual-environments-for-github-actions#github_token-secret Set REVIEWDOG_GITHUB_API_TOKEN with secrets.GITHUB_TOKEN. e.g.  REVIEWDOG_GITHUB_API_TOKEN: `${{ secrets.GITHUB_TOKEN }}`
            - Option 2) Install reviewdog GitHub Apps
                - 1. Install reviewdog Apps. https://github.com/apps/reviewdog
                - 2. Set REVIEWDOG_TOKEN or run reviewdog CLI in trusted CI providers. You can get token from https://reviewdog.app/gh/<owner>/<repo-name>.
                    - `$ export REVIEWDOG_TOKEN="xxxxx"`
                    - Note: Token is not required if you run reviewdog in Travis CI.
        - "github-pr-check"
            - Same as github-check reporter but it only supports Pull Requests.
        - "github-pr-review"
            - Report results to GitHub review comments.
            - 1. Set REVIEWDOG_GITHUB_API_TOKEN environment variable.
            - Go to https://github.com/settings/tokens and create new Personal access token with repo scope.
            - For GitHub Enterprise:
                - `$ export GITHUB_API="https://example.githubenterprise.com/api/v3"`
        - "github-annotations"
            - Report results to stdout in GitHub Actions annotation format.
        - "github-pr-annotations"
            - Same as github-annotations reporter but it only supports Pull Requests.
        - "gitlab-mr-discussion"
            - Report results to GitLab MergeRequest discussion.
            - 1. Set REVIEWDOG_GITLAB_API_TOKEN environment variable.
                - Go to https://gitlab.com/profile/personal_access_tokens
                - CI_API_V4_URL (defined by Gitlab CI) as the base URL for the Gitlab API automatically. Alternatively, GITLAB_API can also be defined, and it will take precedence over the former: `$ export GITLAB_API="https://example.gitlab.com/api/v4"`
        - "gitlab-mr-commit"
            - Same as gitlab-mr-discussion, but report results to GitLab comments for each commits in Merge Requests.
        - "gerrit-change-review"
            - Report results to Gerrit Change comments.
            - 1. Set GERRIT_USERNAME and GERRIT_PASSWORD for basic authentication or GIT_GITCOOKIE_PATH for git cookie based authentication.
            - 2. Set GERRIT_CHANGE_ID, GERRIT_REVISION_ID GERRIT_BRANCH and GERRIT_ADDRESS
                - For example:
                    - `$ export GERRIT_CHANGE_ID=myproject~master~I1293efab014de2`
                    - `$ export GERRIT_REVISION_ID=ed318bf9a3c`
                    - `$ export GERRIT_BRANCH=master`
                    - `$ export GERRIT_ADDRESS=http://localhost:8080`
        - "bitbucket-code-report"
            - Create Bitbucket Code Report via Code Insights (https://confluence.atlassian.com/display/BITBUCKET/Code+insights).
            - You can set custom report name with:
                - If running as part of Bitbucket Pipelines no additional configurations is needed.
                - If running outside of Bitbucket Pipelines you need to provide git repo data
                - (see documentation below for local reporters) and BitBucket credentials:
                - For Basic Auth you need to set following env variables: BITBUCKET_USER and BITBUCKET_PASSWORD
                - For AccessToken Auth you need to set BITBUCKET_ACCESS_TOKEN
                - To post results to Bitbucket Server specify BITBUCKET_SERVER_URL.
        - "gitea-pr-review"
            - Report results to Gitea review comments.
                - 1. Set REVIEWDOG_GITEA_API_TOKEN environment variable.
                    - Go to https://<gitea-server>/user/settings/applications and create new Access Token token with repo scope.
                - 2. Set GITEA_ADDRESS environment variable to your Gitea server base address.
                - For example: `$ export GITEA_ADDRESS=http://localhost:3000`
            - For GitHub Enterprise and self hosted GitLab or Gitea, set
                - REVIEWDOG_INSECURE_SKIP_VERIFY to skip verifying SSL (please use this at your own risk)
                - `$ export REVIEWDOG_INSECURE_SKIP_VERIFY=true`
                - For non-local reporters, reviewdog automatically get necessary data from environment variable in CI service (GitHub Actions, Travis CI, Circle CI, drone.io, GitLab CI, Bitbucket Pipelines). You can set necessary data with following environment variable manually if you want (e.g. run reviewdog in Jenkins).
                - `$ export CI_PULL_REQUEST=14 # Pull Request number (e.g. 14)`
                - `$ export CI_COMMIT="$(git rev-parse @)" # SHA1 for the current build`
                - `$ export CI_REPO_OWNER="haya14busa" # repository owner`
                - `$ export CI_REPO_NAME="reviewdog" # repository name`
        - (default "local")
- -runners string
    - comma separated runners name to run in config file. default: run all runners
- -strip int
    - strip NUM leading components from diff file names (equivalent to 'patch -p') (default is 1 for git diff) (default 1)
- -tee
    - enable "tee"-like mode which outputs tools's output as is while reporting results to -reporter. Useful for debugging as well.
- -version
    - print version

## Reference
https://github.com/reviewdog/reviewdog
