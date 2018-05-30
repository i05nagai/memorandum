---
title: bq
---

## bq
bq command.

## CLI

### bq cp

### bq ls
List the objects contained in the named collection.

```
bq ls -n 1000 dataset
```

* `-n num`
    * the number of results
* `-j`
    * show the jobs in the named project
* `-a`
* `-p`
    * show all projects.
* `--filter`
* `--transfer_config --transfer_location='us'`

Show all jobs in projcet

```
bq ls -j project_id
```

Show all projcets

```
bq ls -p -n 1000
```

Show all tables

```
bq ls dataset_name
```

### bq query
* `--nouse_legacy_sql`
* `--replace`
* `--destination_table id`
    * `project_id.dataset_id.table_id`
    * `project_id.dataset_id.table_id$yyyymmdd`
* `--time_partitioning_field field_name`
* `--dry_run`
* `--noflatten_results`
* `--batch`
    * default false
    * batch mode
* `--apend_table`
    * default false
* `--maximum_bytes_billed INTEGER`
    * The upper limit of bytes billed for the query
* `--min_completion_ratio`
    * [Experimental]
    * The minimum fraction of data that must be scanned before a query returns. If not set, the default server value (1.0) will be used.
    * a number in the range [0, 1.0]
* `--parameter`
    * Either a file containing a JSON list of query parameters, or a query parameter in the form `name:type:value`.
    * An empty name produces a positional parameter.
    * The type may be omitted to assume STRING: name::value or ::value.
    * The value "NULL" produces a null value.
    * repeat this option to specify a list of values
* `--[no]replace`
    * default: 'false'
    * If true, erase existing contents before loading new data.
* `--[no]require_cache`
    * Whether to only run the query if it is already cached.
* `--[no]require_partition_filter`
    * Whether to require partition filter for queries over this table. Only apply to partitioned table.
* `--[no]rpc`
    * default false
    * If true, use rpc-style query API instead of jobs.insert().
* `--schema_update_option`
    * Can be specified when append to a table, or replace a table partition. When specified, the schema of the destination table will be updated with the
*   schema of the new data. One or more of the following options can be specified:
    * `ALLOW_FIELD_ADDITION`
        * allow new fields to be added
    * `ALLOW_FIELD_RELAXATION`
        * allow relaxing required fields to nullable; repeat this option to specify a list of values
* `-s,--start_row`
    * default 0
    * First row to return in the result.
* `--time_partitioning_expiration`
    * integer
    * Enables time based partitioning on the table and set the number of seconds for which to keep the storage for a partition.
    * The storage will have an expiration time of its creation time plus this value. A negative number means no expiration.
* `--time_partitioning_field`
    * Enables time based partitioning on the table and the table will be partitioned based on the value of this field. If time based partitioning is enabled without this value, the table will be partitioned based on the loading time.
* `--time_partitioning_type`
    * Enables time based partitioning on the table and set the type. The only type accepted is DAY, which will generate one partition per day.
* `--udf_resource`
    * The URI or local filesystem path of a code file to load and evaluate immediately as a User-Defined Function resource.;
    * repeat this option to specify a list of values
* `--[no]use_cache`
    * Whether to use the query cache to avoid rerunning cached queries.
* `--[no]use_legacy_sql`
    * Whether to use Legacy SQL for the query. If not set, the default value is true.

## Usage

create partitioned table from query resulst

```
cat query.sql | bq query \
  --nouse_legacy_sql \
  --destination_table "project_id:dataset_id.destination_table" \
  --time_partitioning_field field_name
```

insert query result to

```
cat query.sql | bq query \
    --use_legacy_sql=false \
    --allow_large_results \
    --replace \
    --noflatten_results \
    --destination_table 'mydataset.temps$20180101' \
```

## Reference

