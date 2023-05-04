---
title: sbt-assembly
---

## sbt-assembly


## Merge strategy
- https://github.com/sbt/sbt-assembly#merge-strategy
- https://www.oracle.com/de/corporate/features/understanding-java-9-modules.html


```sbt
assembly / assemblyMergeStrategy := {
  case PathList(ps @ _*) if ps.last == "module-info.class" => MergeStrategy.first
  case x => val oldStrategy = (assembly / assemblyMergeStrategy).value oldStrategy(x)
}
```

## Reference
- https://github.com/sbt/sbt-assembly#excluding-jars-and-files
