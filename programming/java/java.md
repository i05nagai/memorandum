---
title: java
---

## java
There are oracle SDK and open SDK

## Install

### oracle SDK
For ubuntu 16.04,

```
sudo apt-get install default-jre
sudo apt-get install default-jdk
# oracle jdk
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java8-installer
sudo apt-get install oracle-java9-installer
```

### open SDK
For ubuntu 16.04

```
# to automatically agree with license
echo debconf shared/accepted-oracle-license-v1-1 select true | \
  sudo debconf-set-selections
echo debconf shared/accepted-oracle-license-v1-1 seen true | \
  sudo debconf-set-selections
# install
apt-get install openjdk-8-jdk
```


## final
* referenceに対しては参照先の変更は可能

## Dependecy injection
* [Using dependency injection in Java - Introduction - Tutorial](http://www.vogella.com/tutorials/DependencyInjection/article.html)
* [Inversion of Control Containers and the Dependency Injection pattern](https://martinfowler.com/articles/injection.html)
* [javax.inject (Java EE 6 )](https://docs.oracle.com/javaee/6/api/javax/inject/package-summary.html)

classの中でinterfaceを使っているときに、 interfaceの実装を注入するという意味。
注入の仕方として、xmlを使ったり設定ファイルや特別なclassなどから行うので、DIという特別な名前が付いている。
interfaceを使ってかくという点では、ただのOOPの概念なので新しくはない。

依存しているinterfaceはlocalの場合はcomponent, remoteの場合はserviceと呼ばれることもある。

## Design pattern
* [iluwatar/java-design-patterns: Design patterns implemented in Java](https://github.com/iluwatar/java-design-patterns)

## Return List or ArrayList
* [java - Should i return List or ArrayList - Stack Overflow](https://stackoverflow.com/questions/10328658/should-i-return-list-or-arraylist)

should return List

## Call private methods
* [java - Any way to Invoke a private method? - Stack Overflow](https://stackoverflow.com/questions/880365/any-way-to-invoke-a-private-method)

Usage

```java
invokePrivateMethod(targetClass, "methodName", 2, arg1, arg2);
```

```java
  public static Object invokePrivateMethod(
      Object obj, String methodName, int paramCount, Object... params) {

    Object[] parameters = new Object[paramCount];
    Class<?>[] classArray = new Class<?>[paramCount];
    for (int i = 0; i < paramCount; i++) {
      parameters[i] = params[i];
      classArray[i] = params[i].getClass();
    }

    Object requiredObj = null;
    try {
      Method method = obj.getClass().getDeclaredMethod(methodName, classArray);
      // force public
      final boolean isAccessible = method.isAccessible();
      method.setAccessible(true);
      requiredObj = method.invoke(obj, params);
      // back to original scope
      method.setAccessible(isAccessible);
    } catch (NoSuchMethodException e) {
      e.printStackTrace();
    } catch (IllegalArgumentException e) {
      e.printStackTrace();
    } catch (IllegalAccessException e) {
      e.printStackTrace();
    } catch (InvocationTargetException e) {
      e.printStackTrace();
    }

    return requiredObj;
  }
```

```kotlin
fun invokePrivateMethod(
        target: Any,
        methodName: String,
        vararg params: Any): Any {
    val targetClass: Class<Any> = target.javaClass
    val paramsClass: Array<Class<Any>> = params.map{ elem -> elem.javaClass}.toTypedArray()

    val targetMethod: Method = targetClass.getDeclaredMethod(methodName, paramsClass)
    val isAccessible: Boolean = targetMethod.isAccessible
    targetMethod.isAccessible = true
    val returnValue: Any = targetMethod.invoke(target, *params)
    targetMethod.isAccessible = isAccessible
    return returnValue
}
```

## Call kotlin code
* [Calling Kotlin from Java - Kotlin Programming Language](https://kotlinlang.org/docs/reference/java-to-kotlin-interop.html)

呼び出したいobjectのmethodには、`@JvmStatic`をつける。

```kotlin
object Obj {
    @JvmStatic fun foo() {}
    fun bar() {}
}
```

## final variables
* [Chapter 4. Types, Values, and Variables](https://docs.oracle.com/javase/specs/jls/se8/html/jls-4.html#jls-4.12.4)
* [coding standards - Excessive use "final" keyword in Java - Software Engineering Stack Exchange](https://softwareengineering.stackexchange.com/questions/98691/excessive-use-final-keyword-in-java)

## Date
* [Javaで日時を扱う（Java8） - kurukuru-papaのブログ](http://kurukurupapa.hatenablog.com/entry/2016/05/22/213011)


## Call kotlin code
[Calling Kotlin from Java - Kotlin Programming Language](https://kotlinlang.org/docs/reference/java-to-kotlin-interop.html)

呼び出したいobjectのmethodには、`@JvmStatic`をつける。

```kotlin
object Obj {
    @JvmStatic fun foo() {}
    fun bar() {}
}
```

#### GC allocation failure
* [garbage collection - Java GC (Allocation Failure) - Stack Overflow](https://stackoverflow.com/questions/28342736/java-gc-allocation-failure)

```
2018-05-22T02:31:33.064+0000: [GC (Allocation Failure) 2018-05-22T02:31:33.064+0000: [ParNew: 77824K->8202K(77824K), 0.0035546 secs] 1837015K->1768418K(3009812K), 0.0036089 secs] [Times: user=0.03 sys=0.00, real=0.00 secs] 
```

## JVM monitoring
* https://stackoverflow.com/questions/1262328/how-is-the-java-memory-pool-divided

* Heap memory
    * Eden Space
        * The pool from which memory is initially allocated for most objects.
    * Survivor Space
        * The pool containing objects that have survived the garbage collection of the Eden space.
    * Tenured Generation or Old Gen
        * The pool containing objects that have existed for some time in the survivor space.
* Non-heap memory
    * Permanent Generation
    * Code Cache
* Java Heap Memory

## Options
* `-Djava.security.egd=`


## Java Key Store
- [Difference between \.keystore file and \.jks file \- Stack Overflow](https://stackoverflow.com/questions/8985685/difference-between-keystore-file-and-jks-file)
- [KeyStore \(Java Platform SE 6\)](https://docs.oracle.com/javase/6/docs/api/java/security/KeyStore.html)

- extension is either `jks` or `keystore`

## Syncrhonized
- [Synchronized Methods \(The Java™ Tutorials > Essential Classes > Concurrency\)](https://docs.oracle.com/javase/tutorial/essential/concurrency/syncmeth.html)

- First, it is not possible for two invocations of synchronized methods on the same object to interleave. When one thread is executing a synchronized method for an object, all other threads that invoke synchronized methods for the same object block (suspend execution) until the first thread is done with the object.
- Second, when a synchronized method exits, it automatically establishes a happens-before relationship with any subsequent invocation of a synchronized method for the same object. This guarantees that changes to the state of the object are visible to all threads.

[Java Synchronized Blocks](http://tutorials.jenkov.com/java-concurrency/synchronized.html)

- synchronized instance method
    - Only one thread per instance can execute inside a synchronized instance method. If more than one instance exist, then one thread at a time can execute inside a synchronized instance method per instance. One thread per instance.
- synchronized static method
    - Synchronized static methods are synchronized on the class object of the class the synchronized static method belongs to. Since only one class object exists in the Java VM per class, only one thread can execute inside a static synchronized method in the same class.
- synchronized block

## Reference
* [Java 8: No more loops](http://www.deadcoderising.com/java-8-no-more-loops/)
* [jjugccc2018 app review postmortem](https://www.slideshare.net/tamrin69/jjugccc2018-app-review-postmortem)
* [How To Install Java with Apt\-Get on Ubuntu 16\.04 \| DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-get-on-ubuntu-16-04)
