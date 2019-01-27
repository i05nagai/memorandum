---
title: spin
---

## spin

## Install

For OSX,

```
curl -LO https://storage.googleapis.com/spinnaker-artifacts/spin/$(curl -s https://storage.googleapis.com/spinnaker-artifacts/spin/latest)/darwin/amd64/spin
chmod +x spin
sudo mv spin /usr/local/bin/spin
# or
go get github.com/spinnaker/spin
```

## CLI

* --config string
    * path to config file
    * default `$HOME/.spin/config`
* --gate-endpoint string
    * Gate (API server) endpoint
    * default `http://localhost:8084`
* -h, --help
    * help for this command
* -k, --insecure
    * ignore certificate errors
* --no-color
    * disable color (default true)
* --output string
    * configure output formatting
* -q, --quiet
    * squelch non-essential output
* --version
    * version for this command

```
spin application
```

* delete
    * Delete the specified application
* get
    * Get the specified application
* list
    * List the all applications
* save
    * Save the provided application

```
spin pipeline
```


* delete
    * Delete the provided pipeline
* execute
    * Execute the provided pipeline
* get
    * Get the pipeline with the provided name from the provided application
* list
    * List the pipelines for the provided application
* save
    * Save the provided pipeline

```
spin pipeline-template
```

* delete
    * Delete the provided pipeline template
* get
    * Get the pipeline template with the provided id
* list
    * List the pipeline templates for the provided scopes
* plan
    * Plan the provided pipeline template config
* save
    * Save the provided pipeline

```
spin help
```

## Usage

```
spin application save \
    --application-name my-app \
    --owner-email someone@example.com \
    --cloud-providers "gce, kubernetes"
```

Create pipeline

```
spin pipeline save --file <path to pipeline json>
```

Execute pipeline

```
spin pipeline execute --name my-pipeline --application my-app
```

Create and update pipeline template

```
spin pipeline-templates save --file <path to pipeline json>
```

Visualize template

```
spin pipeline-templates plan --config <path to template config>
```

## Reference
* [Install and Configure Spin CLI \- Spinnaker](https://www.spinnaker.io/guides/spin/cli/)
* [Manage Applications \- Spinnaker](https://www.spinnaker.io/guides/spin/app/)
