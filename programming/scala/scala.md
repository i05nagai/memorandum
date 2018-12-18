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


class

* `class Queue[T] private`


traits

* inherited trait by `with` or `extends` keyword
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


package

* may appear anywhere
* may refer to objects (singleton or regular) in addition to package
* let you rename and hide some of the imporeted members
* member of packages can be labeled with the acess modifiers `private` and `protected`
* no access modifier means `public`

## Tips

### Styleguide
* [Scala Style Guide | Scala Documentation](https://docs.scala-lang.org/style/index.html)
* [Scalacheat | Scala Documentation](https://docs.scala-lang.org/cheatsheets/index.html)


### Scala project templates with graddle
* [chronodm/scala\-project\-template: A skeletal Scala/Gradle project](https://github.com/chronodm/scala-project-template)


## Reference
* [learning Scalaz — learning Scalaz](http://eed3si9n.com/learning-scalaz/)
* [Introduction · Scala研修テキスト](https://dwango.github.io/scala_text/)
* [deanwampler/prog\-scala\-2nd\-ed\-code\-examples: The code examples used in Programming Scala, 2nd Edition \(O'Reilly\)](https://github.com/deanwampler/prog-scala-2nd-ed-code-examples)

