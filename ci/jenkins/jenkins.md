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

## Tips

#### Variable scope
- [jenkins \- Strange variable scoping behavior in Jenkinsfile \- Stack Overflow](https://stackoverflow.com/questions/50571316/strange-variable-scoping-behavior-in-jenkinsfile)

* variables defined with def in the main script body cannot be accessed from other methods.
* variables defined without def can be accessed directly by any method even from different scripts. It's a bad practice.
* variables defined with def and @Field annotation can be accessed directly from methods defined in the same script.


#### JSON string to objects
You need to use.

```
import groovy.json.JsonSlurperClassic
new groovy.json.JsonSlurperClassic().parseText(json)
```


## Reference
- [Jenkins Pipeline NotSerializableException: groovy\.json\.internal\.LazyMap \- Stack Overflow](https://stackoverflow.com/questions/37864542/jenkins-pipeline-notserializableexception-groovy-json-internal-lazymap/37897833#37897833)
