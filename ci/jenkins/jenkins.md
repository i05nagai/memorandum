---
title: Jenkins
---

## Jenkins


## Configuration

- `triggers`
    - `cron`
    - `pollSCM`
        - check source code change by specified interval
    - `upstream`
        - when specified jobs is finished with specified thresholds, the job will be triggered
- `stages`
    - place
        - inside of `stage`
- `tools`
    - place
        - incide of `pipeline`
        - `stage`
    - `maven`
    - `jdk`
    - `gradle`
- `input`
    - `message`
    - `id`
    - `ok`
    - `submitter`
    - `submitterParameter`
    - `parameters`
- `when`
    - place
        - inside of `stage`
    - `branch`
    - `buildingTag`
    - `changelog`
    - `changeset`
    - `changeRequest`
    - `environment`
    - `equals`
    - `expression`
    - `tag`
    - `not`
    - `allOf`
    - `anyOf`
    - `triggeredBy`

## Reference
