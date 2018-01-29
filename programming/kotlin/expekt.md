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


## Reference
* [winterbe/expekt: BDD assertion library for Kotlin](https://github.com/winterbe/expekt)
