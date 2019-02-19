---
title: Heapster
---

## Heapster
Retired!

* For basic CPU/memory Horizontal Pods Autoscaler
* For general monitoring
    * Consider a third-party monitoring pipeline that can gather Prometheus-formatted metrics. 
* For event transfer
    * Several third-party tools exist to transfer/archive Kubernetes events, depending on your sink. heptiolabs/eventrouter has been suggested as a general alternative.


* [Tools for Monitoring Compute, Storage, and Network Resources | Kubernetes](https://kubernetes.io/docs/tasks/debug-application-cluster/resource-usage-monitoring/)

Heapster enables Container Cluster Monitoring and Performance Analysis for Kubernetes (versions v1.0.6 and higher), and platforms which include it.

* heapsterはcluster-wide aggreagtor of monitoring and event data.
* heapsterはPodとして動く
* heapsterはnodeを認識して、kubeletからmetricsを収集する
    * kubeletはdaemonとして全てのnodeで動いている
    * kubeletはkubernetes masterとnodeのbridge
    * REST APIでmetricsを提供している
* kubeletはcadvisorからmetricsを取得する
    * cadvisorもdaemonとして全てのnodeで動いている
    * cadvisorはCPU, memory, filesystem, and network usage statisticsなどを収集する
    * kubernetes上はWebUIがport`4194`で動いている
* heapsterはPodの情報をLabelにもとづいてgroupingする


## Metric model
* [heapster/model.md at master · kubernetes/heapster](https://github.com/kubernetes/heapster/blob/master/docs/model.md)

```
/heapster
--source=kubernetes.summary_api:''
--sink=stackdriver:?cluster_name=cluster-name&use_old_resources=true&use_new_resources=false&min_interval_sec=100&batch_export_timeout_sec=110
```

## Sources
* [heapster/source-configuration.md at master · kubernetes/heapster](https://github.com/kubernetes/heapster/blob/master/docs/source-configuration.md)

`--source=kubernetes.summary_api:''`

Kubelet/cAdvisorからmemory efficientに取得する。
`kubernetes`を指定した場合と同じmetricsは取得できる。

## CLI

* --source *flags.Uris
    * source(s) to watch (default [])
    * e.g. `kubernetes.summary_api:''`
* --sink *flags.Uris
    * external sink(s) that receive data (default [])
    * e.g. `stackdriver:?cluster_name=cluster-name&use_old_resources=true&use_new_resources=false&min_interval_sec=100&batch_export_timeout_sec=110`
* --sink-export-data-timeout duration
    * Timeout for exporting data to a sink (default 20s)

```
Usage of /heapster:                                                                                                                                                       [20/249]
      --allowed-users string                                    comma-separated list of allowed users
      --alsologtostderr                                         log to standard error as well as files
      --api-server                                              Enable API server for the Metrics API. If set, the Metrics API will be served on --insecure-port (internally) and --secure-port (externally).
      --authentication-kubeconfig string                        kubeconfig file pointing at the 'core' kubernetes server with enough rights to create tokenaccessreviews.authentic
ation.k8s.io.                                                                                                                                                                           --authentication-token-webhook-cache-ttl duration         The duration to cache responses from the webhook token authenticator. (default 10s)                                     --authorization-kubeconfig string                         kubeconfig file pointing at the 'core' kubernetes server with enough rights to create  subjectaccessreviews.author
ization.k8s.io.
      --authorization-webhook-cache-authorized-ttl duration     The duration to cache 'authorized' responses from the webhook authorizer. (default 10s)
      --authorization-webhook-cache-unauthorized-ttl duration   The duration to cache 'unauthorized' responses from the webhook authorizer. (default 10s)
      --bind-address ip                                         The IP address on which to listen for the --secure-port port. The associated interface(s) must be reachable by the rest of the cluster, and by CLI/web clients. If blank, all interfaces will be used (0.0.0.0). (default 0.0.0.0)                                                                        --cert-dir string                                         The directory where the TLS certs are located (by default /var/run/kubernetes). If --tls-cert-file and --tls-private-key-file are provided, this flag will be ignored. (default "/var/run/kubernetes")
      --client-ca-file string                                   If set, any request presenting a client certificate signed by one of the authorities in the client-ca-file is auth
enticated with an identity corresponding to the CommonName of the client certificate.
      --contention-profiling                                    Enable contention profiling. Requires --profiling to be set to work.
      --disable-export                                          Disable exporting metrics in api/v1/metric-export
      --disable-metric-sink                                     Disable metric sink
      --enable-swagger-ui                                       Enables swagger ui on the apiserver at /swagger-ui
      --heapster-port int                                       port used by the Heapster-specific APIs (default 8082)
      --historical-source string                                which source type to use for the historical API (should be exactly the same as one of the sink URIs), or empty to
disable the historical API
      --ignore-label stringSlice                                ignore this label when joining labels
      --label-separator string                                  separator used for joining labels (default ",")
      --listen-ip string                                        IP to listen on, defaults to all IPs
      --log-backtrace-at traceLocation                          when logging hits line file:N, emit a stack trace (default :0)
      --log-dir string                                          If non-empty, write log files in this directory
      --log-flush-frequency duration                            Maximum number of seconds between log flushes (default 5s)
      --logtostderr                                             log to standard error instead of files (default true)
      --max-procs int                                           max number of CPUs that can be used simultaneously. Less than 1 for default (number of cores)
      --metric-resolution duration                              The resolution at which heapster will retain metrics. (default 1m0s)
      --profiling                                               Enable profiling via web interface host:port/debug/pprof/ (default true)
      --requestheader-allowed-names stringSlice                 List of client certificate common names to allow to provide usernames in headers specified by --requestheader-user
name-headers. If empty, any client certificate validated by the authorities in --requestheader-client-ca-file is allowed.
      --requestheader-client-ca-file string                     Root certificate bundle to use to verify client certificates on incoming requests before trusting usernames in hea
ders specified by --requestheader-username-headers
      --requestheader-extra-headers-prefix stringSlice          List of request header prefixes to inspect. X-Remote-Extra- is suggested. (default [x-remote-extra-])
      --requestheader-group-headers stringSlice                 List of request headers to inspect for groups. X-Remote-Group is suggested. (default [x-remote-group])
      --requestheader-username-headers stringSlice              List of request headers to inspect for usernames. X-Remote-User is common. (default [x-remote-user])
      --secure-port int                                         The port on which to serve HTTPS with authentication and authorization. If 0, don't serve HTTPS at all. (default 6
443)
      --stderrthreshold severity                                logs at or above this threshold go to stderr (default 2)
      --store-label stringSlice                                 store this label separately from joined labels with the same name (name) or with different name (newName=name)
      --tls-ca-file string                                      If set, this certificate authority will used for secure access from Admission Controllers. This must be a valid PE
M-encoded CA bundle. Altneratively, the certificate authority can be appended to the certificate provided by --tls-cert-file.
      --tls-cert string                                         file containing TLS certificate
      --tls-cert-file string                                    File containing the default x509 Certificate for HTTPS. (CA cert, if any, concatenated after server cert). If HTTP
S serving is enabled, and --tls-cert-file and --tls-private-key-file are not provided, a self-signed certificate and key are generated for the public address and saved to /var/ru
n/kubernetes.
      --tls-client-ca string                                    file containing TLS client CA for client cert validation
      --tls-key string                                          file containing TLS key
      --tls-private-key-file string                             File containing the default x509 private key matching --tls-cert-file.
      --tls-sni-cert-key namedCertKey                           A pair of x509 certificate and private key file paths, optionally suffixed with a list of domain patterns which ar
e fully qualified domain names, possibly with prefixed wildcard segments. If no domain patterns are provided, the names of the certificate are extracted. Non-wildcard matches tru
mp over wildcard matches, explicit domain patterns trump over extracted names. For multiple key/certificate pairs, use the --tls-sni-cert-key multiple times. Examples: "example.k
ey,example.crt" or "*.foo.com,foo.com:foo.key,foo.crt". (default [])
  -v, --v Level                                                 log level for V logs
      --version                                                 print version info and exit
      --vmodule moduleSpec                                      comma-separated list of pattern=N settings for file-filtered logging
```


## Reference
* [kubernetes/heapster: Compute Resource Usage Analysis and Monitoring of Container Clusters](https://github.com/kubernetes/heapster)

