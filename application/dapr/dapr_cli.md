---
title: dapr CLI
---

## dapr CLI

- annotate
    - Add dapr annotations to a Kubernetes configuration.
    - Supported platforms: Kubernetes
- build-info
    - Print build info of Dapr CLI and runtime
- completion
    - Generates shell completion scripts
- components
    - List all Dapr components. Supported platforms: Kubernetes
- configurations
    - List all Dapr configurations. Supported platforms: Kubernetes
- dashboard
    - Start Dapr dashboard. Supported platforms: Kubernetes and self-hosted
- help
    - Help about any command
- init
    - Install Dapr on supported hosting platforms. Supported platforms: Kubernetes and self-hosted
- invoke
    - Invoke a method on a given Dapr application. Supported platforms: Self-hosted
- list
    - List all Dapr instances. Supported platforms: Kubernetes and self-hosted
- logs
    - Get Dapr sidecar logs for an application. Supported platforms: Kubernetes
- mtls
    - Check if mTLS is enabled. Supported platforms: Kubernetes
- publish
    - Publish a pub-sub event. Supported platforms: Self-hosted
- run
    - Run Dapr and (optionally) your application side by side. Supported platforms: Self-hosted
- status
    - Show the health status of Dapr services. Supported platforms: Kubernetes
- stop
    - Stop Dapr instances and their associated apps. Supported platforms: Self-hosted
- uninstall
    - Uninstall Dapr runtime. Supported platforms: Kubernetes and self-hosted
- upgrade
    - Upgrades or downgrades a Dapr control plane installation in a cluster. Supported platforms: Kubernetes

```
dapr init
```

- Dapr runtime installed to `$HOME/.dapr/bin`



## Reference
- https://docs.dapr.io/getting-started/install-dapr-cli/
