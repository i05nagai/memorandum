---
title: Apache Spark Logging
---

## Apache Spark Logging



## Tips
- [python \- PySpark Throwing error Method \_\_getnewargs\_\_\(\[\]\) does not exist \- Stack Overflow](https://stackoverflow.com/questions/40470487/pyspark-throwing-error-method-getnewargs-does-not-exist)
- [How to log in Apache Spark](https://hackernoon.com/how-to-log-in-apache-spark-f4204fad78a)
- Using spark inside flatMap or any transformation that occures on executors is not allowed (spark session is available on driver only)



#### Best practice for logging in Pyspark
- https://gist.github.com/smartnose/9f173b4c36dc31310e8efd27c3535a14#logging-in-pyspark
- [apache spark \- PySpark Logging? \- Stack Overflow](https://stackoverflow.com/questions/37291690/pyspark-logging)

#### Logging in foreach method
- [How to log in Apache Spark \- By](https://hackernoon.com/how-to-log-in-apache-spark-f4204fad78a#.j93k2ieu7)
- [Spark: Log's in foreachRdd when running on the cluster \- Hortonworks](https://community.hortonworks.com/questions/75314/spark-logs-in-foreachrdd-when-running-on-the-clust.html)
- [Alvin's Big Data Notebook : Distributed Logging in Spark App](http://alvincjin.blogspot.com/2016/08/distributed-logging-in-spark-app.html)

We cannot use `log4j` logger since the `log4j` is not serializable.


## Reference
* [How to Log in Apache Spark | MapR](https://mapr.com/blog/how-log-apache-spark/)
* [How to log in Apache Spark – Hacker Noon](https://hackernoon.com/how-to-log-in-apache-spark-f4204fad78a)
