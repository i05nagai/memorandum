---
title: Mockito
---

## Mockito


## Usage
* [Mockito (Mockito 2.9.0 API)](https://static.javadoc.io/org.mockito/mockito-core/2.9.0/org/mockito/Mockito.html)

Mockの生成

```java
import static org.mockito.Mockito.when;
import static org.mockito.Mockito.verify;

// create
ITweet iTweet = mock(ITweet.class);
// set return
when(iTweet.getMessage()).thenReturn("Using mockito is great");
// do something with mock


// check mock behavior
verify(iTweet, atLeastOnce()).getMessage();
```

Arguments matcher

```java
verify(mock).someMethod(anyInt(), anyString(), eq("third argument"));
```

Verifying exact number of invocations / at least x / never

```java
verify(mockedList, times(1)).add("once");
verify(mockedList, never()).add("never happened");
verify(mockedList, atLeastOnce()).add("three times");
verify(mockedList, atLeast(2)).add("three times");
verify(mockedList, atMost(5)).add("three times");
```

Verification in order
呼び出し順序の保証。

```java
// A. Single mock whose methods must be invoked in a particular order
List singleMock = mock(List.class);

//using a single mock
singleMock.add("was added first");
singleMock.add("was added second");

//create an inOrder verifier for a single mock
InOrder inOrder = inOrder(singleMock);

//following will make sure that add is first called with "was added first, then with "was added second"
inOrder.verify(singleMock).add("was added first");
inOrder.verify(singleMock).add("was added second");
```

2つのobjectのmethodの呼び出し順序

```jav
//using mocks
firstMock.add("was called first");
secondMock.add("was called second");

//create inOrder object passing any mocks that need to be verified in order
InOrder inOrder = inOrder(firstMock, secondMock);

//following will make sure that firstMock was called before secondMock
inOrder.verify(firstMock).add("was called first");
inOrder.verify(secondMock).add("was called second");
```

### Mock static methods
`doReturn`を使う。

```
Mockito
  .doReturn(data)
  .when(SomeClass).doSomething(any()));
```

## Injecting Mock
* [Auto inject dependencies in JUnit using Mockito - JDriven](https://blog.jdriven.com/2013/01/auto-inject-dependencies-in-junit-using-mockito/)
* [Unit tests with Mockito - Tutorial](http://www.vogella.com/tutorials/Mockito/article.html)
* [Mockito: Why You Should Not Use InjectMocks Annotation to Autowire Fields – Ted Vinke's Blog](https://tedvinke.wordpress.com/2014/02/13/mockito-why-you-should-not-use-injectmocks-annotation-to-autowire-fields/)
* [Use Mockito to mock autowired fields - Lubos Krnac's blog](https://lkrnac.net/blog/2014/01/mock-autowired-fields/)



## Reference
* [Mockito framework site](http://site.mockito.org/)
* [mockito/mockito: Most popular Mocking framework for unit tests written in Java](https://github.com/mockito/mockito)
* [Mockito 初めの一歩 - Qiita](https://qiita.com/mstssk/items/98e597c13f12746c907d)
* [JUnit・JMockitチートシート - Qiita](https://qiita.com/disc99/items/4dc78f9a96aa0a9aeb47#_reference-f869d5544b0f1f431513)
