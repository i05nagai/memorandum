---
title: Grafana
---

## Grafana



- `$__interval`
    - it refer to `interval` parameter in query option
- `$__rate_interval`
    - https://grafana.com/blog/2020/09/28/new-in-grafana-7.2-__rate_interval-for-prometheus-rate-queries-that-just-work/
    - it's same as `__interval` parameter but it guarantee that it won't be smaller than the required size of interval for `rate` function


## Display name
https://grafana.com/docs/grafana/latest/panels-visualizations/configure-standard-options/#display-name

- `${__field.displayName}	`




## Reference
* [Grafana - The open platform for analytics and monitoring](https://grafana.com/)
