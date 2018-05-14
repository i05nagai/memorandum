---
title: Kontemplate
---

## Kontemplate

## Install
For OSX

```
brew tap tazjin/kontemplate https://github.com/tazjin/kontemplate
brew install kontemplate
```

## Usage

変数定義用のfileを作る。
`some-api.yaml`

```yaml
context: k8s.prod.mydomain.com
global:
  globalVar: lizards
include:
  - name: some-api
    values:
      version: 1.0-0e6884d
      importantFeature: true
      apiPort: 4567
```

* `context`
* `global`
    * `key: value`でglobalに使える変数名を定義
* `include`
    * `name`
        * kubernetesの`metadata.name`
    * `values`
        * `key: value`で変数を定義


```

```

## CLI


## Reference
* [tazjin/kontemplate: Extremely simple Kubernetes resource templates](https://github.com/tazjin/kontemplate)
