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
        * resources/
           * files to include in main jar here
        * scala/
           * main Scala sources
        * java/
           * main Java sources
    * test/
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

## Reference
* [sbt - The interactive build tool](https://www.scala-sbt.org/)
* [sbt/sbt: sbt, the interactive build tool](https://github.com/sbt/sbt)
