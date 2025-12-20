---
title: testing
---

## testing

## Unit Test
If the test file is in the same package, it may refer to unexported identifiers within the package, as in this example:


```go
package abs

import "testing"

func TestAbs(t *testing.T) {
    got := Abs(-1)
    if got != 1 {
        t.Errorf("Abs(-1) = %d; want 1", got)
    }
}
```

If the file is in a separate "_test" package, the package being tested must be imported explicitly and only its exported identifiers may be used. This is known as "black box" testing.


```go
package abs_test

import (
	"testing"

	"path_to_pkg/abs"
)

func TestAbs(t *testing.T) {
    got := abs.Abs(-1)
    if got != 1 {
        t.Errorf("Abs(-1) = %d; want 1", got)
    }
}
```

## Benchmark

```go
func BenchmarkTemplateParallel(b *testing.B) {
    templ := template.Must(template.New("test").Parse("Hello, {{.}}!"))
    b.RunParallel(func(pb *testing.PB) {
        var buf bytes.Buffer
        for pb.Next() {
            buf.Reset()
            templ.Execute(&buf, "World")
        }
    })
}
```

## Example
https://go.dev/blog/examples

```go
func Example_suffix() { ... }
func ExampleF_suffix() { ... }
func ExampleT_suffix() { ... }
func ExampleT_M_suffix() { ... }
```

```
func ExampleString() {
    fmt.Println(reverse.String("hello"))
    // Output: golly
}
```

## Fuzz

```go
func FuzzHex(f *testing.F) {
  for _, seed := range [][]byte{{}, {0}, {9}, {0xa}, {0xf}, {1, 2, 3, 4}} {
    f.Add(seed)
  }
  f.Fuzz(func(t *testing.T, in []byte) {
    enc := hex.EncodeToString(in)
    out, err := hex.DecodeString(enc)
    if err != nil {
      t.Fatalf("%v: decode: %v", in, err)
    }
    if !bytes.Equal(in, out) {
      t.Fatalf("%v: not equal after round trip: %v", in, out)
    }
  })
}
```

## Reference
- https://pkg.go.dev/testing
