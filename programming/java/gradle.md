---
title: Gradle
---

## Gradle
以下のguideが入門としてわかりやすい。

[Gradle | Guides](https://gradle.org/guides/)


## configuration
- [Gradle: build\.gradle vs\. settings\.gradle vs\. gradle\.properties \| Baeldung](https://www.baeldung.com/gradle-build-settings-properties)

* `build.gradle`
    * この中で記述したcodeは [Project - Gradle DSL Version 4.4.1](https://docs.gradle.org/current/dsl/org.gradle.api.Project.html)にdelegateされる
    * Project classのmethodを確認する
    * 以下のsample codeでは、
        * `Project.apply(colusure)`
        * `Project.configure()`
        * `Project.buildscript`
            * `dependencies`
                * getDependencyにdelegate
            * https://docs.gradle.org/current/javadoc/org/gradle/api/initialization/dsl/ScriptHandler.html
* `settings.gradle`
* `gradle.properties`
    * the file consists of key value pair
    * e.g.
        * `org.gradle.caching=(true,false)`
        * `org.gradle.logging.level=(quiet,warn,lifecycle,info,debug)`
        * `org.gradle.jvmargs=-Xmx2g -XX:MaxPermSize=256m -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8`


```kotlin
// build.gradle
apply {
    plugin("org.junit.platform.gradle.plugin")
}

configure {
    filters {
        engines {
            include("spek")
        }
    }
}
```

## Install
For OSX

```
brew install gradle
```

## Usage

```
gradle init
```

Create a basic files for Gradle interactively.


```
gradle wrapper
```

以下のfileが作成される。

```
.
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradlew          
└── gradlew.bat    
```

taskの一覧

```
./gradlew tasks
```

設定値の一覧を見る

```
./gradlew properties
```

`JavaCompile`のtaskk時にoptionを付与できる。

```
tasks.withType(JavaCompile) {
    options.compilerArgs += ["-Xdoclint:none", "-Xlint:none", "-nowarn"]
}
```

## Build scripts

* `allprojects { }`
    * Configures this project and each of its sub-projects.
* `artifacts { }`
    * Configures the published artifacts for this project.
* `buildscript { }`
    * Configures the build script classpath for this project.
* `configurations { }`
    * Configures the dependency configurations for this project.
* `dependencies { }`
    * Configures the dependencies for this project.
    * [DependencyHandler - Gradle DSL Version 4.4.1](https://docs.gradle.org/current/dsl/org.gradle.api.artifacts.dsl.DependencyHandler.html)
* `repositories { }`
    * Configures the repositories for this project.
* `sourceSets { }`
    * Configures the source sets of this project.
* `subprojects { }`
    * Configures the sub-projects of this project.
* `publishing { }`
    * Configures the PublishingExtension added by the publishing plugin.

taskの作成

```
task zip(type: Zip) {
    from 'src'
}
```

## Syntax
- compile
- implementation

## kotlin

```
my-kotlin-library
├── build.gradle.kts
└── src
    ├── main
    │   └── kotlin
    │       └── org
    │           └── example
    │               └── MyLibrary.kt
    └── test
        └── kotlin
            └── org
                └── example
                    └── MyLibraryTest.kt
```



## kotlin-dsl
* [gradle/kotlin-dsl: Kotlin language support for Gradle build scripts](https://github.com/gradle/kotlin-dsl)
* [kotlin-examples/gradle at master · JetBrains/kotlin-examples](https://github.com/JetBrains/kotlin-examples/tree/master/gradle)
* [RepositoryHandler - Gradle DSL Version 4.4.1](https://docs.gradle.org/current/dsl/org.gradle.api.artifacts.dsl.RepositoryHandler.html)


* build script
    * `build.gradle.kts`
    * `settings.gradle.kts`

```kotlin
buildscript {
  ext.kotlin_version = '1.1.4-3'
  repositories {
    mavenCentral()
  }
  dependencies {
    classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
  }
}
```

## Repository
- [Declaring repositories](https://docs.gradle.org/current/userguide/declaring_repositories.html)

```
// require at least 1 repository to resolve dependency
repositories {
    mavenCentral()
}
```

## Dependency
- [Managing Dependencies of JVM Projects](https://docs.gradle.org/current/userguide/dependency_management_for_java_projects.html)

## junit5 with gradle
- [Using JUnit 5 with Gradle \| Baeldung](https://www.baeldung.com/junit-5-gradle)
- [Test \- Gradle DSL Version 6\.3](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.testing.Test.html)

## Pass arguments
- [How to pass arguments from command line to gradle \- Stack Overflow](https://stackoverflow.com/questions/11696521/how-to-pass-arguments-from-command-line-to-gradle)

```
run {
    if ( project.hasProperty("appArgsWhatEverIWant") ) {
        args Eval.me(appArgsWhatEverIWant)
    }
}
```

```
gradle run  -PappArgsWhatEverIWant="['localhost','8080']"
```

Or

```
gradle run ./gradlew run --args='This string will be passed into my.App#main arguments'
# space is important
gradle run ./gradlew run --args=' --p1=a --p2=a2'
```


## CLI

```
gradle [options]
```

* `--profiler`
    * build時のprofiling
* `--scan`
    * build時のprofiling

```
gradle init
```

Create project template

## Reference
* [Gradle DSL Version 4.4.1](https://docs.gradle.org/current/dsl/)
* [Gradle 4.4.1 Release Notes](https://docs.gradle.org/current/release-notes.html)
* [Gradle：ビルドスクリプトの基本 - Qiita](https://qiita.com/shoma2da/items/367d0682a1b8c91f5531)
* [Gradle wrapper のバージョン更新についてのメモ - Qiita](https://qiita.com/nobuoka/items/09cbdcd4716b930abdc4)
* [townsfolk/gradle\-templates: A gradle project templates plugin](https://github.com/townsfolk/gradle-templates)
