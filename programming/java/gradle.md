---
title: Gradle
---

## Gradle
以下のguideが入門としてわかりやすい。

[Gradle | Guides](https://gradle.org/guides/)


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

For Ubuntu,

```

```

## Usage

```
gradle wrapper
```

以下のfileが作成される。

```
.
├── build.gradle
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

## CLI

```
gradle [options]
```

* `--profiler`
    * build時のprofiling
* `--scan`
    * build時のprofiling


## Reference
* [Gradle DSL Version 4.4.1](https://docs.gradle.org/current/dsl/)
* [Gradle 4.4.1 Release Notes](https://docs.gradle.org/current/release-notes.html)
* [Gradle：ビルドスクリプトの基本 - Qiita](https://qiita.com/shoma2da/items/367d0682a1b8c91f5531)
* [Gradle wrapper のバージョン更新についてのメモ - Qiita](https://qiita.com/nobuoka/items/09cbdcd4716b930abdc4)
