---
title: Cloud Logging
---

## Cloud Logging

## Log Entry Type

- Admin Activity audit logs
- System Event audit logs
- Google Workspace Admin Audit logs
- Enterprise Groups Audit logs
- Login Audit logs
- Access Transparency logs


## Opentelemetry or cloud logging
https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach

- GKE
    - metric
        - Use the OpenTelemetry SDK and the OTLP exporter for your language.
    - trace
        - OTLP exporter to Cloud Trace
        - configure opentelemetry collector
    - log
        - Configure your app to output JSON-structured logs to stdout and stderr. For a list of frameworks, see Recommended logging frameworks.


## Example go
https://github.com/GoogleCloudPlatform/berglas/blob/ab59822b8857d5ffc5bd7e57b79974c90c592dd6/pkg/berglas/logging/formats.go


## Reference


