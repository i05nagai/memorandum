---
title: DataDog Kubernetes
---

## DataDog Kubernetes
There are two types of metrics.
DataDog can collect metrics from `kube-state-metrics`.

## Setup
* [charts/stable/datadog at master · kubernetes/charts](https://github.com/kubernetes/charts/tree/master/stable/datadog)
* https://docs.datadoghq.com/agent/kubernetes/daemonset_setup/#configure-rbac-permissions
* https://github.com/DataDog/datadog-agent

You should check the latest manifests in the Github repository.
Some manifests only works on older version of Docker image of datadog agetn.

#### Prerequiresite
Create service accounts and cluster role bindings
https://docs.datadoghq.com/agent/kubernetes/
Your account requires permissions:

* `container.clusterRoleBindings.create`
* `container.clusterRoles.create`

##### Custom metrics
[Custom Metrics](https://docs.datadoghq.com/getting_started/custom_metrics/)

To send custom metrics, you need to open a port.

```
        ports:
          - containerPort: 8125
            hostPort: 8125
            name: dogstatsdport
            protocol: UDP
```


## Metrics
* [Kubernetes](https://docs.datadoghq.com/integrations/kubernetes/)

datadogがkubernetesから取得できるMetricsの一覧は上にある通り。
`Kubernetes State`とついているものは、`kube-state-metrics`のdeployが必要。

### Log correction
envで `DD_LOGS_ENABLED`をtrueにする。

```
- name: DD_LOGS_ENABLED
    value: "true"
```

```
    (...)
      volumeMounts:
        (...)
        - name: pointerdir
            mountPath: /opt/datadog-agent/run
    (...)
    volumes:
      (...)
      - hostPath:
            path: /opt/datadog-agent/run
          name: pointerdir
    (...)
```

### Event collections
kubenertes API serverのeventをとれる。
取得できるeventの一覧は以下の通り。

## Tips

Add `Kubernetes Engine Developer` or `Kubnernetes Engine Admin`

```
Error from server (Forbidden): error when creating "rbac-datadog.yml": clusterrolebindings.rbac.authorization.k8s.io is forbidden: User "..." cannot create clusterrolebindings.rbac.authorization.k8s.io at the cluster scope: Required "container.clusterRoleBindings.create" permission.
Error from server (Forbidden): error when creating "rbac-datadog.yml": clusterroles.rbac.authorization.k8s.io is forbidden: User "" cannot create clusterroles.rbac.authorization.k8s.io at the cluster scope: Required "container.clusterRoles.create" permission.
```

## Reference
* [Kubernetes](https://docs.datadoghq.com/agent/basic_agent_usage/kubernetes/)
