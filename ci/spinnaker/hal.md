---
title: hal
---

## hal

#### use with Docker

```
docker run -p 8084:8084 -p 9000:9000 \
    --name halyard --rm \
    -v ~/.hal:/home/spinnaker/.hal \
    -it \
    gcr.io/spinnaker-marketplace/halyard:stable
```

## Install
OSX

```
curl -O https://raw.githubusercontent.com/spinnaker/halyard/master/install/debian/InstallHalyard.sh
bash InstallHalyard.sh
```

## Usage

```
hal config provider kubernetes account add prod-demo \
  --context $PROD_CONTEXT \
  --provider-version v2
```

This command automatically forwards ports 9000 (Deck UI) and 8084 (Gate API service).

```
hal deploy connect
```

## CLI

```
hal <subcommad> <global-option>
```

* --daemon-endpoint
    * If supplied, connect to the daemon at this address.
* --options
    * Get options for the specified field name.
* -a, --alpha
    * Enable alpha halyard features.
* -c, --color
    * Enable terminal color output.
* -d, --debug
    * Show detailed network traffic with halyard daemon.
* -h, --help=false
    * Display help text about this command.
* -l, --log
    * Set the log level of the CLI.
* -o, --output
    * Format the CLIs output.
* -q, --quiet
    * Show no task information or messages. When set, ANSI formatting will be disabled, and all prompts will be accepted.


#### hal admin
This is meant for users building and publishing their own Spinnaker images and config.

```
hal admin
```

#### hal backup
Backup and restore (remote or local) copies of your halconfig and all required files.

```
hal backup
```

#### hal config
Configure, validate, and view your halconfig.

```
hal config
```


#### hal deploy
Manage the deployment of Spinnaker. This includes where it's deployed, what the infrastructure footprint looks like, what the currently running deployment looks like, etc...

```
hal deploy apply
```


```
hal deploy apply
```

#### hal shutdown

Shutdown the halyard daemon.

```
shutdown
```

#### hal spin
Manage the lifecycle of spin CLI.

```
hal spin
```

#### hal task
This set of commands exposes utilities of dealing with Halyard's task engine.

```
task
```

#### hal version
Get information about the available Spinnaker versions.

```
version
```

## Others
[halyard/homebrew\-casks: Casks for OSX applications](https://github.com/halyard/homebrew-casks)

```
# with homebrew
brew tap halyard/homebrew-casks
brew cask install halyard
```

## Reference
* [Commands \- Spinnaker](https://www.spinnaker.io/reference/halyard/commands/)
