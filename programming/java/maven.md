---
title: Maven
---

## Maven


## CLI

```
mvn
```

Install dependency

```
mvn install:install-file -Dfile=non-maven-proj.jar -DgroupId=some.group -DartifactId=non-maven-proj -Dversion=1 -Dpackaging=jar
```


## Repository
- local
    - [Maven – Guide to installing 3rd party JARs](https://maven.apache.org/guides/mini/guide-3rd-party-jars-local.html)

## pom

- `groupId`
- `artifactId`
- `version`


```
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.12</version>
      <type>jar</type>
      <scope>test</scope>
      <optional>true</optional>
    </dependency>
    ...
  </dependencies>
```

- `type`
    * this deafult to `jar`
- `scope`
    - This element refers to the classpath of the task at hand (compiling and runtime, testing, etc.) as well as how to limit the transitivity of a dependency.
- `optional`
    - True if only part of the code depends on the dependency.
    - Some functionality can be provided without this dependency

## Distributiong management

## settings.yaml
There are two locations where a `settings.xml` file may live:

- The Maven install: `${maven.home}/conf/settings.xml`
- A user’s install: `${user.home}/.m2/settings.xml`

settings.xml contains system and/or user configuration, while the pom.xml contains project information. All build configuration ends up in the pom.xml.


#### Passing creddentials
Credentials needs to be specified in `settings.xml`. You can pass it by CLI

```
<settings>
    <servers>
        <server>
            <id>${repo.id}</id>
            <username>${repo.login}</username>
            <password>${repo.pwd}</password>
        </server>
    </servers>
</settings>  
```

```
mvn -Drepo.id=myRepo -Drepo.login=someUser -Drepo.pwd=somePassword clean install
```


#### profiles
[Maven – Settings Reference](https://maven.apache.org/settings.html#profiles)


## Goals
Default goals

- `deploy:deploy`
    - deploy artifact to repository


## Reference
- [Maven – POM Reference](https://maven.apache.org/pom.html)
