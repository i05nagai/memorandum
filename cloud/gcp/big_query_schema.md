---
title: BigQuery Schema
---

## BigQuery Schema

* `name`
* `type`
    * [Standard SQL Data Types  \|  BigQuery  \|  Google Cloud](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#geography)
    * `STRING`
    * `INT64`
    * `NUMERIC`
    * `FLOAT64`
    * `BOOL`
    * `BYTES`
    * `DATE`
    * `DATETIME`
    * `TIMESTAMP`
    * `GEOGRAPHY`
    * `TIME`
    * `ARRAY`
    * `STRUCT`

* `mode`
    * `NULLABLE`
* `description`
* `fields`


```json
[
    {
        "name": "id",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "first_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "last_name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "dob",
        "type": "DATE",
        "mode": "NULLABLE"
    },
    {
        "name": "addresses",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "status",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "address",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "city",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "state",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "zip",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "numberOfYears",
                "type": "STRING",
                "mode": "NULLABLE"
            }
        ]
    }
]
```

## Reference
* [Specifying Nested and Repeated Columns  \|  BigQuery  \|  Google Cloud](https://cloud.google.com/bigquery/docs/nested-repeated)
