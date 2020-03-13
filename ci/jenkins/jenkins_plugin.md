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

## Reference
