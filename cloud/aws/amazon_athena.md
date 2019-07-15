---
title: Amazon Athena
---

## Amazon Athena


## Query
- [6\.11\. Regular Expression Functions — Presto 0\.172 Documentation](https://prestodb.github.io/docs/0.172/functions/regexp.html)

Convert string to timestamp

```sql
CASE
  WHEN regexp_like(col, '[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z')
    THEN DATE_PARSE(col, '%Y-%m-%dT%H:%i:%sZ')
  WHEN regexp_like(col, '[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]+Z')
    THEN DATE_PARSE(col, '%Y-%m-%dT%H:%i:%s.%fZ')
  ELSE DATE_PARSE(col, '%Y-%m-%dT%H:%i:%s.%fZ')
END AS col_timestamp
```

## SQL Queries
* Query Engine is based on Presto

### Geospatial query
* [What is a Geospatial Query? \- Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/geospatial-query-what-is.html)

* Data format
    * WKT, GeoJSON are supported
* Data type
    * point
    * line
    * polygon
    * multiline
    * multipolygon
* Gespatial function
    * [List of Supported Geospatial Functions \- Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/geospatial-functions-list.html)

## Pricing
* 5 USD per TB



## Reference

