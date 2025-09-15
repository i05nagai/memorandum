---
title: renovate
---

## renovate

## Example
```json
{
  "packageRules": [
    {
      "matchUpdateTypes": ["minor", "patch", "pin", "digest"],
      "automerge": true
    }
  ]
}
```

```json
{
  "customManagers": [
    {
      "customType": "regex",
      "managerFilePatterns": ["/values.yaml$/"],
      "matchStrings": [
        "image:\\s+(?<depName>my\\.old\\.registry/aRepository/andImage):(?<currentValue>[^\\s]+)"
      ],
      "depNameTemplate": "my.new.registry/aRepository/andImage",
      "autoReplaceStringTemplate": "image: {{{depName}}}:{{{newValue}}}",
      "datasourceTemplate": "docker"
    }
  ]
}
```

## Run

```
RENOVATE_CONFIG_FILE=renovate.json LOG_LEVEL=debug npx renovate --token $GITHUB_TOKEN --require-config=ignored <reponame>
```

## Presets
https://docs.renovatebot.com/config-presets/
https://docs.renovatebot.com/presets-config/

## Configuration
https://docs.renovatebot.com/configuration-options/


### matchDepTypes


### schedule



## CLI

- `--mode <string>`
    - Mode of operation.
- `--allowed-headers <array>`
    - List of allowed patterns for header names in repository hostRules config.
- `--autodiscover-repo-order <string>`
    - The order method for autodiscover server side repository search.
- `--autodiscover-repo-sort <string>`
    - The sort method for autodiscover server side repository search.
--allowed-env <array>                                        List of allowed patterns for environment variable names in repository env config.
--detect-global-manager-config [boolean]                     If `true`, Renovate tries to detect global manager configuration from the file system.
--detect-host-rules-from-env [boolean]                       If `true`, Renovate tries to detect host rules from environment variables.
--merge-confidence-endpoint <string>                         If set, Renovate will query this API for Merge Confidence data.
--merge-confidence-datasources <array>                       If set, Renovate will query the merge-confidence JSON API only for datasources that are part of this list.
--use-cloud-metadata-services [boolean]                      If `false`, Renovate does not try to access cloud metadata services.
--user-agent <string>                                        If set to any string, Renovate will use this as the `user-agent` it sends with HTTP requests.
--allow-post-upgrade-command-templating [boolean]            Set this to `false` to disable template compilation for post-upgrade commands.
--allowed-post-upgrade-commands <array>                      A list of regular expressions that decide which post-upgrade tasks are allowed.
--post-upgrade-tasks <object>                                Post-upgrade tasks that are executed before a commit is made by Renovate.
--onboarding-no-deps [boolean]                               Onboard the repository even if no dependencies are found.
--config-migration [boolean]                                 Enable this to get config migration PRs when needed.
--product-links <object>                                     Links which are used in PRs, issues and comments.
--secrets <object>                                           Object which holds secret name/value pairs.
--status-check-names <object>                                Custom strings to use as status check names.
--migrate-presets <object>                                   Define presets here which have been removed or renamed and should be migrated automatically.
--preset-cache-persistence [boolean]                         Cache resolved presets in package cache.
--global-extends <array>                                     Configuration presets to use or extend for a self-hosted config.
--enabled [boolean]                                          Enable or disable Renovate bot.
--repository-cache <string>                                  This option decides if Renovate uses a JSON cache to speed up extractions.
--repository-cache-type <string>                             Set the type of renovate repository cache if `repositoryCache` is enabled.
--report-type <string>                                       Set how, or if, reports should be generated.
--report-path <string>                                       Path to where the file should be written. In case of `s3` this has to be a full S3 URI.
--force-cli [boolean]                                        Decides if CLI configuration options are moved to the `force` config section.
--draft-p-r [boolean]                                        If set to `true` then Renovate creates draft PRs, instead of normal status PRs.
--dry-run <string>                                           If enabled, perform a dry run by logging messages instead of creating/updating/deleting branches and PRs.
--print-config [boolean]                                     If enabled, Renovate logs the fully resolved config for each repository, plus the fully resolved presets.
--binary-source <string>                                     Controls how third-party tools like npm or Gradle are called: directly, via Docker sidecar containers, or via dynamic install.
--redis-url <string>                                         If set, this Redis URL will be used for caching instead of the file system.
--redis-prefix <string>                                      Key prefix for redis cache entries.
--base-dir <string>                                          The base directory for Renovate to store local files, including repository files and cache. If left empty, Renovate will create its own temporary directory to use.
--cache-dir <string>                                         The directory where Renovate stores its cache. If left empty, Renovate creates a subdirectory within the `baseDir`.
--containerbase-dir <string>                                 The directory where Renovate stores its containerbase cache. If left empty, Renovate creates a subdirectory within the `cacheDir`.
--custom-env-variables <object>                              Custom environment variables for child processes and sidecar Docker containers.
--env <object>                                               Environment variables that Renovate uses when executing package manager commands.
--custom-datasources <object>                                Defines custom datasources for usage by managers.
--docker-child-prefix <string>                               Change this value to add a prefix to the Renovate Docker sidecar container names and labels.
--docker-cli-options <string>                                Pass CLI flags to `docker run` command when `binarySource=docker`.
--docker-sidecar-image <string>                              Change this value to override the default Renovate sidecar image.
--docker-user <string>                                       Set the `UID` and `GID` for Docker-based binaries if you use `binarySource=docker`.
--composer-ignore-platform-reqs <array>                      Configure use of `--ignore-platform-reqs` or `--ignore-platform-req` for the Composer package manager.
--go-get-dirs <array>                                        Directory pattern to run `go get` on.
--log-file <string>                                          Log file path.
--log-file-level <string>                                    Set the log file log level.
--log-context <string>                                       Add a global or per-repo log context to each log entry.
--onboarding [boolean]                                       Require a Configuration PR first.
--onboarding-config <object>                                 Configuration to use for onboarding PRs.
--onboarding-rebase-checkbox [boolean]                       Set to enable rebase/retry markdown checkbox for onboarding PRs.
--fork-processing <string>                                   Whether to process forked repositories. By default, all forked repositories are skipped when in `autodiscover` mode.
--include-mirrors [boolean]                                  Whether to process repositories that are mirrors. By default, repositories that are mirrors are skipped.
--fork-creation [boolean]                                    Whether to create forks as needed at runtime when running in "fork mode".
--fork-token <string>                                        Set a personal access token here to enable "fork mode".
--fork-org <string>                                          The preferred organization to create or find forked repositories, when in fork mode.
--github-token-warn [boolean]                                Display warnings about GitHub token not being set.
--encrypted-warning <string>                                 Warning text to use if encrypted config is found.
--inherit-config [boolean]                                   If `true`, Renovate will inherit configuration from the `inheritConfigFileName` file in `inheritConfigRepoName`.
--inherit-config-repo-name <string>                          Renovate will look in this repo for the `inheritConfigFileName`.
--inherit-config-file-name <string>                          Renovate will look for this config file name in the `inheritConfigRepoName`.
--inherit-config-strict [boolean]                            If `true`, any `inheritedConfig` fetch error will result in an aborted run.
--require-config <string>                                    Controls Renovate's behavior regarding repository config files such as `renovate.json`.
--optimize-for-disabled [boolean]                            Set to `true` to perform a check for disabled config prior to cloning.
--dependency-dashboard [boolean]                             Whether to create a "Dependency Dashboard" issue in the repository.
--dependency-dashboard-approval [boolean]                    Controls if updates need manual approval from the Dependency Dashboard issue before PRs are created.
--dependency-dashboard-autoclose [boolean]                   Set to `true` to let Renovate close the Dependency Dashboard issue if there are no more updates.
--dependency-dashboard-title <string>                        Title for the Dependency Dashboard issue.
--dependency-dashboard-header <string>                       Any text added here will be placed first in the Dependency Dashboard issue body.
--dependency-dashboard-footer <string>                       Any text added here will be placed last in the Dependency Dashboard issue body, with a divider separator before it.
--dependency-dashboard-labels <array>                        These labels will always be applied on the Dependency Dashboard issue, even when they have been removed manually.
--dependency-dashboard-o-s-v-vulnerability-summary <string>  Control if the Dependency Dashboard issue lists CVEs supplied by [osv.dev](https://osv.dev).
--config-warning-reuse-issue [boolean]                       Set this to `false` to make Renovate create a new issue for each config warning, instead of reopening or reusing an existing issue.
--private-key <string>                                       Server-side private key.
--private-key-old <string>                                   Secondary or old private key to try.
--private-key-path <string>                                  Path to the Server-side private key.
--private-key-path-old <string>                              Path to the Server-side old private key.
--encrypted <object>                                         An object containing configuration encrypted with project key.
--timezone <string>                                          Must conform to [IANA Time Zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) format.
--schedule <array>                                           Limit branch creation to these times of day or week.
--automerge-schedule <array>                                 Limit automerge to these times of day or week.
--update-not-scheduled [boolean]                             Whether to update branches when not scheduled. Renovate will not create branches outside of the schedule.
--persist-repo-data [boolean]                                If set to `true`: keep repository data between runs instead of deleting the data.
--expose-all-env [boolean]                                   Set this to `true` to allow passing of all environment variables to package managers.
--allow-plugins [boolean]                                    Set this to `true` if repositories are allowed to run install plugins.
--allow-scripts [boolean]                                    Set this to `true` if repositories are allowed to run install scripts.
--allow-custom-crate-registries [boolean]                    Set this to `true` to allow custom crate registries.
--ignore-plugins [boolean]                                   Set this to `true` if `allowPlugins=true` but you wish to skip running plugins when updating lock files.
--ignore-scripts [boolean]                                   Set this to `false` if `allowScripts=true` and you wish to run scripts when updating lock files.
--platform <string>                                          Platform type of repository.
--endpoint <string>                                          Custom endpoint to use.
--token <string>                                             Repository Auth Token.
--username <string>                                          Username for authentication.
--password <string>                                          Password for authentication.
--npmrc <string>                                             String copy of `.npmrc` file. Use `\n` instead of line breaks.
--npmrc-merge [boolean]                                      Whether to merge `config.npmrc` with repo `.npmrc` content if both are found.
--npm-token <string>                                         npm token used to authenticate with the default registry.
--update-lock-files [boolean]                                Set to `false` to disable lock file updating.
--skip-installs [boolean]                                    Skip installing modules/dependencies if lock file updating is possible without a full install.
--autodiscover [boolean]                                     Autodiscover all repositories.
--autodiscover-filter <array>                                Filter the list of autodiscovered repositories.
--autodiscover-namespaces <array>                            Filter the list of autodiscovered repositories by namespaces.
--autodiscover-projects <array>                              Filter the list of autodiscovered repositories by project names.
--autodiscover-topics <array>                                Filter the list of autodiscovered repositories by topics.
--pr-commits-per-run-limit <integer>                         Set the maximum number of commits per Renovate run. By default there is no limit.
--use-base-branch-config <string>                            Whether to read configuration from `baseBranches` instead of only the default branch.
--git-author <string>                                        Author to use for Git commits. Must conform to [RFC5322](https://datatracker.ietf.org/doc/html/rfc5322).
--git-ignored-authors <array>                                Git authors which are ignored by Renovate. Must conform to [RFC5322](https://datatracker.ietf.org/doc/html/rfc5322).
--git-timeout <integer>                                      Configure the timeout with a number of milliseconds to wait for a Git task.
--enabled-managers <array>                                   A list of package managers to enable. Only managers on the list are enabled.
--include-paths <array>                                      Include package files only within these defined paths.
--ignore-paths <array>                                       Skip any package file whose path matches one of these. Can be a string or glob pattern.
--exclude-commit-paths <array>                               A file matching any of these glob patterns will not be committed, even if the file has been updated.
--execution-timeout <integer>                                Default execution timeout in minutes for child processes Renovate creates.
--registry-aliases <object>                                  Aliases for registries.
--azure-work-item-id <integer>                               The id of an existing work item on Azure Boards to link to each PR.
--auto-approve [boolean]                                     Set to `true` to automatically approve PRs.
--ignore-deps <array>                                        Dependencies to ignore.
--update-internal-deps [boolean]                             Whether to update internal dep versions in a monorepo. Works on Yarn Workspaces.
--package-rules <array>                                      Rules for matching packages.
--auto-replace-global-match [boolean]                        Control whether replacement regular expressions are global matches or only the first match.
--pin-digests [boolean]                                      Whether to add digests to Dockerfile source images.
--separate-major-minor [boolean]                             If set to `false`, Renovate will upgrade dependencies to their latest release only. Renovate will not separate major or minor branches.
--separate-multiple-major [boolean]                          If set to `true`, PRs will be raised separately for each available `major` upgrade version.
--separate-multiple-minor [boolean]                          If set to `true`, Renovate creates separate PRs for each `minor` stream.
--separate-minor-patch [boolean]                             If set to `true`, Renovate will separate `minor` and `patch` updates into separate branches.
--ignore-unstable [boolean]                                  Ignore versions with unstable SemVer.
--ignore-deprecated [boolean]                                Avoid upgrading from a non-deprecated version to a deprecated one.
--respect-latest [boolean]                                   Ignore versions newer than npm "latest" version.
--branch-prefix <string>                                     Prefix to use for all branch names.
--branch-prefix-old <string>                                 Old branchPrefix value to check for existing PRs.
--bump-version <string>                                      Bump the version in the package file being updated.
--semantic-commits <string>                                  Enable Semantic Commit prefixes for commits and PR titles.
--semantic-commit-type <string>                              Commit type to use if Semantic Commits is enabled.
--semantic-commit-scope <string>                             Commit scope to use if Semantic Commits are enabled.
--commit-message-lower-case <string>                         Lowercase PR- and commit titles.
--keep-updated-label <string>                                If set, users can add this label to PRs to request they be kept updated with the base branch.
--rollback-prs [boolean]                                     Create PRs to roll back versions if the current version is not found in the registry.
--recreate-when <string>                                     Recreate PRs even if same ones were closed previously.
--rebase-when <string>                                       Controls when Renovate rebases an existing branch.
--rebase-label <string>                                      Label to request a rebase from Renovate bot.
--stop-updating-label <string>                               Label to make Renovate stop updating a PR.
--minimum-release-age <string>                               Time required before a new release is considered stable.
--internal-checks-as-success [boolean]                       Whether to consider passing internal checks such as `minimumReleaseAge` when determining branch status.
--internal-checks-filter <string>                            When and how to filter based on internal checks.
--pr-creation <string>                                       When to create the PR for a branch.
--pr-not-pending-hours <integer>                             Timeout in hours for when `prCreation=not-pending`.
--pr-hourly-limit <integer>                                  Rate limit PRs to maximum x created per hour. 0 means no limit.
--pr-concurrent-limit <integer>                              Limit to a maximum of x concurrent branches/PRs. 0 means no limit.
--branch-concurrent-limit <integer>                          Limit to a maximum of x concurrent branches. 0 means no limit, `null` (default) inherits value from `prConcurrentLimit`.
--bb-use-default-reviewers [boolean]                         Use the default reviewers (Bitbucket only).
--bb-use-development-branch [boolean]                        Use the repository's [development branch](https://support.atlassian.com/bitbucket-cloud/docs/branch-a-repository/#The-branching-model) as the
                                                           repository's default branch.
--automerge [boolean]                                        Whether to automerge branches/PRs automatically, without human intervention.
--automerge-type <string>                                    How to automerge, if enabled.
--automerge-strategy <string>                                The merge strategy to use when automerging PRs. Used only if `automergeType=pr`.
--automerge-comment <string>                                 PR comment to add to trigger automerge. Only used if `automergeType=pr-comment`.
--ignore-tests [boolean]                                     Set to `true` to enable automerging without tests.
--transform-templates <array>                                List of jsonata transformation rules.
--transitive-remediation [boolean]                           Enable remediation of transitive dependencies.
--osv-vulnerability-alerts [boolean]                         Use vulnerability alerts from `osv.dev`.
--prune-branch-after-automerge [boolean]                     Set to `true` to enable branch pruning after automerging.
--commit-body-table [boolean]                                If enabled, append a table in the commit message body describing all updates in the commit.
--pr-header <string>                                         Text added here will be placed first in the PR body.
--pr-footer <string>                                         Text added here will be placed last in the PR body, with a divider separator before it.
--customize-dashboard <object>                               Customize sections in the Dependency Dashboard issue.
--group-name <string>                                        Human understandable name for the dependency group.
--labels <array>                                             Labels to set in Pull Request.
--add-labels <array>                                         Labels to add to Pull Request.
--assignees <array>                                          Assignees for Pull Request (either username or email address depending on the platform).
--assignees-from-code-owners [boolean]                       Determine assignees based on configured code owners and changes in PR.
--expand-code-owners-groups [boolean]                        Expand the configured code owner groups into a full list of group members.
--assignees-sample-size <integer>                            Take a random sample of given size from `assignees`.
--assign-automerge [boolean]                                 Assign reviewers and assignees even if the PR is to be automerged.
--ignore-reviewers <array>                                   Reviewers to be ignored in PR reviewers presence (either username or email address depending on the platform).
--reviewers <array>                                          Requested reviewers for Pull Requests (either username or email address depending on the platform).
--reviewers-from-code-owners [boolean]                       Determine reviewers based on configured code owners and changes in PR.
--filter-unavailable-users [boolean]                         Filter reviewers and assignees based on their availability.
--fork-mode-disallow-maintainer-edits [boolean]              Disallow maintainers to push to Renovate pull requests when running in fork mode.
--confidential [boolean]                                     If enabled, issues created by Renovate are set as confidential.
--reviewers-sample-size <integer>                            Take a random sample of given size from `reviewers`.
--additional-reviewers <array>                               Additional reviewers for Pull Requests (in contrast to `reviewers`, this option adds to the existing reviewer list, rather than replacing it).
--host-rules <array>                                         Host rules/configuration including credentials.
--cache-hard-ttl-minutes <integer>                           Maximum duration in minutes to keep datasource cache entries.
--cache-ttl-override <object>                                An object that contains cache namespace TTL override values.
--pr-body-definitions <object>                               Table column definitions to use in PR tables.
--pr-body-columns <array>                                    List of columns to use in PR bodies.
--pr-body-notes <array>                                      List of extra notes or templates to include in the Pull Request body.
--prune-stale-branches [boolean]                             Set to `false` to disable pruning stale branches.
--unicode-emoji [boolean]                                    Enable or disable Unicode emoji.
--git-lab-ignore-approvals [boolean]                         Ignore approval rules for MRs created by Renovate, which is useful for automerge.
--custom-managers <array>                                    Custom managers using regex matching.
--clone-submodules [boolean]                                 Set to `true` to initialize submodules during repository clone.
--ignore-pr-author [boolean]                                 Set to `true` to fetch the entire list of PRs instead of only those authored by the Renovate user.
--git-no-verify <array>                                      Which Git commands will be run with the `--no-verify` option.
--update-pinned-dependencies [boolean]                       Whether to update pinned (single version) dependencies or not.
--git-url <string>                                           Overrides the default resolution for Git remote, e.g. to switch GitLab from HTTPS to SSH-based.
--write-discovered-repos <string>                            Writes discovered repositories to a JSON file and then exit.
--platform-automerge [boolean]                               Controls if platform-native auto-merge is used.
--user-strings <object>                                      User-facing strings for the Renovate comment when a PR is closed.
--platform-commit [boolean]                                  Use platform API to perform commits instead of using Git directly.
--branch-name-strict [boolean]                               Whether to be strict about the use of special characters within the branch name.
--checked-branches <array>                                   A list of branch names to mark for creation or rebasing as if it was selected in the Dependency Dashboard issue.
--milestone <integer>                                        The number of a milestone. If set, the milestone will be set when Renovate creates the PR.
--http-cache-ttl-days <integer>                              Maximum duration in days to keep HTTP cache entries.
--cache-private-packages [boolean]                           Cache private packages in the datasource cache. This is useful for self-hosted setups


## Reference

