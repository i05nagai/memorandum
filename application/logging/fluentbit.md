---
title: fluentbit
---

## fluentbit

```
systemctl enable fluentbit
```


- Input -> Parser -> Filter -> Buffer -> Routing -> Output

## Parser


## Configuration
- `/etc/fluent-bit`

#### Parser
https://docs.fluentbit.io/manual/pipeline/parsers/configuring-parser

predefined parsers exist in `/etc/fluent-bit/parsers.conf`

- Format
    - json, regex, ltsv or logfmt.
- Regex

#### Inputs
- Tail
    - https://docs.fluentbit.io/manual/pipeline/inputs/tail
    - Buffer_Chunk_Size
    - Buffer_Max_Size


#### Outputs

- File
    - 

## Reference
- https://docs.fluentbit.io/manual/administration/configuring-fluent-bit
