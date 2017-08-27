---
title: JVM
---

## JVM


## Tips

### CodeCache is full
* [Why do I get message "CodeCache is full. Compiler has been disabled"? | Oracle Poonam Bajaj Blog](https://blogs.oracle.com/poonam/why-do-i-get-message-codecache-is-full-compiler-has-been-disabled)

javaのoptionで以下をつける。

* `-XX:-UseCodeCacheFlushing `
    * Disable Code Cash Flushing
* `-J-XX:ReservedCodeCacheSize`
    * Change size of CodeCascheSize

CodeCacheに伴うこの問題は、JDK8では解消されている。


### java.lang.OutOfMemoryError: PermGen spac
* [Permgen space – Plumbr](https://plumbr.eu/outofmemoryerror/permgen-space)
* [exception - Dealing with "java.lang.OutOfMemoryError: PermGen space" error - Stack Overflow](https://stackoverflow.com/questions/88235/dealing-with-java-lang-outofmemoryerror-permgen-space-error)
* [java - What are the Xms and Xmx parameters when starting JVMs? - Stack Overflow](https://stackoverflow.com/questions/14763079/what-are-the-xms-and-xmx-parameters-when-starting-jvms)
* [Java: PermGen はヒープの外 - sardineの日記](http://d.hatena.ne.jp/sardine/20100716/p2)

jvmのPermGenのmemory不足

* `-J-XX:MaxPermSize=1G`
    * memory size for Pem

必要であれば、下記のmemory sizeも変更する。

* `-Xmx2048m`
    * the maximum memory allocation pool for a Java Virtual Machine
* `-Xms256m`
    * the initial memory allocation pool




## Reference
