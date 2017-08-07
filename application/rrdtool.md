---
title: RRDTool
---

## RRDTool

### rrdgraph
* [RRDtool - rrdgraph](https://oss.oetiker.ch/rrdtool/doc/rrdgraph.en.html)

```
rrdtool graph|graphv filename [option ...] [data definition ...] [data calculation ...] [variable definition ...] [graph element ...] [print element ...]
```

人間の読める形にRRDを加工する。
以下の形式が使える

* `png`
* `svg`
* `eps`


option

* `[-s|--start time] [-e|--end time] [-S|--step seconds]`
    * defaultは1日前から現在まで
    * stepは1pixelが表す時間
    * 1時間1pixcelにしたいなら3600を指定

Graph描画に利用するdataの指定。
[RRDtool - rrdgraph_data](https://oss.oetiker.ch/rrdtool/doc/rrdgraph_data.en.html)


* `DEF:<vname>=<rrdfile>:<ds-name>:<CF>[:step=<step>][:start=<time>][:end=<time>][:reduce=<CF>][:daemon=<address>]`
    * RDD fileから取得するdataを指定
    * vritual name `vname`はscriptや他のoptionで参照するために、dataの別名
    * `rrdfile`はrrdのfile名
    * `ds`はData Sourceの名前
* `VDEF:vname=RPN expression`
    * rpn expressionからデータを加工する
    * 今のところaggregationの処理しか対応していない
* `CDEF:vname=rpn-expression`
    * rpn expressionに従って新しくdataを作成する
    * rrd fileには出力されなず、in memoryのデータ


rpn expressionはReverse Polish Notationの略。
データの加工方法を、指定するための記法。
[RRDtool - rrdgraph_rpn](https://oss.oetiker.ch/rrdtool/doc/rrdgraph_rpn.en.html)


### rrdxport
* [RRDtool - rrdxport](https://oss.oetiker.ch/rrdtool/doc/rrdxport.en.html)

```
rrdtool xport [-s|--start seconds] [-e|--end seconds] [-m|--maxrows rows] [--step value] [--json] [--enumds] [--daemon|-d address] [DEF:vname=rrd:ds-name:CF] [CDEF:vname=rpn-expression] [XPORT:vname[:legend]]
```

RRDを別のformatにexportする。
`json`, `xml`が利用可能で、defaultは`xml`になっている。

option

* `--json`
* `DEF:vname=rrdfile:ds-name:CF[:step=step][:start=time][:end=time]`
    * 
* `CDEF:vname=rpn-expression`
* `XPORT:vname[:legend]`
    * 少なくとも1つ指定が必要
    * 


```
rrdtool xport \
      --start now-1h --end now \
      DEF:xx=host-inout.lo.rrd:output:AVERAGE \
      DEF:yy=host-inout.lo.rrd:input:AVERAGE \
      CDEF:aa=xx,yy,+,8,* \
      XPORT:xx:"out bytes" \
      XPORT:aa:"in and out bits"
```

結果以下のような感じになる。

```xml
  <meta>
    <start>1020611700</start>
    <step>300</step>
    <end>1020615600</end>
    <rows>14</rows>
    <columns>2</columns>
    <legend>
      <entry>out bytes</entry>
      <entry>in and out bits</entry>
    </legend>
  </meta>
  <data>
    <row><t>1020611700</t><v>3.4000000000e+00</v><v>5.4400000000e+01</v></row>
    <row><t>1020612000</t><v>3.4000000000e+00</v><v>5.4400000000e+01</v></row>
    <row><t>1020612300</t><v>3.4000000000e+00</v><v>5.4400000000e+01</v></row>
    <row><t>1020612600</t><v>3.4113333333e+00</v><v>5.4581333333e+01</v></row>
    <row><t>1020612900</t><v>3.4000000000e+00</v><v>5.4400000000e+01</v></row>
    <row><t>1020613200</t><v>3.4000000000e+00</v><v>5.4400000000e+01</v></row>
    <row><t>1020613500</t><v>3.4000000000e+00</v><v>5.4400000000e+01</v></row>
    <row><t>1020613800</t><v>3.4000000000e+00</v><v>5.4400000000e+01</v></row>
    <row><t>1020614100</t><v>3.4000000000e+00</v><v>5.4400000000e+01</v></row>
    <row><t>1020614400</t><v>3.4000000000e+00</v><v>5.4400000000e+01</v></row>
    <row><t>1020614700</t><v>3.7333333333e+00</v><v>5.9733333333e+01</v></row>
    <row><t>1020615000</t><v>3.4000000000e+00</v><v>5.4400000000e+01</v></row>
    <row><t>1020615300</t><v>3.4000000000e+00</v><v>5.4400000000e+01</v></row>
    <row><t>1020615600</t><v>NaN</v><v>NaN</v></row>
  </data>
```

### rrdgraph_data
* [RRDtool - rrdgraph_data](https://oss.oetiker.ch/rrdtool/doc/rrdgraph_data.en.html)


### rrdinfo
* [RRDtool - rrdinfo](https://oss.oetiker.ch/rrdtool/doc/rrdinfo.en.html)

rrdの情報を取得。

```
rrdtool info filename [--daemon|-d address [--noflush|-F]]
```

結果は以下のような感じでかえる。
dsの`[]`の中は、data source名で、ここに記載されているものが指定可能。

```
 filename = "random.rrd"
 rrd_version = "0001"
 step = 300
 last_update = 955892996
 header_size = 2872
 ds[a].type = "GAUGE"
 ds[a].minimal_heartbeat = 600
 ds[a].min = NaN
 ds[a].max = NaN
 ds[a].last_ds = "UNKN"
 ds[a].value = 2.1824421548e+04
 ds[a].unknown_sec = 0
 ds[b].type = "GAUGE"
 ds[b].minimal_heartbeat = 600
 ds[b].min = NaN
 ds[b].max = NaN
 ds[b].last_ds = "UNKN"
 ds[b].value = 3.9620838224e+03
 ds[b].unknown_sec = 0
 rra[0].cf = "AVERAGE"
 rra[0].pdp_per_row = 1
 rra[0].cdp_prep[0].value = nan
 rra[0].cdp_prep[0].unknown_datapoints = 0
 rra[0].cdp_prep[1].value = nan
 rra[0].cdp_prep[1].unknown_datapoints = 0
```

### rrdfetch
* [RRDtool - rrdfetch](https://oss.oetiker.ch/rrdtool/doc/rrdfetch.en.html)

graph commandで内部的にdataを取得するために利用されるcommandである。

```
rrdtool fetch filename CF [--resolution|-r resolution] [--start|-s start] [--end|-e end] [--align-start|-a] [--daemon|-d address]
```

* `CF`
    * consolidation function
    * `AVERAGE,MIN,MAX,LAST`


## Reference
