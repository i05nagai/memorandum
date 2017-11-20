---
title: Billing
---

## Billing

## Export to BigQuery
bigqueryにexportできる。

schemaは以下のようになる。

* _PARTITIONTIME
* billing_account_id
    * STRING
* service
* service.id
    * STRING
* service.description
    * STRING
* sku
* sku.id
    * STRING
* sku.description
    * STRING
* usage_start_time
    * TIMESTAMP
* usage_end_time
    * TIMESTAMP
* project
* project.id
    * STRING
* project.name
    * STRING
* project.labels
* project.labels.key
    * STRING
* project.labels.value
    * STRING
* labels
* labels.key
    * STRING
* labels.value
    * STRING
* export_time
    * TIMESTAMP
* cost
    * FLOAT
* currency
    * STRING
* currency_conversion_rate
    * FLOAT
* usage
* usage.amount
    * FLOAT
* usage.unit
    * STRING
* credits
* credits.name
    * STRING
* credits.amount
    * FLOAT

## Reference
