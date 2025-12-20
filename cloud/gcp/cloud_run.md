---
title: Cloud Run
---

## Cloud Run


## HTTP

### Best practices
Use startup CPU boost to reduce startup latency

- Write effective services
- Optimize performance
    - Start containers quickly
    - Use startup CPU boost to reduce startup latency
    - Use minimum instances to reduce cold starts
    - Use dependencies wisely
    - Use global variables
- Perform lazy initialization of global variables
- Optimize concurrency
    - Tune concurrency for your service


## Jobs

### Best practices

- Use task retries
    - 0 means no retry
    - 3 retries by default
- Plan for job task restarts
    - idempotent
- Use checkpointing
    - example1: write to GCS object and query before running
        - 1. Write your progress every 10 minutes or whatever your lost work tolerance allows, to a pi-progress.txt Cloud Storage object.
        - 2. When a task starts, query the pi-progress.txt object and load the value as a starting place. Use that value as the initial input to your function.
        - 3. Write your final result to Cloud Storage as an object named pi-complete.txt to avoid duplication via parallel or repeated execution or pi-complete-DATE.txt to differentiate by completion date.
    - 



## Environment Variables
- https://cloud.google.com/run/docs/container-contract#env-vars

- CLOUD_RUN_JOB
- CLOUD_RUN_EXECUTION
- CLOUD_RUN_TASK_INDEX
- CLOUD_RUN_TASK_ATTEMPT
- CLOUD_RUN_TASK_COUNT




## Reference

