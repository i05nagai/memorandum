---
title: Kotlin
---

## Kotlin

## Annotation
* `@field:AnnotateClass`
    * annotate java field
* `@get:AnnotateClass`
    * annotate java getter
* `@param:AnnotateClass`
    * annotate java constructor parameter
    * constructor parameter
* `@file:`
* `@property:`
    * annotations with this target are not visible to Java;
* `@set:`
    * property setter;
* `@receiver:`
    * receiver parameter of an extension function or property;
* `@setparam:`
    * property setter parameter;
* `@delegate:`
    * the field storing the delegate instance for a delegated property

```
class Example(@field:Ann val foo,    // annotate Java field
              @get:Ann val bar,      // annotate Java getter
              @param:Ann val quux)   // annotate Java constructor parameter
```

## Visibility Modifiers
* packages
    * package内のclass/functinoのvisibility
    * private
        * file only
    * public
        * visibility modifiersを省略した場合
    * internal
    * protected
* class/interface
    * class内のclass/methodのvisibility
    * private
        * file only
    * public
        * visibility modifiersを省略した場合
    * internal
    * protected
* constructors

## Operators
* elvis operator
* `!!` operator

```kotlin
// if b is null, this returns null
val l = b?.length ?: -1
// if b is null, this throws null-execption
val l = b!!.length
```

## Equality
* [Equality - Kotlin Programming Language](https://kotlinlang.org/docs/reference/equality.html)

* equals
    * [equals - Kotlin Programming Language](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.reflect/-k-class/equals.html)

```
// structual equality
a == b
// a == b is equvalent to
a?.equals(b) ?: (b === null)

// reference equality
a === b
```

## Any == Object?
* AnyはObjectではない
* Anyは `toString(), hashCode(),equals()`のmehthodしか持たない
* javaのObjectはkotlinではAnyとして扱われるが、Objectの他のmethodは直接呼べない
* extensionとして実装する必要がある

### Companion object/object/static method
* [What is the advantage of "companion object" vs static keyword - Language Design - Kotlin Discussions](https://discuss.kotlinlang.org/t/what-is-the-advantage-of-companion-object-vs-static-keyword/4034/21)

kotlinのobjectはsingletonを与える。
companion objectはclassのInstance内でのstatic methodを与える。


## Reference
* [Outdated Kotlin Runtime | Smartphone-Zine](http://www.smartphone-zine.com/android/outdated-kotlin-runtime)
* [kotlin-web-site/coding-conventions.md at yole/styleguide · JetBrains/kotlin-web-site](https://github.com/JetBrains/kotlin-web-site/blob/yole/styleguide/pages/docs/reference/coding-conventions.md)
