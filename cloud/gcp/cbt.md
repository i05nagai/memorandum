---
title: cbt
---

## cbt

## Install

```
gcloud components update
gcloud components install cbt
```

## Configuration

- `~/.cbtrc`

```
project = project-id
instance = quickstart-instance
```


## Usage
You can export the crendential with `GOOGLE_APPLICATION_CREDENTIALS`.
Or json file can be specified with `-creds`

```
cbt -project <project> -instance <instance> [cmd]
```

List instances

```
cbt listinstances
```

Count rows in a table

```
cbt count <table-id>
```

Create an instance with an initial cluster

```
cbt createinstance <instance-id> <display-name> <cluster-id> <zone> <num-nodes> <storage-type>
```

Create a cluster in the configured instance

```
cbt createcluster <cluster-id> <zone> <num-nodes> <storage-type>
cbt createcluster my-instance-c2 europe-west1-b 3 SSD
```

Create a column family

```
cbt createfamily <table-id> <family>
```

Create a table

```
cbt createtable <table-id> [families=<family>:gcpolicy=<gcpolicy-expression>,...]
```

- families
    - Column families and their associated garbage collection (gc) policies.
    - Put gc policies in quotes when they include shell operators && and ||. For gcpolicy,
    - see "setgcpolicy".
- splits
    - Row key(s) where the table should initially be split


Update a cluster in the configured instance

```
cbt updatecluster
```



```
cbt deleteinstance              Delete an instance
cbt deletecluster               Delete a cluster from the configured instance
cbt deletecolumn                Delete all cells in a column
cbt deletefamily                Delete a column family
cbt deleterow                   Delete a row
cbt deleteallrows               Delete all rows
cbt deletetable                 Delete a table
```

Batch write many rows based on the input file

```
cbt import <table-id> <input-file> [app-profile=<app-profile-id>] [column-family=<family-name>] [batch-size=<500>] [workers=<1>]
```

Set value of a cell (write)

```
cbt set <table-id> <row-key> [app-profile=<app-profile-id>] <family>:<column>=<val>[@<timestamp>]
```

```
cbt listclusters                List clusters in an instance
cbt lookup                      Read from a single row
cbt ls                          List tables and column families
cbt read                        Read rows
cbt setgcpolicy                 Set the garbage-collection policy (age, versions) for a column family
cbt waitforreplication          Block until all the completed writes have been replicated to all the clusters
cbt createtablefromsnapshot     Create a table from a backup
cbt createsnapshot              Create a backup from a source table
cbt listsnapshots               List backups in a cluster
cbt getsnapshot                 Get backups info
cbt deletesnapshot              Delete snapshot in a cluster
cbt createappprofile            Create app profile for an instance
cbt getappprofile               Read app profile for an instance
cbt listappprofile              Lists app profile for an instance
cbt updateappprofile            Update app profile for an instance
cbt deleteappprofile            Delete app profile for an instance
```

## Reference
- https://cloud.google.com/bigtable/docs/cbt-overview
