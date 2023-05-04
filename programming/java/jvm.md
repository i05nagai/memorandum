---
title: JVM
---

## JVM

## Direct buffer
Java NIO APIs use ByteBuffers as the source and destination of I/O calls, and come in two flavours:

- Heap Byte Buffer (wrap a byte[] array, allocated in the garbage collected Java heap)
- Direct Byte Buffer (wrap memory allocated outside the Java heap )

Since only "native" memory can be passed to operating system calls, so it won't be moved by the garbage collector, it means that when you use a heap ByteBuffer for I/O, it is copied into a temporary direct ByteBuffer. The JDK caches one temporary buffer per thread, without any memory limits (i.e. an unbounded cache). As a result, if you call I/O methods with large heap ByteBuffers from multiple threads, your process can use a huge amount of additional native memory.

## Young generation
The young generation is the place where all the new objects are created. When the young generation is filled, garbage collection is performed. 
This garbage collection is called Minor GC.

## Old generation
https://www.digitalocean.com/community/tutorials/java-jvm-memory-model-memory-management-in-java

Old Generation memory contains the objects that are long-lived and survived after many rounds of Minor GC. 
Usually, garbage collection is performed in Old Generation memory when it’s full. 
Old Generation Garbage Collection is called Major GC and usually takes a longer time.


## Permgen

- PermGen (Permanent Generation) is a special heap space separated from the main memory heap.
- The JVM keeps track of loaded class metadata in the PermGen. 
- the JVM stores all the static content in this memory section. This includes all the static methods, primitive variables, and references to the static objects.
- it contains data about bytecode, names, and JIT information
- The default maximum memory size for 32-bit JVM is 64 MB and 82 MB for the 64-bit version.
- With its limited memory size, PermGen is involved in generating the famous OutOfMemoryError. Simply put, the class loaders weren't garbage collected properly and, as a result, generated a memory leak.

## Metaspace
https://www.baeldung.com/java-permgen-metaspace
https://stackoverflow.com/questions/39675406/difference-between-metaspace-and-native-memory-in-java

- it has replaced the older PermGen memory space.
- Metaspace grows automatically by default.
- The garbage collector now automatically triggers the cleaning of the dead classes once the class metadata usage reaches its maximum metaspace size.

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
