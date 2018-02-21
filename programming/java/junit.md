---
title: JUnit
---

## JUnit

```
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class FirstJUnit5Tests {
    @Test
    void myFirstTest() {
        assertEquals(2, 1 + 1);
    }

}
```

## Assertions
* https://junit.org/junit5/docs/current/user-guide/#writing-tests-assertions

## Conditional Test Execution
Testの実行の条件をつけることができる。

* Operating System Conditions
* Java Runtime Environment Conditions
* System Property Conditions
* Environment Variable Conditions
* Script-based Conditions

## Tagging and Filtering
testにはtagをつけて、filterして、実行できる。

## Dependency injections
* https://junit.org/junit5/docs/current/user-guide/#writing-tests-dependency-injection

## Reference
* [JUnit 5 User Guide](https://junit.org/junit5/docs/current/user-guide/)
* [Unit Testing with JUnit - Tutorial](http://www.vogella.com/tutorials/JUnit/article.html)
