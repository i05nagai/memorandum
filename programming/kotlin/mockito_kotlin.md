---
title: Mockito-Kotlin
---

## Mockito-Kotlin


## Usage
* [Mocking and verifying · nhaarman/mockito-kotlin Wiki](https://github.com/nhaarman/mockito-kotlin/wiki/Mocking-and-verifying)

Creating mock

```kotlin
// creating mock
// this
val mock : MyClass = mock()
// or this
val mock = mock<MyClass>()
// pass the new mock as an argument
myClass.test(mock())
```

`Mockito`の`when`のかわりに`whenever`が使える。
kotlinで`when`は予約語。
が呼ばれた

```kotlin
// If mock.stringValue() is called, mock returns `test`
whenever(mock.stringValue()).thenReturn("test")
```

lambda expressionでreturnを設定できる。

```kotlin
//
val mock = mock<MyClass> {
    on { stringValue() }.doReturn("test")
}
// `doReturn` is defined as infix operator
val mock = mock<MyClass> {
    on { stringValue() } doReturn "test"
}
```

verify expression

```kotlin
// `doSomething` is called with "test" as an argument
verify(myClass).doSomething("test")
// `doSomething` is called with any argument
verify(myClass).doSomething(any())
// `doSomething` is called with an argument inherting MySubClass
verify(myClass).doSomething(any<MySubClass>())
```

verifying properties

```kotlin
interface Foo {
  var bar : String
}

@Test
fun test() {
  val foo = mock<Foo>()
  foo.bar = "test"
  // veryfy properties, where `foo` is mock
  verify(foo).bar = "test"
}
```

Arguments matcher
`check`は`(T) -> Unit`の関数を実行するだけなので、failを知らせる場合はassertを投げる必要がある。
そのため下記例では、`assertThat`をしている。

```kotlin
// size is an arugment of setItems
verify(myClass).setItems(argThat { size == 2 } )
// is equivalent to
verify(myClass).setItems(argForWhich { size == 2 } )
// 
verify(myClass).setItems(check { 
  assertThat(it.size, is(2))
  assertThat(it[0], is("test"))
})
```

Argument Captors

```kotlin
argumentCaptor<String>().apply {
  verify(myClass, times(2)).setItems(capture())

  assertEquals(2, allValues.size)
  assertEquals("test", firstValue)
}
```

## Reference
