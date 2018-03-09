---
title: java
---

## java

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


## Call kotlin code
[Calling Kotlin from Java - Kotlin Programming Language](https://kotlinlang.org/docs/reference/java-to-kotlin-interop.html)

呼び出したいobjectのmethodには、`@JvmStatic`をつける。

```kotlin
object Obj {
    @JvmStatic fun foo() {}
    fun bar() {}
}
```

## Reference
* [Java 8: No more loops](http://www.deadcoderising.com/java-8-no-more-loops/)
