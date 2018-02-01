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

## Reference
* [Outdated Kotlin Runtime | Smartphone-Zine](http://www.smartphone-zine.com/android/outdated-kotlin-runtime)
