---
title: bec
---

## bec


## Duplication
```
pr-restrictions:
  required-approvers: 2
  required-successful-builds: 1
```

are the same as below.

```
hooks:
  - enabled: true
    key: com.atlassian.bitbucket.server.bitbucket-bundled-hooks:requiredApproversMergeHook
    settings:
      requiredCount: "2"
  - enabled: false
    key: com.atlassian.bitbucket.server.bitbucket-build:requiredBuildsMergeCheck
    settings:
      requiredCount: "1"
```

You can use only `pr-restrictions`.
Both fields are mandatory in `pr-restrctions` and configuration in hooks show diff if there is discrepancy between pr-restrictions and hooks.


## Error

#### Error1

```
escript: exception error: no match of right hand side value {error,
                                                    [<<"Url field is blank, please supply one.">>]}
```

You may need to remove below configuration in hooks.

```
- enabled: false
  key: de.aeffle.stash.plugin.stash-http-get-post-receive-hook:http-get-post-receive-hook
  settings: {}
```




## Reference
