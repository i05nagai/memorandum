---
title: DataDog Kubernetes
---

## DataDog Kubernetes

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

* `collect_kubernetes_events`

## Reference
* [Kubernetes](https://docs.datadoghq.com/agent/basic_agent_usage/kubernetes/)
