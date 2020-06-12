---
title: Jenkins Plugin
---

## Jenkins Plugin

## Docker
- [Jenkins Plugins](https://plugins.jenkins.io/docker-plugin)
- [Docker Plugin \- Jenkins \- Jenkins Wiki](https://wiki.jenkins.io/display/JENKINS/Docker+Plugin)


## Slack
- https://github.com/jenkinsci/slack-plugin

```groovy
// notify message to all commiters
args.put('notifyCommitters', true)
args.put('botUser', true)
slackSend(args)
```

## Bitbucket
- [jenkinsci/stashnotifier\-plugin: A Jenkins Plugin to notify Atlassian Stash\|Bitbucket of build results](https://github.com/jenkinsci/stashnotifier-plugin)

```
def notifyBitbucket(String state) {
    notifyBitbucket(
            commitSha1: 'commit',
            credentialsId: '00000000-1111-2222-3333-123456789abc',
            disableInprogressNotification: false,
            considerUnstableAsSuccess: true,
            ignoreUnverifiedSSLPeer: true,
            buildStatus: state,
            buildName: 'Performance Testing',
            includeBuildNumberInKey: false,
            prependParentProjectKey: false,
            projectKey: '',
            stashServerBaseUrl: 'https://my.company.intranet/bitbucket')

}
```

## Artifactory plugin
- [Declarative Pipeline Syntax \- JFrog Artifactory \- JFrog Wiki](https://www.jfrog.com/confluence/display/RTF/Declarative+Pipeline+Syntax)
- [jfrog/jenkins\-artifactory\-plugin: Jenkins artifactory plugin](https://github.com/jfrog/jenkins-artifactory-plugin)
- [Using File Specs \- JFrog Artifactory \- JFrog Wiki](https://www.jfrog.com/confluence/display/RTF/Using+File+Specs)
    - file  spec  schema

Uploading schema

- target
    - Specifies the target path in Artifactory in the following format: `[repository_name]/[repository_path]`
    - You can find it `repositor_name` in Artfactory GUI as Name
    - You can find it `repository_path` in Artfactory GUI as repository path


## Kubernetes plugin
- [jenkinsci/kubernetes\-plugin: Jenkins plugin to run dynamic agents in a Kubernetes/Docker environment](https://github.com/jenkinsci/kubernetes-plugin)

## code-coverage-api
- [Code Coverage API \| Jenkins plugin](https://plugins.jenkins.io/code-coverage-api/)
- [Code Coverage API Plugin](https://jenkins.io/doc/pipeline/steps/code-coverage-api/)

- merge

## cobertura
- [Cobertura \| Jenkins plugin](https://plugins.jenkins.io/cobertura/)
- [Cobertura Plugin](https://jenkins.io/doc/pipeline/steps/cobertura/)


## job dsl
- [Job DSL \| Jenkins plugin](https://plugins.jenkins.io/job-dsl/)

You ca generate pipeline job from groovy scrips.

```
job('z-emr-job-generate-job') {
    steps {
        dsl {
            external("jobdsls/*.groovy")
            removeAction("DELETE")
        }
    }
}
```

If you geenrate job from dsl, you'll see the following error.

- [seed job asks for script approval in jenkins \- Stack Overflow](https://stackoverflow.com/questions/43699190/seed-job-asks-for-script-approval-in-jenkins)
- [ERROR: script not yet approved for use · Issue \#1 · robinbowes/jenkins\-job\-dsl\-seed\-all\-demo](https://github.com/robinbowes/jenkins-job-dsl-seed-all-demo/issues/1)
- [Script Security · jenkinsci/job\-dsl\-plugin Wiki](https://github.com/jenkinsci/job-dsl-plugin/wiki/Script-Security)
- [jenkins\-bootstrap\-shared/configure\-job\-dsl\-security\.groovy at master · samrocketman/jenkins\-bootstrap\-shared](https://github.com/samrocketman/jenkins-bootstrap-shared/blob/master/scripts/configure-job-dsl-security.groovy)


#### Suppress automatic build
- [2git/Jenkinsfile\.dsl at master · Praqma/2git](https://github.com/Praqma/2git/blob/master/Jenkinsfile.dsl)
    - suppress automatic SCM build
- [job\-dsl\-plugin/job\-dsl\-core/src/main/groovy/javaposse/jobdsl/dsl/helpers/workflow at master · jenkinsci/job\-dsl\-plugin](https://github.com/jenkinsci/job-dsl-plugin/tree/master/job-dsl-core/src/main/groovy/javaposse/jobdsl/dsl/helpers/workflow)
- [Jenkins Job DSL for a Multi\-Branch Pipeline that includes Branch Source Strategy & custom Jenkinsfile script path](https://gist.github.com/djfdyuruiry/e3c891c6204bea602e770f9bf7a0cb1c)


#### AuthorizationMatrix
- [Jenkins DSL Authorization Matrix loop \| Virtualizatio'n'automation](https://emilwypych.com/2018/06/27/jenkins-dsl-authorization-matrix-loop/?cn-reloaded=1)

In Jenkinsfile, you can write in options section.

```
    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
        authorizationMatrix(permissions:[
            // for all logined users
            "hudson.model.Item.Build:authenticated",
            "hudson.model.Item.Cancel:authenticated",
            // for all user
            // "hudson.model.Item.Build:anonymous",
            // "hudson.model.Item.Cancel:anonymous"
        ])
        timestamps()
    }
```

## pipeline-utility-stesp
- [pipeline\-utility\-steps\-plugin/STEPS\.md at master · jenkinsci/pipeline\-utility\-steps\-plugin](https://github.com/jenkinsci/pipeline-utility-steps-plugin/blob/master/docs/STEPS.md)


```
findFiles(glob: "path/to/*/file").each { path -> 
    echo(path.getName()) // filename
    echo(path.getPath()) // filepath
}
```

## Reference

