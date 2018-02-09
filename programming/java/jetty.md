---
title: Jetty
---

## Jetty
Eclipse Jetty is a Java HTTP (Web) server and Java Servlet container.


## Start jetty
* [Enable remote debugging](https://www.eclipse.org/jetty/documentation/9.3.x/enable-remote-debugging.html)

設定はcli argumentsで渡すか、`start.ini`で渡す。

Command Line 

```
 $ java -Xdebug -agentlib:jdwp=transport=dt_socket,address=9999,server=y,suspend=n -jar start.jar
```

start.ini

```ini
--exec
-Xdebug
-agentlib:jdwp=transport=dt_socket,address=9999,server=y,suspend=n
```

```
$ java -jar start.jar
```


## Debug
* [Debugger failed to attach: handshake failed - received  #257 · akhikhl/gretty](https://github.com/akhikhl/gretty/issues/257)
    * 以下のようなerrroがでる場合
    * jettyのdebugger用のportにaccessしている
    * webappとdebuggerのportは別

```
Debugger failed to attach: handshake failed - received >POST /wlcApp/l< - expected >JDWP-Handshake<
````

## Reference
* [Jetty (web server) - Wikipedia](https://en.wikipedia.org/wiki/Jetty_(web_server))
