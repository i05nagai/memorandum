---
title: Golang CI Lint
---

## Golang CI Lint

## Configurations



- exhaustive
    -  checks exhaustiveness of enum switch statements in Go source code.
    - https://github.com/nishanths/exhaustive
- gochecksumtype
    - A simple utility for running exhaustiveness checks on type switch statements. Exhaustiveness checks are only run on interfaces that are declared to be "sum types."
    - https://github.com/alecthomas/go-check-sumtype
- gosec 
    - inspects source code for security problems
- errorlint
- exhaustive
- exptostd
- forbidigo # forbids identifiers
- funcorder # checks the order of functions, methods, and constructors
- gochecksumtype # checks exhaustiveness on Go "sum types"
- intrange # finds places where for loops could make use of an integer range
- makezero # finds slice declarations with non-zero initial length
- mnd # detects magic numbers
- musttug
- https://github.com/go-simpler/musttag?tab=readme-ov-file
- nilerr # finds the code that returns nil even if it checks that the error is not nil
- noctx # finds sending http request without context.Context
- perfsprint # checks that fmt.Sprintf can be replaced with a faster alternative
  - Golang linter for performance, aiming at usages of fmt.Sprintf which have faster alternatives.
- predeclared # finds code that shadows one of Go's predeclared identifiers
- protogetter # reports direct reads from proto message fields when getters should be used
- recvcheck # checks for receiver type consistency
  - Don’t mix receiver types. Choose either pointers or struct types for all available method
- revive # fast, configurable, extensible, flexible, and beautiful linter for Go, drop-in replacement of golint
- sloglint
  - https://github.com/go-simpler/sloglint
- spancheck # checks for mistakes with OpenTelemetry/Census spans
- testifylint # checks usage of github.com/stretchr/testify
- tparallel # detects inappropriate usage of t.Parallel() method in your Go test codes
- unconvert # removes unnecessary type conversions
- unparam # reports unused function parameters
- unused # checks for unused constants, variables, functions and types
- usestdlibvars # detects the possibility to use variables/constants from the Go standard library
- wastedassign # finds wasted assignment statements
- zerologlint # detects the wrong usage of zerolog that a user forgets to dispatch zerolog.Event
- wrapcheck # checks that errors returned from external packages are wrapped


## CLI

Cache control and information

```
golangci-lint cache
```

Generate the autocompletion script for the specified shell

```
golangci-lint completion
```

Config file information

```
golangci-lint config
```

Build a version of golangci-lint with custom linters

```
golangci-lint custom
```

Format Go source files

```
golangci-lint fmt
```

List current formatters configuration

```
golangci-lint formatters
```

List current linters configuration

```
golangci-lint linters
```

Migrate configuration file from v1 to v2

```
golangci-lint migrate
```

Run the linters

```
golangci-lint run
```

## Configuration
- .golangci.yml
- .golangci.yaml
- .golangci.toml
- .golangci.json


### Linters

- errcheck:
    - Errcheck is a program for checking for unchecked errors in Go code. These unchecked errors can be critical bugs in some cases.
- errorlint:
    - Errorlint is a linter for that can be used to find code that will cause problems with the error wrapping scheme introduced in Go 1.13.
- gocritic:
    - Provides diagnostics that check for bugs, performance and style issues. [auto-fix]
- gomodguard:
    - Allow and block list linter for direct Go module dependencies.
    - This is different from depguard where there are different block types for example version constraints and module recommendations.
- govet:
    - Vet examines Go source code and reports suspicious constructs. It is roughly the same as 'go vet' and uses its passes.
- importas:
    - Enforces consistent import aliases. [auto-fix]
- ineffassign:
    - Detects when assignments to existing variables are not used. [fast]
- misspell:
    - Finds commonly misspelled English words. [fast, auto-fix]
- perfsprint:
    - Checks that fmt.Sprintf can be replaced with a faster alternative. [auto-fix]
- revive:
    - Fast, configurable, extensible, flexible, and beautiful linter for Go. Drop-in replacement of golint. [auto-fix]
- staticcheck:
    - It's the set of rules from staticcheck.
- testifylint:
    - Checks usage of github.com/stretchr/testify.
- thelper: Thelper detects tests helpers which is not start with t.Helper() method.
- unparam: Reports unused function parameters.
- unused: Checks Go code for unused constants, variables, functions and types.
- usestdlibvars: A linter that detect the possibility to use variables/constants from the Go standard library. [fast, auto-fix]
- usetesting: Reports uses of functions with replacement inside the testing package. [auto-fix]
- whitespace: Whitespace is a linter that checks for unnecessary newlines at the start and end of functions, if, for, etc. [fast, auto-fix]
- asasalint: Check for pass []any as any in variadic func(...any).
- asciicheck: Checks that all code identifiers does not have non-ASCII symbols in the name. [fast]
- bidichk: Checks for dangerous unicode character sequences. [fast]
- bodyclose: Checks whether HTTP response body is closed successfully.
- canonicalheader: Canonicalheader checks whether net/http.Header uses canonical header. [auto-fix]
- containedctx: Containedctx is a linter that detects struct contained context.Context field.
- contextcheck: Check whether the function uses a non-inherited context.
- copyloopvar: A linter detects places where loop variables are copied. [fast, auto-fix]
- cyclop: Checks function and package cyclomatic complexity. [fast]
- decorder: Check declaration order and count of types, constants, variables and functions. [fast]
- depguard: Go linter that checks if package imports are in a list of acceptable packages. [fast]
- dogsled: Checks assignments with too many blank identifiers (e.g. x, _, _, _, := f()). [fast]
- dupl: Detects duplicate fragments of code. [fast]
- dupword: Checks for duplicate words in the source code. [fast, auto-fix]
- durationcheck: Check for two durations multiplied together.
- err113: Go linter to check the errors handling expressions. [auto-fix]
- errchkjson: Checks types passed to the json encoding functions. Reports unsupported types and reports occurrences where the check for the returned error can be omitted.
- errname: Checks that sentinel errors are prefixed with the `Err` and error types are suffixed with the `Error`.
- exhaustive: Check exhaustiveness of enum switch statements.
- exhaustruct: Checks if all structure fields are initialized.
- exptostd: Detects functions from golang.org/x/exp/ that can be replaced by std functions. [auto-fix]
- fatcontext: Detects nested contexts in loops and function literals. [auto-fix]
- forbidigo: Forbids identifiers.
- forcetypeassert: Finds forced type assertions.
- funcorder: Checks the order of functions, methods, and constructors. [fast]
- funlen: Checks for long functions. [fast]
- ginkgolinter: Enforces standards of using ginkgo and gomega. [auto-fix]
- gocheckcompilerdirectives: Checks that go compiler directive comments (//go:) are valid. [fast]
- gochecknoglobals: Check that no global variables exist.
- gochecknoinits: Checks that no init functions are present in Go code. [fast]
- gochecksumtype: Run exhaustiveness checks on Go "sum types".
- gocognit: Computes and checks the cognitive complexity of functions. [fast]
- goconst: Finds repeated strings that could be replaced by a constant.
- gocyclo: Computes and checks the cyclomatic complexity of functions. [fast]
- godot: Check if comments end in a period. [fast, auto-fix]
- godox: Detects usage of FIXME, TODO and other keywords inside comments. [fast]
- goheader: Checks if file header matches to pattern. [fast, auto-fix]
- gomoddirectives: Manage the use of 'replace', 'retract', and 'excludes' directives in go.mod. [fast]
- goprintffuncname: Checks that printf-like functions are named with `f` at the end. [fast]
- gosec: Inspects source code for security problems.
- gosmopolitan: Report certain i18n/l10n anti-patterns in your Go codebase.
- grouper: Analyze expression groups. [fast]
- iface: Detect the incorrect use of interfaces, helping developers avoid interface pollution. [auto-fix]
- inamedparam: Reports interfaces with unnamed method parameters. [fast]
- interfacebloat: A linter that checks the number of methods inside an interface. [fast]
- intrange: Intrange is a linter to find places where for loops could make use of an integer range. [auto-fix]
- ireturn: Accept Interfaces, Return Concrete Types.
- lll: Reports long lines. [fast]
- loggercheck: Checks key value pairs for common logger libraries (kitlog,klog,logr,slog,zap).
- maintidx: Maintidx measures the maintainability index of each function. [fast]
- makezero: Finds slice declarations with non-zero initial length.
- mirror: Reports wrong mirror patterns of bytes/strings usage. [auto-fix]
- mnd: An analyzer to detect magic numbers. [fast]
- musttag: Enforce field tags in (un)marshaled structs.
- nakedret: Checks that functions with naked returns are not longer than a maximum size (can be zero). [fast, auto-fix]
- nestif: Reports deeply nested if statements. [fast]
- nilerr: Finds the code that returns nil even if it checks that the error is not nil.
- nilnesserr: Reports constructs that checks for err != nil, but returns a different nil value error.
- nilnil: Checks that there is no simultaneous return of `nil` error and an invalid value.
- nlreturn: Nlreturn checks for a new line before return and branch statements to increase code clarity. [fast, auto-fix]
- noctx: Finds sending http request without context.Context.
- nolintlint:
    - Reports ill-formed or insufficient nolint directives. [fast, auto-fix]
- nonamedreturns: Reports all named returns.
- nosprintfhostport: Checks for misuse of Sprintf to construct a host with port in a URL. [fast]
- paralleltest: Detects missing usage of t.Parallel() method in your Go test.
- prealloc: Finds slice declarations that could potentially be pre-allocated. [fast]
- predeclared: Find code that shadows one of Go's predeclared identifiers. [fast]
- promlinter: Check Prometheus metrics naming via promlint. [fast]
- protogetter: Reports direct reads from proto message fields when getters should be used. [auto-fix]
- reassign: Checks that package variables are not reassigned.
- recvcheck: Checks for receiver type consistency.
- rowserrcheck: Checks whether Rows.Err of rows is checked successfully.
- sloglint: Ensure consistent code style when using log/slog. [auto-fix]
- spancheck: Checks for mistakes with OpenTelemetry/Census spans.
- sqlclosecheck: Checks that sql.Rows, sql.Stmt, sqlx.NamedStmt, pgx.Query are closed.
- tagalign: Check that struct tags are well aligned. [fast, auto-fix]
- tagliatelle: Checks the struct tags.
- testableexamples: Linter checks if examples are testable (have an expected output). [fast]
- testpackage: Linter that makes you use a separate _test package. [fast]
- tparallel: Tparallel detects inappropriate usage of t.Parallel() method in your Go test codes.
- unconvert: Remove unnecessary type conversions.
- varnamelen: Checks that the length of a variable's name matches its scope.
- wastedassign: Finds wasted assignment statements.
- wrapcheck: Checks that errors returned from external packages are wrapped.
- wsl: Add or remove empty lines. [fast, auto-fix]
- zerologlint: Detects the wrong usage of `zerolog` that a user forgets to dispatch with `Send` or `Msg`.

### Formatters
https://golangci-lint.run/usage/formatters/


## False Positives
https://golangci-lint.run/docs/linters/false-positives/#preset-std-error-handling





```yaml
version: "2"
linters:
  enable:
  - ...
  exclusions:
    presets:
      - comments
      - common-false-positives
      - legacy
      - std-error-handling
```


## Reference
- https://golangci-lint.run/welcome/install/
- https://freshman.tech/linting-golang/
