---
title: firebase CLI
---

## firebase CLI

## Install

```
npm install firebase
```


#### init

```
firebase init [feature]
```

- database
- emulators
- extensions
- firestore
- functions
- hosting
- hosting:github
- remoteconfig
- storage

#### login/logout

log the CLI into Firebase

```
login [options]
```

authorize the CLI for an additional account

```
login:add [options] [email]
```

generate an access token for use in non-interactive environments

```
login:ci [options]
```

list authorized CLI accounts

```
login:list
```

set the default account to use for this project directory or the global default account if not in a Firebase project directory

```
login:use <email>
```


```
logout [email]                                                 log the CLI out of Firebase
```

#### open

quickly open a browser to relevant project resources

```
open [link]
```

#### projects
add Firebase resources to a Google Cloud Platform project

```
projects:addfirebase [projectId]
```

creates a new Google Cloud Platform project, then adds Firebase resources to the project

```
projects:create [options] [projectId]

```

list all Firebase projects you have access to

```
projects:list
```

#### remoteconfig

get a Firebase project's Remote Config template

```
remoteconfig:get [options]
```

roll back a project's published Remote Config template to the one specified by the provided version number

```
remoteconfig:rollback [options]
```

get a list of Remote Config template versions that have been published for a Firebase project

```
remoteconfig:versions:list [options]
```

#### serve

start a local server for your static assets

```
serve [options]
```

#### setup

downloads the [service] emulator

```
setup:emulators:[service]
```

- database
- firestore
- pubsub
- storage
- ui


#### target

display configured deploy targets for the current project

```
target [type]

```

apply a deploy target to a resource

```
target:apply <type> <name> <resources...>
```

clear all resources from a named resource target

```
target:clear <type> <target>
```

remove a resource target

```
target:remove <type> <resource>
```

#### use

set an active Firebase project for your working directory

```
use [options] [alias_or_project_id]
```


## Reference
