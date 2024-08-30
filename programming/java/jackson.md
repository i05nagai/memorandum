---
title: Jackson
---

## Jackson

getterもjsonにserializeされる。
getterのserializeをやめたい場合は、annotationをつける。

```
@JsonIgnore
```


## Pacakges

- `com.fasterxml.jackson.datatype:jackson-datatype-jsr310`
    - To support OffsetDatetime

```
// Up to Jackson 2.9: (but not with 3.0)
ObjectMapper mapper = new ObjectMapper()
   .registerModule(new ParameterNamesModule())
   .registerModule(new Jdk8Module())
   .registerModule(new JavaTimeModule()); // new module, NOT JSR310Module

// with 3.0 (or with 2.10 as alternative)
ObjectMapper mapper = JsonMapper.builder() // or different mapper for other format
   .addModule(new ParameterNamesModule())
   .addModule(new Jdk8Module())
   .addModule(new JavaTimeModule())
   // and possibly other configuration, modules, then:
   .build();
```

## Reference
* [FasterXML/jackson: Main Portal page for the Jackson project](https://github.com/FasterXML/jackson)
