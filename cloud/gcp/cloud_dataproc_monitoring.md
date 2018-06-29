---
title: Cloud Dataproc Monitoring
---

## Cloud Dataproc Monitoring


## Stackdriver
* [Stackdriver monitoring  \|  Cloud Dataproc Documentation  \|  Google Cloud](https://cloud.google.com/dataproc/docs/guides/stackdriver-monitoring)


## Job dirver output
[Job driver output  \|  Cloud Dataproc Documentation  \|  Google Cloud](https://cloud.google.com/dataproc/docs/guides/driver-output)

Configure logging.
By default logging level is `INFO`


```
gcloud dataproc jobs submit hadoop ...\
  --driver-log-levels root=FATAL,com.example=INFO
```


## Reference
