---
title: Cloud Dataproc
---

## Cloud Dataproc

## Concepts
* Auto-created staging bucket
    * When you create a cluster, Cloud Dataproc creates a Cloud Storage staging bucket in your project or reuses an existing Cloud Dataproc-created bucket from a previous cluster creation request.
    * Created for each region
* preemptible(secondary) worker
* Single node cluster
    * act as master and worker
    * Trying out new versions of Spark and Hadoop or other open source components
    * Building proof-of-concept (PoC) demonstrations
    * Lightweight data science
    * Small-scale non-critical data processing
    * Education related to the Spark and Hadoop ecosystem

## Submit jobs
* via gcloud 
* via spark-shell or spark-submit in 

## Jobs

### Restartable jobs
By default, Cloud Dataproc jobs will not automatically restart on failure.
Restartable jobs are especially useful for long-running and streaming jobs.

* Successful
    * the driver terminates with code 0.
* failed
    * The driver terminates with a non-zero code more than 4 times in 10 minutes.
    * The driver terminates with non-zero code, and has exceeded the max_failures_per_hour setting.
* restart
    * the driver exits with a non-zero code, is not thrashing, and is within the max_failures_per_hour setting.

### Job state
[Life of a Cloud Dataproc Job  \|  Cloud Dataproc Documentation  \|  Google Cloud](https://cloud.google.com/dataproc/docs/concepts/jobs/life-of-a-job)

`dataproc` agent

1. User submits job to Cloud Dataproc.
    * JobStatus.State is marked as `PENDING`.
2. Job waits to be acquired by the `dataproc` agent.
    * `RUNNING`
        * If the job is acquired
    * `ERROR`
    * If the job is not acquired due to agent failure, Compute Engine network failure, or other cause
3. Once a job is acquired by the agent, the agent verifies that there are sufficient resources available on the Cloud Dataproc cluster's master node to start the driver.
    * `QUEUED`
        * If sufficient resources are not available, the job is delayed (throttled).
        * `Job.JobStatus.details` provides information on the cause of the delay.
4. If sufficient resources are available, the `dataproc` agent starts the job driver process.
    * At this stage, typically there are one or more applcations running in Apache Hadoop YARN.
    * However, Yarn applications may not start until the driver finishes scanning Cloud Storage directories or performing other start-up job tasks.
5. The `dataproc` agent periodically sends updates to Cloud Dataproc on job progress, cluster metrics, and Yarn applications associated with the job
6. Yarn application complete.
    * `RUNNING`
        * while driver performs any job completion tasks, such as materializing collections.
        * An unhandled or uncaught failure in the Main thread can leave the driver in a zombie state, without cause of failure
7. Driver exits. `dataproc` agent reports completion to Cloud Dataproc.
    * `DONE`


### job monitoring
[Life of a Cloud Dataproc Job  \|  Cloud Dataproc Documentation  \|  Google Cloud](https://cloud.google.com/dataproc/docs/concepts/jobs/life-of-a-job#job_monitoring_and_debugging)

```
gcloud dataproc jobs describe job-id
```

## Managing clusters

### Scaling clusters
[Scaling clusters  \|  Cloud Dataproc Documentation  \|  Google Cloud](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/scaling-clusters)


Scale up/Scale down.

```
gcloud dataproc clusters update cluster-name \
  [--num-workers and/or --num-preemptible-workers] new-number-of-workers
```

Scale down.
Use Graceful Decommisioning to avoid losing work in progress.
Take a few minutes to finish changes.
Actual size and expected size can be different in the graceful procedure.

* You can forcefully decommission preemptible workers at any time.
* You gracefully decommission primary workers at any time
* [YARN914 Umbrella Support graceful decommission of nodemanager ASF JIRA](https://issues.apache.org/jira/browse/YARN-914)

```
gcloud dataproc clusters update cluster-name \
  --graceful-decommission-timeout="timeout-value" \
  [--num-workers and/or --num-preemptible-workers]=decreased-number-of-workers
  other args ...
```


## Cluster Web Interface
[Cluster Web interfaces  \|  Cloud Dataproc Documentation  \|  Google Cloud](https://cloud.google.com/dataproc/docs/concepts/accessing/cluster-web-interfaces#create_an_ssh_tunnel)

| Web UI               | Port  | URL                          |
|----------------------|-------|------------------------------|
| YARN ResourceManager | 8088  | http://master-host-name:8088 |
| HDFS NameNode        | 9870* | http://master-host-name:9870 |

## Configuration


## Tips

### Install jupyter notebook
[Install and run a Jupyter notebook on a Cloud Dataproc cluster  \|  Cloud Dataproc Documentation  \|  Google Cloud](https://cloud.google.com/dataproc/docs/tutorials/jupyter-notebook)



## Pricing

Standard (Iowa)

| Machine type   | Virtual CPUs | Memory | Dataproc Premium (USD) |
|----------------|--------------|--------|------------------------|
| n1-standard-1  | 1            | 3.75GB | 0.010USD               |
| n1-standard-2  | 2            | 7.5GB  | 0.020USD               |
| n1-standard-4  | 4            | 15GB   | 0.040USD               |
| n1-standard-8  | 8            | 30GB   | 0.080USD               |
| n1-standard-16 | 16           | 60GB   | 0.160USD               |
| n1-standard-32 | 32           | 120GB  | 0.320USD               |
| n1-standard-64 | 64           | 240GB  | 0.640USD               |

There are Highmemory and HighCPU machine types.

Exampel

| Item         | Machine Type  | Virtual CPUs | Attached persistent disk | Number in cluster |
|--------------|---------------|--------------|--------------------------|-------------------|
| Master Node  | n1-standard-4 | 4            | 500 GB                   | 1                 |
| Worker Nodes | n1-standard-4 | 4            | 500 GB                   | 5                 |

num of vCPUs * hours * Cloud Dataproc price

= 24 * 2h * 0.01USD/h = 0.48 USD

= 24 * 24h * 0.01USD/h = 5.76 USD

= 24 * 24h * 30day * 0.01USD/h = 172.8 USD




## Reference
https://cloud.google.com/dataproc/docs/concepts/overview
