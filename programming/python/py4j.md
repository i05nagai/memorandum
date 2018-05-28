---
title: Py4J
---

## Py4J
[spark/java_gateway.py at master · apache/spark](https://github.com/apache/spark/blob/master/python/pyspark/java_gateway.py)


## Writing python programs

```python
from py4j.java_gateway import JavaGateway
gateway = JavaGateway()

# constructor and static method
arr = gateway.jvm.java.util.ArrayList()
```
 
## Convert python collections to Java collections
* [3. Advanced Topics — Py4J](https://www.py4j.org/advanced_topics.html)

## Tips
```python
from py4j.java_gateway import java_import
java_import(gateway.jvm, "org.apache.spark.SparkConf")
```

## Reference
* [Welcome to Py4J — Py4J](https://www.py4j.org/)
