---
title: checkstyle
---

## checkstyle


## with Maven
[Apache Maven Checkstyle Plugin – Usage](https://maven.apache.org/plugins/maven-checkstyle-plugin/usage.html)

In `pom.xml`, the below confiugration needs to be added to validate the style before building package.
`checkstyle-result.xml` file will be generated under `target` dir.

```xml
 <plugin>
   <groupId>org.apache.maven.plugins</groupId>
   <artifactId>maven-checkstyle-plugin</artifactId>
   <version>3.1.1</version>
   <configuration>
     <configLocation>checkstyle.xml</configLocation>
     <encoding>UTF-8</encoding>
     <consoleOutput>true</consoleOutput>
     <failsOnError>true</failsOnError>
     <linkXRef>false</linkXRef>
   </configuration>
   <executions>
     <execution>
       <id>validate</id>
       <phase>validate</phase>
       <goals>
         <goal>check</goal>
       </goals>
     </execution>
   </executions>
 </plugin>
```

## Reference
- [checkstyle – Checkstyle 8\.31](https://checkstyle.sourceforge.io/)
- [checkstyle/checkstyle: Checkstyle is a development tool to help programmers write Java code that adheres to a coding standard\. By default it supports the Google Java Style Guide and Sun Code Conventions, but is highly configurable\. It can be invoked with an ANT task and a command line program\.](https://github.com/checkstyle/checkstyle)
