## Apache spark

## Cluster Mode Overview
* [Cluster Mode Overview - Spark 2.1.1 Documentation](https://spark.apache.org/docs/latest/cluster-overview.html)

## Components

<div style="text-align: center">
    <img src="https://spark.apache.org/docs/latest/img/cluster-overview.png">
</div>

1. それぞれのapplicationはそれぞれexecutorのprocessをもつ
    * applicationが独立するので、ここのapplicationのschedulingとexecutionの管理のみすればよい
    * そのかわりdataはapplication間で共有されない
    * 共有する場合は別の場所に出力する
2. sparkはcluster managerについては関与しない
3. driver programはexecutorからの接続をうけつけるようになっている必要がある
    * worker nodeからnetworkが見えている必要がある
4. driverがtaskのschedulingをするので、taskの実行者のexecutorとは同じLAN上に合ったほうがよい。

## Reference
* [Making Apache Spark Testing Easy with Spark Testing Base - Cloudera Engineering Blog](http://blog.cloudera.com/blog/2015/09/making-apache-spark-testing-easy-with-spark-testing-base/)
