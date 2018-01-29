---
title: expekt
---

## expekt
Expekt is a (work in progress) BDD assertion library for Kotlin, inspired by Chai.js.

## Gradle

```
testCompile "com.winterbe:expekt:0.5.0"
```

## Usage

```
import com.winterbe.expekt.expect
import com.winterbe.expekt.should
class ExpektTest {
    @Test
    fun helloExpekt() {
        23.should.equal(23)
        "Kotlin".should.not.contain("Scala")
        listOf(1, 2, 3).should.have.size.above(1)
    }
}
```

`should`の記法の一覧

```
23.should.equal(23)
null.should.be.`null`
"foo".should.not.equal("bar")
3.should.satisfy { it % 2 == 1 }
3.should.be.above(2).and.below(4)
"abc".should.contain("bc").and.startWith("a")
"abc".should.not.have.length.above(3)
"abc".should.not.match(Regex("[0-9]+"))
listOf(1, 2, 3).should.contain(3).and.have.length.above(2)
listOf(1, 2, 3).should.contain.any.elements(1, 3, 4)
listOf(1, 2, 3).should.have.all.elements(1, 2, 3)
mapOf("foo" to "bar", "bar" to "foo").should.contain("foo" to "bar")
```

`expect`の記法の一覧

```kotlin
expect(23).to.equal(23)
expect(null).to.be.`null`
expect("foo").not.to.equal("bar")
expect(3).not.to.satisfy { it % 2 == 1 }
expect(3).to.be.above(2).and.to.be.below(4)
expect("abc").to.contain("bc").and.to.startWith("a")
expect("abc").not.to.have.length.above(3)
expect("abc").not.to.match(Regex("[0-9]+"))
expect(listOf(1, 2, 3)).to.contain(3).and.to.have.length.above(2)
expect(listOf(1, 2, 3)).to.contain.any.elements(1, 3, 4)
expect(listOf(1, 2, 3)).to.have.all.elements(1, 2, 3)
expect(mapOf("foo" to "bar", "bar" to "foo")).to.contain("foo" to "bar")
```


## Reference
* [winterbe/expekt: BDD assertion library for Kotlin](https://github.com/winterbe/expekt)
