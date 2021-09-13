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

## CLI
- [Quick Start Guide — jenkins\-job\-builder 3\.2\.1\.dev2 documentation](https://docs.openstack.org/infra/jenkins-job-builder/quick-start.html)

There is a CLI command in Jenkins.


## Parametrized build

#### Parameter is no loaded before the first build
- [JENKINS41929 Offer Build with Parameters on first build when declarative Jenkinsfile found - Jenkins JIRA](https://issues.jenkins-ci.org/browse/JENKINS-41929)

If you use `suppress automatic build`, jenkins doesn't recognize parameters.
Workaround is to skip the first build and to use it as a build to just load parameters.

```
            if (env.BUILD_NUMBER.equals("1")) {
                currentBuild.displayName = "Parameter loading build"
                currentBuild.result = 'ABORTED'
                currentBuild.description = 'Stopping initial build. The first build is used to load parameters.'
                error("Stopping initial build. The first build is used to load parameters.")
            }
```

## Prallel jobs

```
stage('Install') {
    steps {
        sh("do something")
        script {
            def parallel_jobs = [1, 2, 3].collectEntries { ent ->
                [ent, {
                    triggerRemoteJob(
                        remoteJenkinsName: "<jenkins-name>",
                        job: "<job-name>",
                        token: "<token>",
                        parameters: "commitHash=${env.GIT_COMMIT}\npath=/path/to/somewhere}",
                        blockBuildUntilComplete: true)
                }]
            }
            parallel(parallel_jobs)
        }
    }
}
```

## Steps
- https://www.jenkins.io/doc/pipeline/steps/


## Security
- [Securing Jenkins](https://www.jenkins.io/doc/book/system-administration/security/)
- [Managing Security](https://www.jenkins.io/doc/book/managing/security/)
- [Getting Started with Pipelines](https://www.jenkins.io/pipeline/getting-started-pipelines/)

## API

- `<server-url>/queue/api/json?pretty=true&depth=0`
    - get queue info
    - global 
- `<server-url>/view/all/job/<pipeline-name>/job/<branch-name>/2/api/json?pretty=true`
- `<server-url>/queue/item/%(number)d/api/json?depth=%(depth)s`
- `<server-url>/queue/item/%(number)d/api/json?depth=%(depth)s`
- `<server-url>/job/<job-name>/api/json?pretty=true`


## Credential
- [Using a Jenkinsfile](https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#handling-credentials)

```
withCredentials([usernamePassword(credentialsId: 'credential-id', usernameVariable: 'BITBUCKET_USER', passwordVariable: 'BITBUCKET_PASSWORD')]) {
    sh("git push https://${BITBUCKET_USER}:${BITBUCKET_PASSWORD}@bitbucket.com/path/to/repo.git ${branch}")
}
```

## Permissions

- com.cloudbees.plugins.credentials.CredentialsProvider.Create
- com.cloudbees.plugins.credentials.CredentialsProvider.Delete
- com.cloudbees.plugins.credentials.CredentialsProvider.ManageDomains
- com.cloudbees.plugins.credentials.CredentialsProvider.Update
- com.cloudbees.plugins.credentials.CredentialsProvider.View
- hudson.model.Item.Build
- hudson.model.Item.Build
- hudson.model.Item.Cancel
- hudson.model.Item.Configure
- hudson.model.Item.Delete
- hudson.model.Item.Discover
- hudson.model.Item.Move
- hudson.model.Item.Read
- hudson.model.Item.Workspace

## Reference
- [Jenkins Pipeline NotSerializableException: groovy\.json\.internal\.LazyMap \- Stack Overflow](https://stackoverflow.com/questions/37864542/jenkins-pipeline-notserializableexception-groovy-json-internal-lazymap/37897833#37897833)
