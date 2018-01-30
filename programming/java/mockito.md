---
title: Mockito
---

## Mockito


## Usage
* [Mockito (Mockito 2.9.0 API)](https://static.javadoc.io/org.mockito/mockito-core/2.9.0/org/mockito/Mockito.html)


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



## Reference
* [Mockito framework site](http://site.mockito.org/)
* [mockito/mockito: Most popular Mocking framework for unit tests written in Java](https://github.com/mockito/mockito)
* [Mockito 初めの一歩 - Qiita](https://qiita.com/mstssk/items/98e597c13f12746c907d)
