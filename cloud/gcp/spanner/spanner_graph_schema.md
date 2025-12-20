---
title: Spanner Graph Schema
---

## Spanner Graph Schema


## Property

```
CREATE PROPERTY GRAPH FinGraph
  NODE TABLES (
    GraphNode
      DYNAMIC LABEL (label)
      DYNAMIC PROPERTIES (properties)
)
  EDGE TABLES (
    GraphEdge
      SOURCE KEY (id) REFERENCES GraphNode(id)
      DESTINATION KEY (dest_id) REFERENCES GraphNode(id)
      DYNAMIC LABEL (label)
      DYNAMIC PROPERTIES (properties)
);
```

## Reference
- https://cloud.google.com/spanner/docs/reference/standard-sql/graph-schema-statements
