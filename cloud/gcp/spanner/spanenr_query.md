---
title: Spanner Query
---

## Spanner Query


## Tips

### Many-to-Many Relationships
https://cloud.google.com/blog/products/databases/resolve-and-optimize-many-to-many-relationships-in-spanner/

Index with STORING

```
CREATE INDEX idx_groupId_ext ON membership(group_id) STORING (enrolled);
```


Foreign keys

```sql
CREATE TABLE membership (
  user_id INT64,
  group_id INT64,
  enrolled TIMESTAMP NOT NULL OPTIONS (allow_commit_timestamp=true),
  CONSTRAINT FKUsertomember FOREIGN KEY(group_id) REFERENCES GroupMgmt(group_id),
     CONSTRAINT FKGrouptomember FOREIGN KEY(user_id) REFERENCES Users(user_id),
) PRIMARY KEY(user_id, group_id);
```

Interleaving

```sql
CREATE TABLE membership_user (
  user_id INT64,
  group_id INT64,
  enrolled TIMESTAMP NOT NULL OPTIONS (allow_commit_timestamp = true),
) PRIMARY KEY(user_id, group_id),
INTERLEAVE IN PARENT Users ON DELETE CASCADE;

CREATE TABLE membership_group (
  group_id INT64,
  user_id INT64,
  enrolled TIMESTAMP NOT NULL OPTIONS (allow_commit_timestamp = true),
) PRIMARY KEY(group_id, user_id),
INTERLEAVE IN PARENT GroupMgmt ON DELETE CASCADE;
```


## Reference

