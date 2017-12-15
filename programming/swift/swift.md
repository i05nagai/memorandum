---
title: Swift
---

## Swift
* delegateにoverrideは不要

## as
* [Swift as!について - Qiita](https://qiita.com/suisuina/items/f8639d1aee61fb0530b5)

* as
    * キャストが成功すると保証されるときに使用（アップキャストなど）
* as!
    強制ダウンキャストの際に使用
* as?
    * ダウンキャストが成功するか分からない場合に使用(失敗すると戻り値はnil)

## Guard
* https://qiita.com/mishimay/items/75fb0958f33079ff0e8a

```swift
func show(message: String?) {
    if message == nil {
        return
    }
    let theMessage = message! // ここ
    // ...
}
```

guardするとunwrappした変数として後から利用可能

```swift
func show(message: String?) {
    guard let theMessage = message else {
        return
    }

    print(theMessage) // アンラップした変数を使うことができる
}
```

guardの中では以下のいずれかが必要

* `noreturn`のついた関数を呼ぶ
* 以下のいずれかを書く
    * `return`
    * `break`
    * `continue`
    * `throw`


## Enum
* [The Swift Programming Language - Enumerations（列挙型）をまとめる - Qiita](https://qiita.com/kiyotaman/items/33b6fb7556d37dba2bbc)

```swift
enum CompassPoint {
    case North
    case South
    case East
    case West
}
```

型が推測可能なら省略可能

```swift
var directionToHead = CompassPoint.West
directionToHead = .West
```


## Optional type
* https://qiita.com/cotrpepe/items/518c4476ca957a42f5f1#t-%E3%81%AFimplicitlyunwrappedoptionalt-%E3%81%AE%E3%82%B7%E3%83%B3%E3%82%BF%E3%83%83%E3%82%AF%E3%82%B9%E3%82%B7%E3%83%A5%E3%82%AC%E3%83%BC%E3%81%A7%E3%81%82%E3%82%8B

```swift
var a: Int?
var a: Optional<Int>
```

```swift
var a: Int!
var a: ImplicitlyUnwrappedOptional<Int>
```

Forced unwrapp

```
wrappedDog!.bark()
```


## Reference
* [swift/OptimizationTips.rst at master · apple/swift](https://github.com/apple/swift/blob/master/docs/OptimizationTips.rst)
* [Best Swift Books In 2017 – Level Up! – Medium](https://medium.com/level-up-web/best-swift-books-in-2017-e2b4d562825f)
