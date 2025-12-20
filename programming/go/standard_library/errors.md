---
title: errors
---

## errors


## Tips
- https://go.dev/blog/go1.13-errors
- When adding additional context to an error, either with fmt.Errorf or by implementing a custom type, you need to decide whether the new error should wrap the original. There is no single answer to this question; it depends on the context in which the new error is created. Wrap an error to expose it to callers. Do not wrap an error when doing so would expose implementation details.

## Wrapping errors

```go
err := fmt.Errorf("access denied: %w", ErrPermission)
```

## erros.Unwrap

```go
func doSomething() error {
	return errors.New("low-level I/O failure")
}

func handler() error {
	err := doSomething()
	if err != nil {
		return fmt.Errorf("handler failed: %w", err)
	}
	return nil
}

func main() {
    err := handler()
    fmt.Println(err)
}
```


## errors.Is

```go
var ErrPermission = errors.New("permission denied")
func checkPermission() error {
	return fmt.Errorf("access error: %w", ErrPermission)
}
func main() {
	err := checkPermission()
	if errors.Is(err, ErrPermission) {
		fmt.Println("permission error detected")
	}
}
```

## errors.As
Extracting Specific Error Types

```go
type MyError struct {
	Msg string
}

func (e MyError) Error() string {
	return e.Msg
}

func fail() error {
	return fmt.Errorf("operation failed: %w", MyError{"something bad happened"})
}

func main() {
	err := fail()
	var myErr MyError
	if errors.As(err, &myErr) {
		fmt.Println("custom error occurred:", myErr.Msg)
	}
}
```

## Reference
- https://go.dev/blog/error-handling-and-go
