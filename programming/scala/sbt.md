---
title: sbt
---

## sbt
The interactive build tool.

## Install
Before isntall you need to java 1.8.

For OSX,

```
brew install sbt
```

For ubuntu 16.04,

```
echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823
sudo apt-get update
sudo apt-get install sbt
```


## Directory structure
`Base directory` is the directory containing the project.
In usual, the directory containing `build.sbt`.


* `/build.sbt`
    * sbt build definition files 
    * any files `*.sbt` in base directory
* `project/`
    * `Dependencies.scala`
* `target/`
    * Generated files (compiled classes, packaged jars, managed files, caches, and documentation) will be written to the target directory by default.
* `src/`
    * `main/`
        * `resources/`
           * files to include in main jar here
        * `scala/`
           * main Scala sources
        * `java/`
           * main Java sources
    * `test/`
        * resources
           * files to include in test jar here
        * scala/
           * test Scala sources
        * java/
           * test Java sources


## Library
* [sbt Reference Manual — Library Management](https://www.scala-sbt.org/1.x/docs/Library-Management.html)

```sbt

val scalaTestVersion = "3.0.1"
libraryDependencies ++= Seq(
  "org.scalatest" %% "scalatest" % scalaTestVersion % "test",
)
```

## Testing
* [sbt Reference Manual — Testing](https://www.scala-sbt.org/1.x/docs/Testing.html)

## Error

#### sbt-assembly: deduplication found error
See https://github.com/sbt/sbt-assembly#merge-strategy
See https://github.com/sbt/sbt-assembly#excluding-jars-and-files
See https://stackoverflow.com/questions/25144484/sbt-assembly-deduplication-found-error
See https://github.com/sbt/sbt-assembly/issues/146

```
assemblyMergeStrategy in assembly := {
 case PathList("META-INF", _*) => MergeStrategy.discard
 case _                        => MergeStrategy.first
}
```

```
java.lang.RuntimeException: deduplicate: different file contents found in the following:
org.eclipse.jetty.orbit/javax.transaction/orbits/javax.transaction-1.1.1.v201105210645.jar:META-INF/ECLIPSEF.RSA
org.eclipse.jetty.orbit/javax.servlet/orbits/javax.servlet-3.0.0.v201112011016.jar:META-INF/ECLIPSEF.RSA
org.eclipse.jetty.orbit/javax.mail.glassfish/orbits/javax.mail.glassfish-1.4.1.v201005082020.jar:META-INF/ECLIPSEF.RSA
org.eclipse.jetty.orbit/javax.activation/orbits/javax.activation-1.1.0.v201105071233.jar:META-INF/ECLIPSEF.RSA
```



## Reference
* [sbt - The interactive build tool](https://www.scala-sbt.org/)
* [sbt/sbt: sbt, the interactive build tool](https://github.com/sbt/sbt)

