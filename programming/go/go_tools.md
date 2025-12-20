---
title: go tools
---

## go tools


## //go:build tools
https://www.alexedwards.net/blog/using-go-run-to-manage-tool-dependencies


Convetion to manage go dev dependencis.

```
//go:build tools
// +build tools

package tools

import (
	_ "github.com/99designs/gqlgen"                 // the CLI entrypoint used by go:generate
	_ "github.com/99designs/gqlgen/api"             // invoked by the CLI
	_ "github.com/99designs/gqlgen/codegen/config"  // pulls x/tools/go/packages
	_ "github.com/99designs/gqlgen/internal/imports"// pulls x/tools/imports, ast/astutil
)
```

From 1.17, we can use `go run` to run a specific version of a tool without needing to install it globally.

```
//go:generate go run github.com/99designs/gqlgen@v0.17.24 generate
```


## Reference
