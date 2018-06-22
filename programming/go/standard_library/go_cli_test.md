---
title: go CLI test
---

## go CLI test


## CLI
```
go test [build/test flags] [packages] [build/test flags & test binary flags]
```

* `-bench regexp`
    * Run only those benchmarks matching a regular expression.
    * By default, no benchmarks are run.
    * To run all benchmarks, use '-bench .' or '-bench=.'.
    * The regular expression is split by unbracketed slash (/) characters into a sequence of regular expressions, and each
    * part of a benchmark's identifier must match the corresponding
    * element in the sequence, if any. Possible parents of matches are run with b.N=1 to identify sub-benchmarks.
    * For example, given -bench=X/Y, top-level benchmarks matching X are run with b.N=1 to find any sub-benchmarks matching Y, which are then run in full.

* `-benchtime t`
    * Run enough iterations of each benchmark to take t, specified as a time.Duration (for example, -benchtime 1h30s).
    * The default is 1 second (1s).

* `-count n`
    * by default 1
    * Run each test and benchmark n times
    * If -cpu is set, run n times for each GOMAXPROCS value.
    * Examples are always run once.

* `-cover`
    * Enable coverage analysis.
    * Note that because coverage works by annotating the source code before compilation, compilation and test failures with coverage enabled may report line numbers that don't correspond to the original sources.

* `-covermode set,count,atomic`
    * Set the mode for coverage analysis for the package[s] being tested.
    * The default is "set" unless -race is enabled, in which case it is "atomic".
    * `set: bool`: does this statement run?
    * `count: int`: how many times does this statement run?
    * `atomic: int`: count, but correct in multithreaded tests; significantly more expensive.

* `-coverpkg pattern1,pattern2,pattern3`
    * Apply coverage analysis in each test to packages matching the patterns.
    * The default is for each test to analyze only the package being tested.
    * See 'go help packages' for a description of package patterns.
    * Sets -cover.

* `-v`
    * Verbose output: log all tests as they are run.
    * Also print all text from Log and Logf calls even if the test succeeds.

* `-vet list`
    * Configure the invocation of "go vet" during "go test" to use the comma-separated list of vet checks.
    * If list is empty, "go test" runs "go vet" with a curated list of checks believed to be always worth addressing.
    * If list is "off", "go test" does not run "go vet" at all.

## Usage

Run all tests

```
go test -v -run ''
```

Run tests maching `Foo/A=`

```
go test -run Foo/A=
```

Run and measure coverage

```
go test -v -run '' -cover
```

## Configuration

## Reference

