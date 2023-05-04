---
title: Strategic Merge Patch
---

## Strategic Merge Patch


## operations

replace


```yaml
$patch: replace  # recursive and applies to all fields of the map it's in
containers:
- name: nginx
  image: nginx-1.0
```

```yaml
containers:
  - name: nginx
    image: nginx-1.0
  - $patch: replace   # any further $patch operations nested in this list will be ignored
```

merge

delete

```yaml
containers:
  - name: nginx
    image: nginx-1.0
  - $patch: delete
    name: log-tailer  # merge key and value goes here
```

```

```

delete from primitive list


## Reference
- https://github.com/kubernetes/community/blob/master/contributors/devel/sig-api-machinery/strategic-merge-patch.md
