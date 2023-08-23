---
title: cargo
---

## cargo
Package manager for rust.

## CLI

- `build`, `b`
    - Compile the current package
- `check`, `c`
    - Analyze the current package and report errors, but don't build object files
- `clean`
    - Remove the target directory
- `doc`, `d`
    - Build this package's and its dependencies' documentation
- `new`
    - Create a new cargo package
- `init`
    - Create a new cargo package in an existing directory
- `add`
    - Add dependencies to a manifest file
- `remove`
    - Remove dependencies from a manifest file
- `run`, `r`
    - Run a binary or example of the local package
- `test`, `t`
    - Run the tests
- `bench`
    - Run the benchmarks
- `update`
    - Update dependencies listed in Cargo.lock
- `search`
    - Search registry for crates
- `publish`
    - Package and upload this package to the registry
- `install`
    - Install a Rust binary. Default location is `$HOME/.cargo/bin`
- `uninstall`
    - Uninstall a Rust binary

## carg test
Specify the num of threads.

```
cargo test --test-threads=1
```

By default, if a test passes, Rust’s test library captures anything printed to standard output.

```
cargo test -- --show-output
```

Filter out tests by name.

```
cargo test <test-name>
```



```
cargo test --test <test-name>
```

## Configurtion
https://doc.rust-lang.org/cargo/reference/config.html

## Build scripts
- `build.rs` is compiled and executed before building the package


## Reference
- https://doc.rust-lang.org/cargo/
