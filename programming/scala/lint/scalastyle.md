---
title: scalastyle
---

## scalastyle


## With sbt
* [Scalastyle \- SBT plugin](http://www.scalastyle.org/sbt.html)

Add the following line to sbt file for sbt-plugins. For example, `project/plugins.sbt`.

```
addSbtPlugin("org.scalastyle" %% "scalastyle-sbt-plugin" % "1.0.0")
```

Then run

```
sbt update
```

The following command generate configuration `scalastyle-config.xml` for `scalastyle` in current directory.

```
sbt scalastyleGenerateConfig
```

After configuration file generated,

```
# for main/
sbt scalastyle
# for test/
sbt test:scalastyle
```

The result is written in `target/scalastyle-result.xml`.

## CLI

## Usage

## Configuration
* [spark/scalastyle\-config\.xml at master · apache/spark](https://github.com/apache/spark/blob/master/scalastyle-config.xml)
* [finch/scalastyle\-config\.xml at master · finagle/finch](https://github.com/finagle/finch/blob/master/scalastyle-config.xml)

## Reference
* [scalastyle/scalastyle: scalastyle](https://github.com/scalastyle/scalastyle)
