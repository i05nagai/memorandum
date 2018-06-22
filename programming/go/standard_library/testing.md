---
title: testing
---

## testing


## Testing

```go
func TestXxx(*testing.T)
```

Naming convention

* `xxx.go`
    * `package zzz`
    * `Xxx` func
* `xxx_test.go`
    * `package zzz`
        * Put the file in the same package as the one being tested.
        * The file will be excluded from regular package builds
    * `TextXxx` func
    * it's not common to test package private functions

## Benchmarking

```go
func BenchmarkXxx(b *testing.B)
```

* the functions are executed by `go test` command when its `-bench` flag is provided

```go
func BenchmarkXxx(b *testing.B) {
    b.ResetTimer()
}
```

## Subtesting and subbenchmarking

```go
func TestFoo(t *testing.T) {
    // <setup code>
    t.Run("A=1", func(t *testing.T) { ... })
    t.Run("A=2", func(t *testing.T) { ... })
    t.Run("B=1", func(t *testing.T) { ... })
    // <tear-down code>
}
```

## Reference
* [testing - The Go Programming Language](https://golang.org/pkg/testing/)
* [Go advanced testing tips & tricks – Povilas Versockas – Medium](https://medium.com/@povilasve/go-advanced-tips-tricks-a872503ac859)
