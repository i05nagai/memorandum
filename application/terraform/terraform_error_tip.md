---
title: Terraform Error Tip
---

## Terraform Error Tip


### terraform init with backend
Error messsage is like below.

```
Initializing the backend...
Error loading backend config: 1 error(s) occurred:

* terraform.backend: configuration cannot contain interpolations

The backend configuration is loaded by Terraform extremely early, before
the core of Terraform can be initialized. This is necessary because the backend
dictates the behavior of that core. The core is what handles interpolation
processing. Because of this, interpolations cannot be used in backend
configuration.

If you'd like to parameterize backend configuration, we recommend using
partial configuration with the "-backend-config" flag to "terraform init".
```

Your initial configuration failed.
Thus, you need to disable backends to see actual error.

```
terraform init -backend=false
```

Delete `.terraform` directory to initialize incomplete states.

### netrpc
以下のようなerrorが出たらterraformのversionをあげる。
providerが古いterraformに対応していない可能生がある。
それかproviderのversionを指定する。

```
provider.terraform: dial unix ....|netrpc: connect: no such file or directory
```


## Reference
