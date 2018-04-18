---
title: Java Flight Recorder
---

## Java Flight Recorder
java profiler.

## Usage

## CLI

### From java command

```
$ java -XX:+UnlockCommercialFeatures -XX:+FlightRecorder -XX:StartFlightRecording=duration=60s,filename=/tmp/recording.jfr MyAp
```

### jcmd
実行中のjava process のprofilingができる。
ただし、`-XX:+UnlockCommercialFeatures`, `-XX:+FlightRecorder`が指定されている必要がある。


```
$ jcmd 5368 JFR.start duration=60s filename=/tmp/recording.jfr
```


## Reference
* [Java Flight Recorder(JFR)について調べてみた - Qiita](https://qiita.com/ohsoko-hiroshi/items/66825c8f3e2fdbe697c4)
