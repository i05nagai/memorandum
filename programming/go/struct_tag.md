---
title: struct tag
---

## struct tag


```go
import (
	"fmt"
	"reflect"
)

type Product struct {
	Name  string `json:"name" db:"product_name"`
	Price int    `json:"price" db:"price_in_cents"`
}

func main() {
	t := reflect.TypeOf(Product{})
	for i := 0; i < t.NumField(); i++ {
		field := t.Field(i)
		fmt.Printf("Field: %s\n", field.Name)
		fmt.Printf("  JSON tag: %s\n", field.Tag.Get("json"))
		fmt.Printf("  DB tag:   %s\n", field.Tag.Get("db"))
	}
}
```

## Reference
- https://go.dev/wiki/Well-known-struct-tags
