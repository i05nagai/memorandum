---
title: Spek
---

## Spek
kotlin用のBDD。RSpecを参考にしている。

## Examples
* [spek/samples/src/test/kotlin/org/spekframework/spek2/samples at 2.x · spekframework/spek](https://github.com/spekframework/spek/tree/2.x/samples/src/test/kotlin/org/spekframework/spek2/samples)



## Usage
testは`org.jetbrains.spek.api.Spek` classを継承して作る。

```kotlin
import org.jetbrains.spek.api.Spek
object NameSpec: Spek({
    beforeEachTest {
        //
    }
    afterEachTest {
        //
    }
    // write test
    describe('methodName') {
        it ('should be okay') {
            // do test
        }
    }

    // skip if suffix is x
    xit("should not return 11") {
        // Waiting for next release
    }
})
```

以下の二通りの書き方ができる。

* given, on, it
    * Spekの最初のversionの書き方
    * name
        * class名としてtestのspecification名をつける
    * given
        * testのcontextを書く
    * on
        * actionを書く
    * it
        * 実際のtestを書く
* describe it
    * Jasmine and Mocha style frameworksの記法
    * name
        * class名としてtestのspecification名をつける
    * describe
        * 何をtestするかのcontextを書く
        * describeはnestできる
    * it
        * 実際のtestを書く

```kotlin
object CalculatorSpec: Spek({
    given("a calculator") {
        val calculator = SampleCalculator()
        on("addition") {
            val sum = calculator.sum(2, 4)
            it("should return the result of adding the first number to the second number") {
                assertEquals(6, sum)
            }
        }
        on("subtraction") {
            val subtract = calculator.subtract(4, 2)
            it("should return the result of subtracting the second number from the first number") {
                assertEquals(2, subtract)
            }
        }
    }
})
```

```kotlin
object SimpleSpec: Spek({
    describe("a calculator") {
        val calculator = SampleCalculator()

        describe("addition") {
            val sum = calculator.sum(2, 4)

            it("should return the result of adding the first number to the second number") {
                assertEquals(6, sum)
            }
        }

        describe("subtraction") {
            val subtract = calculator.subtract(4, 2)

            it("should return the result of subtracting the second number from the first number") {
                assertEquals(2, subtract)
            }
        }
    }
})
```

**Scopes**

* Test
    * jUnitのtest methodと同じ
    * `it`のscopeと同じ
* Group
    * 複数のitをまとめたものがgroup
* Action

xUnitでよくあるfixtureが使える。

```kotlin
object FixtureSpec: Spek({
    describe("a group") {
        beforeGroup {
            ...
        }

        beforeEachTest {
            ...
        }

        context("a nested group") {

            beforeEachTest {
                ...
            }

            beforeEachTest {
                ...
            }

            it ("should work") { ... }
        }

        it("do something") { ... }

        afterEachTest {
            ...
        }

        afterGroup {
            ...
        }
    }
})
```

**Subject**

```kotlin
object SimpleCalculatorSpec: SubjectSpek<Calculator>({
    // instantiate Calculator() and assign it to subject
    // the instantiation is executed each tests
    subject { Calculator() }

    it("should return the result of adding the first number to the second number") {
        assertEquals(6, subject.sum(2, 4))
    }

    it("should return the result of subtracting the second number from the first number") {
        assertEquals(2, subject.subtract(4, 2)) (2)
    }
})
```

**Shared Subjects**

Subclassのtestで親classのtestを引き継ぐ場合などに有用。
`itBehavesLike(ClassNane)`で、subjectを差し替えてtestを引き継ぐ。

```kotlin
object AdvancedCalculatorSpec: SubjectSpek<AdvancedCalculator>({
    subject { AdvancedCalculator() }

    // use same tests in Simple
    itBehavesLike(SimpleCalculatorSpec)

    describe("pow") {
        it("should return the power of base raise to exponent") {
            assertEquals(subject.pow(2, 2), 4)
        }
    }
})
```

## Assertions
Spek自身にAssertionの関数はない。
下記のPluginを使う

* HamKrest
* Expekt
* Kluent

## With gradle

* [Spek User Guide](http://spekframework.org/docs/latest/#_gradle_kotlin_script)

## Reference
* [Spek - A Kotlin Specification Framework for the JVM](http://spekframework.org/)
