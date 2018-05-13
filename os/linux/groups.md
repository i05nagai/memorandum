---
title: groups
---

## groups
`/etc/group`にgroupの一覧

## CLI


## Usage
userの所属するgroup

```
groups USERNAME
```

groupに所属するuserの一覧

```
getent group GROUPNAME
getent group groupname | awk -F: '{print $4}'
```

## Reference
