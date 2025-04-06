---
title: github cli
---

## github cli

## Install

```
```

## auth

```
gh auth login
```

## repo

```
gh repo
```

create:      Create a new repository
list:        List repositories owned by user or organization
archive:     Archive a repository
clone:       Clone a repository locally
delete:      Delete a repository
deploy-key:  Manage deploy keys in a repository
edit:        Edit repository settings
fork:        Create a fork of a repository
rename:      Rename a repository
set-default: Configure default repository for this directory
sync:        Sync a repository
unarchive:   Unarchive a repository
view:        View a repository

```
gh repo list
      --archived            Show only archived repositories
      --fork                Show only forks
  -q, --jq expression       Filter JSON output using a jq expression
      --json fields         Output JSON with the specified fields
  -l, --language string     Filter by primary coding language
  -L, --limit int           Maximum number of repositories to list (default 30)
      --no-archived         Omit archived repositories
      --source              Show only non-forks
  -t, --template string     Format JSON output using a Go template; see "gh help formatting"
      --topic strings       Filter by topic
      --visibility string   Filter by repository visibility: {public|private|internal}
```

- assignableUsers
- codeOfConduct
- contactLinks
- createdAt
- defaultBranchRef
- deleteBranchOnMerge
- description
- diskUsage
- forkCount
- fundingLinks
- hasDiscussionsEnabled
- hasIssuesEnabled
- hasProjectsEnabled
- hasWikiEnabled
- homepageUrl
- id
- isArchived
- isBlankIssuesEnabled
- isEmpty
- isFork
- isInOrganization
- isMirror
- isPrivate
- isSecurityPolicyEnabled
- isTemplate
- isUserConfigurationRepository
- issueTemplates
- issues
- labels
- languages
- latestRelease
- licenseInfo
- mentionableUsers
- mergeCommitAllowed
- milestones
- mirrorUrl
- name
- nameWithOwner
- openGraphImageUrl
- owner
- parent
- primaryLanguage
- projects
- pullRequestTemplates
- pullRequests
- pushedAt
- rebaseMergeAllowed
- repositoryTopics
- securityPolicyUrl
- squashMergeAllowed
- sshUrl
- stargazerCount
- templateRepository
- updatedAt
- url
- usesCustomOpenGraphImage
- viewerCanAdminister
- viewerDefaultCommitEmail
- viewerDefaultMergeMethod
- viewerHasStarred
- viewerPermission
- viewerPossibleCommitEmails
- viewerSubscription
- visibility
- watchers

## Reference



IDsのdataが
