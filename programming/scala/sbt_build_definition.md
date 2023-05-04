---
title: sbt build definition
---

## sbt build definition
A build definition is defined in build.sbt, and it consists of a set of projects (of type Project). Because the term project can be ambiguous, we often call it a subproject in this guide.
`build.sbt`


Keys

- SettingKey[T]: a key for a value evaluated only once (the value is computed when loading the subproject, and kept around).
- TaskKey[T]: a key for a value, called a task, that is evaluated each time it’s referred to (similarly to a scala function), potentially with side effects.
- InputKey[T]: a key for a task that has command line arguments as input. Check out Input Tasks for more details.

## Configuration

Revolvers

https://www.scala-sbt.org/1.x/docs/Resolvers.html

```
resolvers ++= Seq(
    "Sonatype OSS Snapshots" at "https://oss.sonatype.org/content/repositories/snapshots",
    
)
```

libraryDependencies

https://www.scala-sbt.org/1.x/docs/Library-Dependencies.html
The `%` methods create ModuleID objects from strings, then you add those ModuleID to libraryDependencies.
If you use organization `%%` moduleName `%` version rather than organization `%` moduleName `%` version (the difference is the double %% after the organization), sbt will add your project’s binary Scala version to the artifact name.

```
libraryDependencies ++= Seq(
    "org.apache.derby" % "derby" % "10.4.1.3",
)
```

## Reference
* [sbt Reference Manual — Build definition](https://www.scala-sbt.org/1.x/docs/Basic-Def.html)
