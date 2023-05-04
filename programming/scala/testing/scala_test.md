---
title: ScalaTest
---

## ScalaTest


## Install
sbt

```sbt

val scalaTestVersion = "3.0.1"
libraryDependencies ++= Seq(
  "org.scalatest" %% "scalatest" % scalaTestVersion % "test",
)
```

## sytle
https://www.scalatest.org/user_guide/selecting_a_style

- FunSuite
    - xUnit
- FlatSpec
    - BDD
- AnyFunSpec
    - Ruby RSpec
- WordSpec
    - spec, spec2
- AnyFreeSpec


## Fixture

```scala
class ExampleSpec extends AnyFlatSpec {

  def fixture =
    new {
      val builder = new StringBuilder("ScalaTest is ")
      val buffer = new ListBuffer[String]
    }

  "Testing" should "be easy" in {
    val f = fixture
    f.builder.append("easy!")
    assert(f.builder.toString === "ScalaTest is easy!")
    assert(f.buffer.isEmpty)
    f.buffer += "sweet"
  }

  it should "be fun" in {
    val f = fixture
    f.builder.append("fun!")
    assert(f.builder.toString === "ScalaTest is fun!")
    assert(f.buffer.isEmpty)
  }
}
```

```scala
trait Builder extends SuiteMixin { this: Suite =>
  val builder = new StringBuilder
  abstract override def withFixture(test: NoArgTest) = {
    builder.append("ScalaTest is ")
    try super.withFixture(test) // To be stackable, must call super.withFixture
    finally builder.clear()
  }
}

trait Buffer extends SuiteMixin { this: Suite =>
  val buffer = new ListBuffer[String]
  abstract override def withFixture(test: NoArgTest) = {
    try super.withFixture(test) // To be stackable, must call super.withFixture
    finally buffer.clear()
  }
}

class ExampleSpec extends AnyFlatSpec with Builder with Buffer {

  "Testing" should "be easy" in {
    builder.append("easy!")
    assert(builder.toString === "ScalaTest is easy!")
    assert(buffer.isEmpty)
    buffer += "sweet"
  }

  it should "be fun" in {
    builder.append("fun!")
    assert(builder.toString === "ScalaTest is fun!")
    assert(buffer.isEmpty)
    buffer += "clear"
  }
}
```

## assertions

```scala
assert(left == right)

fail() // forcing failure

val s = "hi"
assertThrows[IndexOutOfBoundsException] { // Result type: Assertion
  s.charAt(-1)
}

val s = "hi"
val caught =
  intercept[IndexOutOfBoundsException] { // Result type: IndexOutOfBoundsException
    s.charAt(-1)
  }
assert(caught.getMessage.indexOf("-1") != -1)

// if assume is false, the following test will be cancelled
assume(database.isAvailable)
```

## Run before and after tests
https://www.scalatest.org/scaladoc/3.2.14/org/scalatest/flatspec/AnyFlatSpec.html#beforeAndAfter

## Tips

#### Disable logging
https://stackoverflow.com/questions/27220196/disable-scalatest-logging-statements-when-running-tests-from-maven


## Reference
* [scalatest/scalatest: A testing tool for Scala and Java developers](https://github.com/scalatest/scalatest)
* [ScalaTest](http://www.scalatest.org/)
