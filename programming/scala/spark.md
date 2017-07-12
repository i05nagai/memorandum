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

## Tuning Spark
* [Tuning - Spark 2.1.1 Documentation](https://spark.apache.org/docs/latest/tuning.html)

### Data Serialization
Sparkのserializationの最初のstep

* Java Serialization
    * defaultで利用される
* java.io.Serialization
* java.io.Externalizable
    * serializationのperformanceはこのclassを拡張することでできる
* Kryo serialization
    * javaのserializationより高速でcompactになるが(10xほど) Serializable型を全てsupportしているわけではないので、自分で調整が必要な場合がある

SparkConfで設定できる。

```
conf.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
```

serializeはworker nodeのshufflingだけでなくRDDのdiskへの書き込み時にも利用される。
Kryoがdefaultでない理由はserializeのためにobjectの登録作業があるからである。
network-intesive applicationでは使うことが推奨される。

### Memory Tuning
memory tuningの3つの確認事項

1. objectが利用しているmemoryの料
2. objectへのaccessのcost
3. garbage collectioのoverhead

Javaのobjectはdefaultでは高速にアクセス可能だが、fieldの実際のデータの2-5倍のメモリを消費する
その主な理由は以下の3つになる。

1. それぞれのjava obejctは16bytesの自身へのclassへのpointerなどの情報を持つObject headerを持っている。
    * 例えば、intなどのデータの場合はobject headerの方が圧倒的に大きくなる
2. javaのstringは実際の文字列のデータより40bytes余分にメモリを消費する
    * stringはarray of charで、配列はサイズなどの情報をもつ
    * UTF-16なので、全ての文字列は2bytes消費する
    * 10文字で60bytes
3. 

### Tuning Data Structure
pointer basedのdata構造やwrapper objectのようなOverheadのあるjava objectを使うのをやめることで、memoryの消費を減らすことができる。
いくつか方法がある。

1. JavaやScalaのcollection (HashMapなど)ではなくprimitive typeやobjectの配列を利用する
2. 小さいobjectやpointerがnestした構造をさける
3. keyとして文字列ではなく、数値のIDを使う
4. 32GBより少ないメモリを使っている場合は、JVM flag `-XX:+UseCompressedOops`を使う。

### Serialized RDD Storage
tuningしてもdataを保存するのに大きすぎる場合はserializeして保存する方法がある。
serializeしてpartitionを1つの巨大なbinary bytes arraに変換して保存できる。
`persist`コマンドで`MEMORY_ONLY_SER`などを指定すれば良い。

## Reference
* [Making Apache Spark Testing Easy with Spark Testing Base - Cloudera Engineering Blog](http://blog.cloudera.com/blog/2015/09/making-apache-spark-testing-easy-with-spark-testing-base/)
