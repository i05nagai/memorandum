---
title: grafana-server
---

## grafana-server


## CLI

```
grafana
```

* `-config string`
    * path to config file
* `-homepath string`
    * path to grafana install/home path, defaults to working directory
* `-packaging string`
    * describes the way Grafana was installed (default "unknown")
* `-pidfile string`
    * path to pid file
* `-profile`
    * Turn on pprof profiling
* `-profile-port int`
    * Define custom port for profiling (default 6060)
* `-test.bench regexp`
    * run only benchmarks matching regexp
* `-test.benchmem`
    * print memory allocations for benchmarks
* `-test.benchtime d`
    * run each benchmark for duration d (default 1s)
* `-test.blockprofile file`
    * write a goroutine blocking profile to file
* `-test.blockprofilerate rate`
    * set blocking profile rate (see runtime.SetBlockProfileRate) (default 1)
* `-test.count n`
    * run tests and benchmarks n times (default 1)
* `-test.coverprofile file`
    * write a coverage profile to file
* `-test.cpu list`
    * comma-separated list of cpu counts to run each test with
* `-test.cpuprofile file`
    * write a cpu profile to file
* `-test.failfast`
    * do not start new tests after the first test failure
* `-test.list regexp`
    * list tests, examples, and benchmarks matching regexp then exit
* `-test.memprofile file`
    * write an allocation profile to file
* `-test.memprofilerate rate`
    * set memory allocation profiling rate (see runtime.MemProfileRate)
* `-test.mutexprofile string`
    * write a mutex contention profile to the named file after execution
* `-test.mutexprofilefraction int`
    * if >= 0, calls runtime.SetMutexProfileFraction() (default 1)
* `-test.outputdir dir`
    * write profiles to dir
* `-test.parallel n`
    * run at most n tests in parallel (default 4)
* `-test.run regexp`
    * run only tests and examples matching regexp
* `-test.short`
    * run smaller test suite to save time
* `-test.testlogfile file`
    * write test action log to file (for use only by cmd/go)
* `-test.timeout d`
    * panic test binary after duration d (default 0, timeout disabled)
* `-test.trace file`
    * write an execution trace to file
* `-test.v`
    * verbose: print additional output
* `-v `
    * prints current version and exits

## Usage

## Configuration

## Reference
