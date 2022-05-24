---
title: Apache Avro
---

## Apache Avro
There are two notations for schema.

- IDL. Suffix is typically `.avdl`.
- JSON expression. Suffix is typically `.avsc`.


- `namespace`
    - A namespace is a dot-separated sequence of such names.
    - The empty string may also be used as a namespace to indicate the null namespace.
    - Equality of names (including field names and enum symbols) as well as fullnames is case-sensitive.
- `protocol`
    - A protocol is a JSON object with the following attributes
        - `protocol`
            - a string, the name of the protocol (required)
        - `namespace`
            - an optional string that qualifies the name;
        - `doc`
            - an optional string describing this protocol;
        - `types`
            - an optional list of definitions of named types (records, enums, fixed and errors). An error definition is just like a record definition except it uses "error" instead of "record". Note that forward references to named types are not permitted.
        - `messages`
            - an optional JSON object whose keys are message names and whose values are objects whose attributes are described below. No two messages may have the same name.




## IDL

## JSON schema

#### Example

```
{
  "type": "record",
  "name": "LongList",
  "aliases": ["LinkedLongs"],                      // old name for this
  "fields" : [
    {"name": "value", "type": "long"},             // each element has a long
    {"name": "next", "type": ["null", "LongList"]} // optional next element
  ]
}
```

## Reference
- Apache Avro™ 1.11.0 Specification https://avro.apache.org/docs/current/spec.html
