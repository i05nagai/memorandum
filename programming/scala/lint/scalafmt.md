---
title: scalafmt
---

## scalafmt

## Install

with sbt,

```
val scalafmtVersion = "3.6.1"
addSbtPlugin("org.scalameta" % "sbt-scalafmt" % scalafmtVersion)
```

## Tasks

- myproject/scalafmt
    - Format main sources of myproject project
- myproject/test:scalafmt
    Format test sources of myproject project
- scalafmtCheck
    - Check if the scala sources under the project have been formatted.
- scalafmtSbtx
    - Format *.sbt and project/*.scala files.
- scalafmtSbtCheck
    - Check if the files have been formatted by scalafmtSbt.
- scalafmtOnly <file>...
    - Format specified files listed.
- scalafmtAll or scalafmtCheckAll
    - Execute the scalafmt or scalafmtCheck task for all configurations in which it is enabled (since v2.0.0-RC5)

## Configuration
https://scalameta.org/scalafmt/docs/configuration.html

## Reference
- https://scalameta.org/scalafmt/docs/installation.html
