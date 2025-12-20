---
title: kustomize
---

## kustomize
Kustomize traverses a Kubernetes manifest to add, remove or update configuration options without forking

## Install
It is avaialble with kubectl.
You do not install kustomize explictly.

```
brew install kustomize
```

## Example
https://github.com/kubernetes-sigs/kustomize/tree/master/examples

## Configuration
https://kubectl.docs.kubernetes.io/references/kustomize/glossary/#kustomization

`kustomization.yaml`

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
- {pathOrUrl}
- ...

generators:
- {pathOrUrl}
- ...

transformers:
- {pathOrUrl}
- ...

validators:
- {pathOrUrl}
- ...

# convienience fields
# All the other fields in a kustomization file (configMapGenerator, namePrefix, patches, etc.) are conveniences as well, as they are shorthand for
# run a particular generator or transformer with a particular configuration.
commonLabels:
```

## Property
https://github.com/kubernetes-sigs/kustomize/blob/master/examples/combineConfigs.md
- Common properties
- Plumbing properties


## Directory structures

```
├── base
│   ├── deployment.yaml
│   ├── kustomization.yaml
│   └── service.yaml
└── overlays
    ├── dev
    │   ├── kustomization.yaml
    │   └── patch.yaml
    ├── prod
    │   ├── kustomization.yaml
    │   └── patch.yaml
    └── staging
        ├── kustomization.yaml
        └── patch.yaml
```


## CLI

```
kubectl kustomize DIR [flags] [options]

# Build the current working directory
kubectl kustomize

# Build some shared configuration directory
kubectl kustomize /home/config/production

# Build from github
kubectl kustomize https://github.com/kubernetes-sigs/kustomize.git/examples/helloWorld?ref=v1.0.6
```


- `--as-current-user=false`
    - use the uid and gid of the command executor to run the function in the container
- `--enable-alpha-plugins=false`
    - enable kustomize plugins
- `--enable-helm=false`
    - Enable use of the Helm chart inflator generator.
- `-e, --env=[]`
    - a list of environment variables to be used by functions
- `--helm-api-versions=[]`
    - Kubernetes api versions used by Helm for Capabilities.APIVersions
- `--helm-command='helm'`
    - helm command (path to executable)
- `--helm-kube-version=''`
    - Kubernetes version used by Helm for Capabilities.KubeVersion
- `--load-restrictor='LoadRestrictionsRootOnly'`
    - if set to 'LoadRestrictionsNone', local kustomizations may load files from outside their root. This does, however, break the relocatability of the kustomization.
- `--mount=[]`
    - - a list of storage options read from the filesystem
- `--network=false`
    - enable network access for functions that declare it
- `--network-name='bridge'`
    - the docker network to run the container in
- `-o, --output=''`
    - If specified, write output to this path.


## Reference
- https://kustomize.io/
