---
title: Scala
---

## Scala

## Install
[Scala | Mac OS X Setup Guide](http://sourabhbajaj.com/mac-setup/Scala/README.html)

For OSX,

```
brew install scala
```

For ubuntu 16.04,

```
apt-get install scala
```

## Syntax
* operator notation associavity
    * if the method ends with a colon, the method is called by right operand
        * `a :: b` is `b.::(a)`
    * otherwise, the method is called by left operand
        * `a * b` is `a.*(b)`
* `def this(elem: Type*)`
    * repeated parameters


#### method

```scala
def aaa(newStack: => Int, lastItemAdded: Int): Int = {
  return 1
}

aaa(1, 1)
```

#### class

* `class Queue[T] private`

#### generics
* [Overcoming type erasure in Scala – Sinisa Louc – Medium](https://medium.com/@sinisalouc/overcoming-type-erasure-in-scala-8f2422070d20)

* type erasure
    * it’s a procedure performed by Java and Scala compilers which removes all generic type information after compilatio
    * See `Manifest`


#### Manifest
* [TypeTags and Manifests \| Scala Documentation](https://docs.scala-lang.org/overviews/reflection/typetags-manifests.html)
* [scala\.reflect\.ClassTag Scala Example](https://www.programcreek.com/scala/scala.reflect.ClassTag)
* if you cannot import `reflect` and got `object runtime is not a member of package reflect`, you need to add `scala-reflect` as a dependecy

* introduced since scala 2.7

TypeTags

* TypeTag:
    * `classic`
    * WeakTypeTag
* ClassTag

#### traits

* inherited trait by `with` or `extends` keyword
    - `extend` can be used only once
* mixin
* method can be overrided
* java interface + maintain state and declare fields
* no primary constructor
* `abstract class` can inherit `trait`
* `traits` inherits class

to trait or not to trait

* if the behaivor will not be reused
    * make it a concrete class
* if it might be resused in multiple, unrelated classes
    * make it a trait
* if you want to inherit from it in Java code,
    * use an abstract class
* if you plan to distribute it in compiled form and you expect outside groups to write classes inheriting from it
    * you might lean towards using an abstract class
* if efficient is very important
    * lean towards using a class
* if you still do not know
    * start by making it as a trait

#### apply function

* `object Greet { def apply(name: String): String = name }` then `Greet("name")`

#### package

* may appear anywhere
* may refer to objects (singleton or regular) in addition to package
* let you rename and hide some of the imporeted members
* member of packages can be labeled with the acess modifiers `private` and `protected`
* no access modifier means `public`


#### package object
- https://www.scala-lang.org/docu/files/packageobjects/packageobjects.html

#### case object
https://docs.scala-lang.org/overviews/scala-book/case-objects.html

- It’s serializable
- It has a default hashCode implementation
- It has an improved toString implementation

Use cases

- When creating enumerations
- When creating containers for “messages” that you want to pass between other objects (such as with the Akka actors library)

#### implict conversion

* use `implicit` keyword
* you can use it to mark any variable, function, or object definition
* `implicit object`
    * [scala \- What are implicit objects? \- Stack Overflow](https://stackoverflow.com/questions/22592456/what-are-implicit-objects)
    * [The Neophyte's Guide to Scala Part 12: Type classes \- Daniel Westheide](https://danielwestheide.com/blog/2013/02/06/the-neophytes-guide-to-scala-part-12-type-classes.html)

```scala
implicit class IntWithTimes(x: Int) {
  def times[A](f: => A): Unit = {
    def loop(current: Int): Unit =
      if (current > 0) {
        f
        loop(current - 1)
      }
    loop(x)
  }
}

5 times {
  println('a')
}
```

#### Type parametrization

* We denote `T` is a subtype of `S` by `T < S`
* `trait Queue[+T]`
    * covariant
    * If `T < S`, `Queue[T] < Queue[S]`
* `trait [-T]`
    * contravariant
    * If `T` is subtype of S, this would imply that `Queue[S]` is a subtype of `Queue[T]`
    * If `T < S`, `Queue[T] > Queue[S]`
* `T*`
    * repeated parameter
* `[U: >: T]`
    * `class Queue[+T] { def enqueue[U >: T](x: U) }`
    * `T` is the lower bound for `U`
    * `U` is required to be supertype of `T`
* `[U: <: T]`
    * `U` is required to be subtype of `T`
* `[T: ClassManifest]`
    * context bound
    * implict parameter list
    * `def meth[A : ContextBound1 : ContextBoundN](a: A)`
        * is equivalent to `def meth[A](a: A)(implicit evidence: ContextBound1[A], ContextBoundN[A])`

## conf
- https://blog.knoldus.com/quickknol-reading-configuration-files-in-scala/
- https://lightbend.github.io/config/
    - library to read config

## val and def
- https://stackoverflow.com/questions/19642053/when-to-use-val-or-def-in-scala-traits

## Tips

### Styleguide
* [Scala Style Guide | Scala Documentation](https://docs.scala-lang.org/style/index.html)
* [Scalacheat | Scala Documentation](https://docs.scala-lang.org/cheatsheets/index.html)


### Scala project templates with graddle
* [chronodm/scala\-project\-template: A skeletal Scala/Gradle project](https://github.com/chronodm/scala-project-template)


### not found: value println
If you find this error when importing `scala.Predef` or any classes or objects under `scala.Predef`, you should try remove the line importing the objectrs related to `scala.Predef`



## Reference
* [learning Scalaz — learning Scalaz](http://eed3si9n.com/learning-scalaz/)
* [Introduction · Scala研修テキスト](https://dwango.github.io/scala_text/)
* [deanwampler/prog\-scala\-2nd\-ed\-code\-examples: The code examples used in Programming Scala, 2nd Edition \(O'Reilly\)](https://github.com/deanwampler/prog-scala-2nd-ed-code-examples)
* [A Tour of Scala: Explicitly Typed Self References \| The Scala Programming Language](https://www.scala-lang.org/old/node/124)
* [4 Fun and Useful Things to Know about Scala's apply\(\) functions](https://blog.matthewrathbone.com/2017/03/06/scala-object-apply-functions.html)
* [generics \- Meaning of additional colon in Scala class parametrization \- Stack Overflow](https://stackoverflow.com/questions/12786910/meaning-of-additional-colon-in-scala-class-parametrization)
