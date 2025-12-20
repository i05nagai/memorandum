---
title: Spanner Graph Query
---

## Spanner Graph Query


## Example


## Path pattern
```
  (a:Account)-[e:Transfers]->(b:Account)          -- path pattern
  WHERE a != b                                    -- WHERE clause
```

```
(a:Account)-[e:Transfers]->(b:Account)          -- path pattern
```

## Element pattern
https://cloud.google.com/spanner/docs/reference/standard-sql/graph-patterns#element_pattern_definition



### property_filters
It contains a key value map of element properties and their values.

```
{name: 'Cruz Richards'}
{last_name: 'Richards', albums: 2}
```

### element_property




## Statements

### Filter Statement
The syntax for the FILTER statement is similar to the syntax for the graph pattern WHERE clause, but they are evaluated differently.
The FILTER statement is evaluated after the previous statement. The WHERE clause is evaluated as part of the containing statement.

## Pattern
Graph Query Language (GQL) supports the following patterns.
Patterns can be used in a MATCH statement.



## Reference




