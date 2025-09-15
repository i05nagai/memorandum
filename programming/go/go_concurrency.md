---
title: Go Concurrency
---

## Go Concurrency


https://drive.google.com/file/d/1nPdvhB0PutEJzdCq5ms6UI58dp50fcAN/view

```go
package main

import (
	"context"
	"fmt"
	"time"
)

// worker simulates a long-running task that checks for cancellation.
func worker(ctx context.Context, id int) {
	fmt.Printf("Worker %d started\n", id)
	for {
		select {
		case <-ctx.Done():
			fmt.Printf("Worker %d stopped: %s\n", id, ctx.Err())
			return
		default:
			// Simulate doing work
			fmt.Printf("Worker %d is working...\n", id)
			time.Sleep(500 * time.Millisecond)
		}
	}
}

func main() {
	// Create a context with cancel function
	ctx, cancel := context.WithCancel(context.Background())

	// Start the worker goroutine
	go worker(ctx, 1)

	// Let the worker run for 2 seconds
	time.Sleep(2 * time.Second)

	// Cancel the context to stop the worker
	fmt.Println("Canceling context...")
	cancel()

	// Give the worker time to finish cleanly
	time.Sleep(1 * time.Second)

	fmt.Println("Main function done.")
}
```


## wait for goroutines to complete
https://go.dev/blog/loopvar-preview

```go
func main() {
    done := make(chan bool)

    values := []string{"a", "b", "c"}
    for _, v := range values {
        go func() {
            fmt.Println(v)
            // Output: c, c, c 
            done <- true
        }()
    }

    // wait for all goroutines to complete before exiting
    for _ = range values {
        <-done
    }
}
```

## Reference

