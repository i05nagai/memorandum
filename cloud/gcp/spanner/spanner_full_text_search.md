---
title: Spanner Full Text Search
---

## Spanner Full Text Search

## Search Index or Secondary Index
https://cloud.google.com/spanner/docs/full-text-search/search-vs-secondary-index


## Combined Tokenlists
https://cloud.google.com/spanner/docs/full-text-search/combine-tokenlists

### Combined Token

(1) Tokenize words separately and concatenate TOKENLISTs
(2) Concatenate strings and tokenize the result

### Query-side TOKENLIST concatenation


## Search Index and non search inex
https://cloud.google.com/spanner/docs/full-text-search/mix-full-text-and-non-text-queries


## Internal layout
https://docs.cloud.google.com/spanner/docs/full-text-search/search-indexes

- docid



## Exact match
For exact match, use `TOKEN` 

```
ALTER TABLE Albums
  ADD COLUMN AlbumTitle_Tokens TOKENLIST
  AS (TOKEN(AlbumTitle)) HIDDEN;
CREATE SEARCH INDEX Albums_By_AlbumTitle_Tokens
  ON Albums(AlbumTitle_Tokens);
```

In query,

```
select
    *
from
    Almbums
where
    AlbumTitle = 'albumtitle'
;
```


## Limitation

### Number of columns
Search index can have only 15 columns (+primary key).
If you use exact match, it consume 1 column for exact match.
There are some workaround for this limitation

#### (1) Use JSON


```sql
CREATE TABLE
  table4 (
    id STRING(4) ,
    json1 JSON
    )
PRIMARY KEY
  (id);
INSERT INTO
  table4 (id,
    json1)
VALUES
  ('1', -- type: STRING(4)
    JSON'{"key1": "v11", "key2": "v12"}'
    ),
  ('2', -- type: STRING(4)
    JSON'{"key1": "v12", "key2": "v22", "key3": "v23"}'
    )
THEN RETURN
  id,
  json1;


ALTER TABLE table4
  ADD COLUMN json1_tokens TOKENLIST
  AS (TOKENIZE_JSON(json1)) HIDDEN;

-- do not forget to store original JSON column
CREATE SEARCH INDEX
    index_table4_json1_storing
    ON table4 (json1_tokens)
    STORING(json1)
    ;
```

This workaround can be used if exact match is used with AND condition.

#### (2)


## Reference

