---
title: Github Actions
---

## Github Actions


## Workflows
- https://github.com/peter-evans/slash-command-dispatch
- https://docs.prow.k8s.io/docs/components/plugins/approve/approvers/

## cahce
https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/caching-dependencies-to-speed-up-workflows#usage-limits-and-eviction-policy

limitations

- GitHub will remove any cache entries that have not been accessed in over 7 days.
- There is no limit on the number of caches you can store, but the total size of all caches in a repository is limited to 10 GB.
- Once a repository has reached its maximum cache storage, the cache eviction policy will create space by deleting the oldest caches in the repository.


## Self hosetd runner
https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners

- Repository-level runners are dedicated to a single repository.
- Organization-level runners can process jobs for multiple repositories in an organization.
- Enterprise-level runners can be assigned to multiple organizations in an enterprise account.

- A self-hosted runner is automatically removed from GitHub if it has not connected to GitHub Actions for more than 14 days.
- An ephemeral self-hosted runner is automatically removed from GitHub if it has not connected to GitHub Actions for more than 1 day.

## Reference
