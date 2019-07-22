---
title: avro
---

## avro


## Install

```
pip install avro
pip install avro-python3
```

## API

## Usage


```python
import avro.schema
schema = avro.schema.parse(open("user.avsc", "rb").read())
```

```python
import avro.datafile
import avro.io
writer = avro.datafile.DataFileWriter(open("users.avro", "wb"), avro.io.DatumWriter(), schema)
writer.append({"name": "Alyssa", "favorite_number": 256})
writer.append({"name": "Ben", "favorite_number": 7, "favorite_color": "red"})
writer.close()

reader = avro.datafile.DataFileReader(open("users.avro", "rb"), avro.io.DatumReader())
for user in reader:
    print user
reader.close()
```

## Reference
- [Apache Avro™ 1\.8\.2 Getting Started \(Python\)](https://avro.apache.org/docs/1.8.2/gettingstartedpython.html)
