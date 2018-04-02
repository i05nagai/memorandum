---
title: DataDog
---

## DataDog

## Docker image
* [datadog-agent/Dockerfiles/agent at master · DataDog/datadog-agent](https://github.com/DataDog/datadog-agent/tree/master/Dockerfiles/agent)
* [datadog/docker-dd-agent - Docker Hub](https://hub.docker.com/r/datadog/docker-dd-agent/)

## Autodiscovery
* [Using Autodiscovery with Kubernetes and Docker](https://docs.datadoghq.com/agent/autodiscovery/)

## Kubernetes
* [charts/stable/datadog at master · kubernetes/charts](https://github.com/kubernetes/charts/tree/master/stable/datadog)

kubernetes用のmanifestが提供されている。
また、Helm chartもある。

```yaml
apiVersion: extensions/v1beta1
kind: DaemonSet
metadata:
  name: datadog-agent
spec:
  template:
    metadata:
      labels:
        app: datadog-agent
      name: datadog-agent
    spec:
      containers:
      - image: datadog/agent:latest
        imagePullPolicy: Always
        name: datadog-agent
        ports:
          - containerPort: 8125
            name: dogstatsdport
            protocol: UDP
        env:
          - name: DD_API_KEY
            value: 
          - name: KUBERNETES
            value: "yes"
          - name: DD_KUBERNETES_KUBELET_HOST
            valueFrom:
              fieldRef:
                fieldPath: status.hostIP
        resources:
          requests:
            memory: "128Mi"
            cpu: "100m"
          limits:
            memory: "512Mi"
            cpu: "250m"
        volumeMounts:
          - name: dockersocket
            mountPath: /var/run/docker.sock
          - name: procdir
            mountPath: /host/proc
            readOnly: true
          - name: cgroups
            mountPath: /host/sys/fs/cgroup
            readOnly: true
        livenessProbe:
          exec:
            command:
            - ./probe.sh
          initialDelaySeconds: 15
          periodSeconds: 5
      volumes:
        - hostPath:
            path: /var/run/docker.sock
          name: dockersocket
        - hostPath:
            path: /proc
          name: procdir
        - hostPath:
            path: /sys/fs/cgroup
          name: cgroups
```

Custom metricsを送る場合は、hostのPortをあける。
[Custom Metrics](https://docs.datadoghq.com/getting_started/custom_metrics/)

```
        ports:
          - containerPort: 8125
            hostPort: 8125
            name: dogstatsdport
            protocol: UDP
```

## Reference
* [How to monitor Google Kubernetes Engine with Datadog](https://www.datadoghq.com/blog/monitor-google-kubernetes-engine/)
