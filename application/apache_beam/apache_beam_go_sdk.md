---
title: Apache Beam Go SDK
---

## Apache Beam Go SDK


## Beam programming
https://beam.apache.org/documentation/programming-guide/

## CLI options

- -async
    - Do not wait for job completion.
- -autoscaling_algorithm string
    - Autoscaling mode to use (optional).
- -beam_strict
    - Apply additional validation to pipelines.
- -control_endpoint string
    - Local control gRPC endpoint (required in worker mode).
- -cpu_profiling string
    - Job records CPU profiles to this GCS location (optional)
- -dataflow_endpoint string
    - Dataflow endpoint (optional).
- -dataflow_kms_key string
    - The Cloud KMS key identifier used to encrypt data at rest (optional).
- -dataflow_service_options string
    - Comma separated list of additional job modes and configurations (optional)
- -disk_size_gb int
    - Size of root disk for VMs, in GB (optional).
- -disk_type string
    - Type of root disk for VMs (optional).
- -dot_file string
    - DOT output file to create
- -dry_run
    - Dry run. Just print the job, but don't submit it.
- `-endpoint string`
    - Job service endpoint (required).
- `-environment_config string`
    - Set environment configuration for running the user code.
    - For DOCKER: Url for the docker image.
    - For PROCESS: json of the form `{"os": "<OS>", "arch": "<ARCHITECTURE>", "command": "<process to execute>", "env":{"<Environment variables 1>": "<ENV_VAL>"} }`.
    - All fields in the json are optional except command.
- `-environment_type string`
        Environment Type. Possible options are DOCKER, EXTERNAL, and LOOPBACK.
- `-execute_async`
    - Asynchronous execution. Submit the job and return immediately. Alias of --async.
- `-experiments string`
    - Comma-separated list of experiments (optional).
- `-flexrs_goal string`
    - Which Flexible Resource Scheduling mode to run in (optional)
- `-id string`
    - Local identifier (required in worker mode).
- `-input string`
    - File(s) to read. (default "./file.txt")
- `-job_name string`
    - Job name (optional).
- `-labels string`
    - JSON-formatted map[string]string of job labels (optional).
- `-logging_endpoint string`
    - Local logging gRPC endpoint (required in worker mode).
- `-machine_type string`
    - alias of worker_machine_type (optional)
- `-max_num_workers int`
    - Maximum number of workers during scaling (optional).
- `-min_cpu_platform string`
    - GCE minimum cpu platform (optional)
- `-network string`
    - GCP network (optional)
- `-no_use_public_ips`
    - Workers must not use public IP addresses (optional)
- `-num_workers int`
    - Number of workers (optional).
- `-number_of_worker_harness_threads int`
    - The number of threads per each worker harness process (optional).
- `-options string`
    - JSON-encoded pipeline options (required in worker mode). (deprecated)
- `-output string
    - `Output file (required).
- `-parallelism int`
    - The degree of parallelism to be used when distributing operations onto Flink workers. (default -1)
- `-project string`
    - Google Cloud Platform project ID.
- `-region string`
    - GCP Region (required)
- `-resource_hints value`
    - Set whole pipeline level resource hints, accepting values of the format '<urn>=<value>'. eg.'min_ram=12GB', 'beam:resources:accelerator:v1='runner_specific' In case of duplicate hint URNs, the last value specified will be used. See https://beam.apache.org/documentation/runtime/resource-hints/ for more information.
- `-retain_docker_containers`
    - Retain Docker containers created by the runner.
- `-runner string`
    - Pipeline runner.
- `-sdk_container_image string`
    - Worker harness container image (optional).
- `-sdk_harness_container_image_override value`
    - Overrides for SDK harness container images. Could be for the local SDK or for a remote SDK that pipeline has to support due to a cross-language transform. Each entry consists of two values separated by a comma where first value gives a regex to identify the container image to override and the second value gives the replacement container image. Multiple entries can be specified by using this flag multiple times. A container will have no more than 1 override applied to it. If multiple overrides match a container image it is arbitrary which will be applied.
- `-semi_persist_dir string`
    - Local semi-persistent directory (optional in worker mode). (default "/tmp")
- `-service_account_email string`
    - Service account email (optional).
- `-small_word_length int`
    - length of small words (default: 9) (default 9)
- `-staging_location string`
    - GCS staging location (required).
- `-subnetwork string`
    - GCP subnetwork (optional)
- `-teardown_policy string`
    - Job teardown policy (internal only).
- `-temp_location string`
    - Temp location (optional)
- `-template_location string`
    - GCS location to save the job graph. If set, the job is not submitted to Dataflow (optional.)
- `-transform_name_mapping string`
    - JSON-formatted mapping of old transform names to new transform names for pipeline updates (optional)
- `-update`
    - Submit this job as an update to an existing Dataflow job (optional); the job name must match the existing job to update
- `-use_public_ips`
    - Workers must use public IP addresses (optional) (default true)
- `-worker`
    - Whether binary is running in worker mode.
- `-worker_binary string`
    - Worker binary (optional)
- `-worker_harness_container_image string`
    - Worker harness container image (optional). Deprecated in favor of the sdk_container_image flag.
- `-worker_machine_type string`
    - GCE machine type (optional)
- `-worker_region string`
    - Dataflow worker region (optional)
- `-worker_zone string`
    - Dataflow worker zone (optional)
- `-zone string`
    - GCP zone (optional)


## ParDo


```go

func init() {
    register.DoFn3x0[context.Context, string, func(string)](&extractFn{})
}

type extractFn struct {
	SmallWordLength int `json:"smallWordLength"`
}

func (f *extractFn) ProcessElement(ctx context.Context, line string, emit func(string)) {
	if len(strings.TrimSpace(line)) == 0 {
		empty.Inc(ctx, 1)
	}
	for _, word := range wordRE.FindAllString(line, -1) {
		if len(word) < f.SmallWordLength {
			smallWords.Inc(ctx, 1)
		}
		emit(word)
	}
}
```

## IterX
https://beam.apache.org/documentation/programming-guide/#side-inputs



## Sync

```
resource.type="dataflow_step"
resource.labels.job_id="2022-06-29_08_02_54-JOB_ID"
labels."compute.googleapis.com/resource_name"="testpipeline-jenkins-0629-DATE-cyhg-harness-8crw"
logName=("projects/apache-beam-testing/logs/dataflow.googleapis.com%2Fdocker"
OR
"projects/apache-beam-testing/logs/dataflow.googleapis.com%2Fworker-startup"
OR
"projects/apache-beam-testing/logs/dataflow.googleapis.com%2Fworker")
```



## Cross language features
You need to run expansion server to use cross language feature.

Numbered release:

The expansion service jar is vendored as module `org.apache.beam:beam-sdks-java-io-google-cloud-platform-expansion-service` in Maven Repository.
This jar can be executed directly with the following command.

Development env:

This requires that the JAVA_HOME environment variable points to your JDK installation. From the root `beam/` directory of the Apache Beam repository, the jar can be built (or built and run) with the following commands:


On dataflow


### Expansion service
https://beam.apache.org/documentation/programming-guide/#create-x-lang-transforms



## Reference
- https://docs.google.com/document/d/1yj0_hxq2J1iestjFUUrm_BVQLsFxQiiqtcFhgodzIgM/edit?tab=t.0#heading=h.mgr8mrx81tnc
- https://cloud.google.com/dataflow/docs/reference/service-options
